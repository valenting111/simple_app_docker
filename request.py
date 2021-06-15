# Simple script to ping the API and check it works correctly
import requests

message = {"item_id": 10}

# Modify url of server to yours
url = "http://127.0.0.1:8000"

# response store the data sent back from the api in a JSON format
response1 = requests.get(url)

print(response1.text)

# Try another endpoint
response2 = requests.get(url + "/test")

print(response2.text)

response3 = requests.get(
    url + "/items/{}".format(message["item_id"]), params=message)

print(response3.text)
