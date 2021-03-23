import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta  # pip install python-dateutil

from_location = "London"  # IATA: LHR

today = datetime.now().strftime("%d/%m/%Y")  # date format: dd/mm/yyyy
tomorrow = (datetime.now() + relativedelta(days=+1)).strftime("%d/%m/%Y")
six_months_from_now = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")
print(today, tomorrow, six_months_from_now)

# KIWI
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_API_KEY = "**********"

# SEARCH
kiwi_params = {
    "fly_from": "LHR",
    "fly_to": "BER",
    "dateFrom": today,
    "dateTo": tomorrow,
    "curr": "USD",
}

kiwi_headers = {
    "apikey": KIWI_API_KEY,
    "Content-Type": "application/json",
}

kiwi_response = requests.get(KIWI_ENDPOINT, params=kiwi_params, headers=kiwi_headers)
kiwi_response.raise_for_status()
kiwi_data = kiwi_response.json()

prices = []
for i in range(len(kiwi_data['data'])):
    price = kiwi_data['data'][i]['conversion']['USD']
    prices.append(price)

print(prices)
lowest_price = prices[0]
print(f"Lowest price: ${lowest_price}")


# GET IATA CODE FOR LONDON
def get_IATA_codes(city: str) -> list:
    all_codes = []
    iata_url = "https://tequila-api.kiwi.com/locations/query"
    iata_params = {
        "term": city,
        "location_types": "airport",
        "limit": 10,

    }
    iata_headers = {
        "apikey": "**********",
        "Content-Type": "application/json",
    }
    iata_response = requests.get(iata_url, params=iata_params, headers=iata_headers)
    iata_data = iata_response.json()

    for entry in range(len(iata_data['locations'])):
        iata_code = iata_data['locations'][entry]['code']
        all_codes.append(iata_code)

    return all_codes
    # return f"{city}: {iata_code}"


print(get_IATA_codes("London"))




