import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "abc123", "content": "Hello World"})

print(get_response.json())
print(get_response.status_code)