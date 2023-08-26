import requests
import json

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=d6cd386eb2064099812135415232608&q={city}"

r = requests.get(url)

# print(r.text)

wdic = json.loads(r.text)
# print(wdic)
print()
print(wdic["location"]["name"])
print(wdic["location"]["region"])
print(wdic["current"]["temp_c"])
print(wdic["current"]["condition"]["text"])
print()