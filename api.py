from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '12d11ac2-2408-42db-b534-71f4e0c7cc93',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  print()
  for i, value in enumerate(data["data"]):
    output = f'{i}:{value["name"]}'
    print(output)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)