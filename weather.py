import requests
def get_weather(user_input):
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
    city = user_input
    url = api_address + city
    json_data = requests.get(url).json()
    weather ={
        "description": json_data["weather"][0]["description"],
        "temp":json_data["main"]["temp"]-(273.15)
    }
    answer = "Today in {} is {}, daily temperature is {:.1f}" \
        .format(city,weather["description"],weather["temp"])
    return answer


