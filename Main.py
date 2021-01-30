import requests
import datetime
import json

# var = ['www.pythonru', 'com']
# print ('\n'.join(var))
# today = datetime.datetime.today()
# print( today.strftime("%d.%m.%Y %H:%M") )


# url1 = 'https://json.medrating.org/todos'
# url2 = 'https://json.medrating.org/users'
# whole_json_1 = requests.get(url1)
# whole_json_2 = requests.get(url2)
# data = whole_json_1.json()
# data2 = whole_json_2.json()
# print(data, '\n', data2)


response = requests.get("https://json.medrating.org/todos")
todos = json.loads(response.text)