import requests
import json

response = requests.get("http://192.168.33.1/status")
# Print the status code of the response.
#print(response.content)
data = json.loads(response.text)

print(json.dumps(json.dumps(data, indent=4, sort_keys=True)))