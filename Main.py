import requests

url ='https://json.medrating.org/todos'
r = requests.get(url)
data = r.json()
print(data)