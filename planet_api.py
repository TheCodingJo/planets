import requests

name = 'Neptune'
api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'K2YKactzA3BM2y31zmFXYA==sbVsnIj4ub7ys4Kt'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)