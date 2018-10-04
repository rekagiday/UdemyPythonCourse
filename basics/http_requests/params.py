import requests

url = url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term":"cat", "limit":1}
    )

print(response.json()["results"][0]["joke"]) 
