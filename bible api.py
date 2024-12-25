
print("bible api")
import requests
import json
bible=str(input("what book are you looking for:   "))
chapter=int(input("what chapter are you looking for:    "))
verse=int(input("what verse are you looking for:   "))
url=f"https://bible-api.com/{bible}%20{chapter}:{verse}"
response=requests.get(url)
one=response.json()
print()
print(one["text"])

