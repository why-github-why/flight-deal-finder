import requests


# GET IATA CODE FOR LONDON
def get_IATA_codes(city: str) -> dict:
    codes = []
    result = {}
    iata_url = "https://tequila-api.kiwi.com/locations/query"
    iata_params = {
        "term": city,
        "location_types": "airport",
        "limit": 10,
    }
    iata_headers = {
        "apikey": "_H78EQXmz-r6cOfGJwgz_9imZEmWLuXL",
        "Content-Type": "application/json",
    }
    iata_response = requests.get(iata_url, params=iata_params, headers=iata_headers)
    iata_data = iata_response.json()

    entries = range(len(iata_data['locations']))
    for entry in entries:
        iata_code = iata_data['locations'][entry]['code']
        codes.append(iata_code)
    for entry in range(len(codes)):
        city = iata_data['locations'][entry]['name']
        result[city] = codes[entry]

    print(result)
    return result
    # return f"{city}: {iata_code}"


get_IATA_codes("London")

London_IATA_codes = {
    'London Stansted': 'STN',
    'Gatwick': 'LGW',
    'Heathrow': 'LHR',
    'East London': 'ELS',
    'London City': 'LCY',
    'London Southend': 'SEN',
    'London International': 'YXU'
}

# class NotificationManager:
#     # This class is responsible for sending notifications with the deal flight details.
#     pass
