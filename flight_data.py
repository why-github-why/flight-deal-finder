import requests


# This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self):

        self.SHEETY_ENDPOINT = "https://api.sheety.co/ce3e0494effc0ceae503ec088710bc16/flightDeals/sheet1"
        self.IATA_URL = "https://tequila-api.kiwi.com/locations/query"  # IATA Codes Query
        self.KIWI_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
        self.KIWI_API_KEY = "_H78EQXmz-r6cOfGJwgz_9imZEmWLuXL"

        self.sheety_headers = {
            "Authorization": "Basic c210cGxpYjI6NWgzM3R5IyE="
        }
        sheety_response = requests.get(self.SHEETY_ENDPOINT, headers=self.sheety_headers)
        self.sheety_data = sheety_response.json()

    def update_IATA(self):
        for i in range(len(self.sheety_data['sheet1'])):
            # GET CITY, LOWEST PRICE DATA
            city = self.sheety_data['sheet1'][i]['city']
            lowest_price = self.sheety_data['sheet1'][i]['lowestPrice']
            print(city, lowest_price)

            # GET IATA CODES
            iata_params = {
                "term": city,
                "location_types": "airport",
                "limit": 10,

            }
            iata_headers = {
                "apikey": self.KIWI_API_KEY,
                "Content-Type": "application/json",
            }

            iata_response = requests.get(self.IATA_URL, params=iata_params, headers=iata_headers)
            iata_data = iata_response.json()
            iata_code = iata_data['locations'][0]['code']
            print(f"{city}: {iata_code}")

            # UPDATE SHEETY TO INCLUDE IATA CODES
            update_url = f"https://api.sheety.co/ce3e0494effc0ceae503ec088710bc16/flightDeals/sheet1/"
            sheety_params = {
                "sheet1": {
                    "city": city,
                    "iataCode": iata_code,
                    "lowestPrice": lowest_price,
                }
            }
            requests.post(url=update_url, json=sheety_params, headers=self.sheety_headers)
            print(f"{city} updated!")

