import requests
url = "https://icanhazdadjoke.com"

# response = requests.get(url, headers={"Accept":"text/plain"})
# print(response.text)

response = requests.get(url, headers={"Accept":"application/json"})

print(response.json()["joke"])
