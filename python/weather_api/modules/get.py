from requests import get
import json


def get_data(city):
    appid = "xxx"
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = get(url, params={"appid": appid, "q": city, "units": "metric"})
    data = json.loads(response.content)
    return data
