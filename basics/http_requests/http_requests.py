import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
print(f"Your request to {url} came back with the status code {response.status_code}")
print(response.headers)
