import requests

ENDPOINT = 'https://dlp-wt.wdprapps.disney.com/prod/v1/waitTimes'
TOKEN = '3jPT5qMimN3kR2kxqd1ez9iF1C68CrBf7zw5ICo4'
HEADERS = {
   "content-type": "application/json",
   "x-api-key": TOKEN
}

r = requests.get(ENDPOINT, headers=HEADERS)
print(r.status_code, r.json())
