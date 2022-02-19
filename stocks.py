# Be sure to install the requests library first!
import requests

my_api_key = 'iFk4u3kWxv8Msm3cPZ0CCMDTio30REM_'
response = requests.get(f'https://api.polygon.io/v1/open-close/AAPL/2020-10-14?adjusted=true&apiKey={my_api_key}').json()

print(response)