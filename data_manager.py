import requests


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/ce3e0494effc0ceae503ec088710bc16/flightDeals/sheet1"
        self.sheety_headers = {
            "Authorization": "Basic c210cGxpYjI6NWgzM3R5IyE="
        }
        sheety_response = requests.get(self.SHEETY_ENDPOINT, headers=self.sheety_headers)
        self.sheety_data = sheety_response.json()
        city = self.sheety_data['sheet1'][0]['city']
        lowest_price = self.sheety_data['sheet1'][0]['lowestPrice']
        print(self.sheety_data, city, lowest_price)
