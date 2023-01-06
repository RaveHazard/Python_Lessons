import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

print("Status code " + str(response.status_code))
assert 200 == response.status_code, "qweqeqw"
if response.status_code == 200:
    print("Success, we take new joke")
else:
    print("Filed, request failed")
response.encoding = 'utf-8'
print(response.text)




