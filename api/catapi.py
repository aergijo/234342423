import requests
import json

def getapi():
    ds = requests.get("https://api.thecatapi.com/v1/images/search").content
    data = json.loads(ds)
    urls = [item["url"] for item in data]
 #   print(urls[0])
    return urls[0]