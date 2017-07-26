import unittest
import requests

API_KEY="837e403d4c5425a98031c4b235758aad"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}"
location = "Kent,OH"
def get_weather(location):
    #response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Kent,OH&APPID=API_KEY")
    #print("response.status_code= ", response.status_code)
    response = requests.get(url.format(location,API_KEY))
    data=response.json()
    #print("response.json= ", data)
    #print(data['name'])
    #print(data['main'])
    temperature= data['main']['temp']-270
    humidity = data['main']['humidity']
    return temperature,humidity

class TestStringMethods(unittest.TestCase):

    def test_weather_data(self):
        temperature, humidity =get_weather("Kent,OH")
        assert 5<= humidity <= 95
        assert -20 <= temperature <= 90
if __name__ == '__main__':
    unittest.main(verbosity=2)