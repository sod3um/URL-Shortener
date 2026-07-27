import requests, sys

response = requests.post("http://127.0.0.1:8000/api/create", json={
    "url": sys.argv[1]
})

print(response.text)