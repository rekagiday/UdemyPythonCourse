import requests
import random

url = url = "https://icanhazdadjoke.com/search"

topic = input("Let me tell you a joke! Give me a topic: ")

response = requests.get(
    url,
    headers={"Accept":"application/json"},
    params={"term": topic}
    )

jokes = len(response.json()["results"])
if jokes == 1:
    print(f"I\'ve got one joke about {topic}. Here it is: {response.json()['results'][0]['joke']}")
elif jokes == 0:
    print(f"Sorry, I dont know any jokes about {topic}. Try something else.")
else:
    random_joke = random.randint(0, jokes)
    print(f"I\'ve got {jokes} jokes about {topic}. Here is one: {response.json()['results'][random_joke]['joke']}")
