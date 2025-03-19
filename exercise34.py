#api
from collections import UserList
import requests
import webbrowser

url = "https://random.dog/woof.json"
#get post
r = requests.get(url)
print(r.text)
print(r.json())
print(r.status_code)
data = r.json()
webbrowser.open(data["url"])