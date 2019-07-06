import requests
def get_joke():
    url = "http://api.icndb.com/jokes/random?firstName=John&amp;lastName=Doe"
    json_data = requests.get(url).json()
    joke = json_data["value"]["joke"]
    return joke

