import requests

api_key = "ce85d82de6691557571ab4c1b0971efa"
city = "Pune"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
res = requests.get(url).json()
print(res)