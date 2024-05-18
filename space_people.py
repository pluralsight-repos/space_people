import requests

# Get my IP
# response = requests.get('https://httpbin.org/ip')
# print('Your ip is {0}'.format(response.json()['origin']))

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

# print(json)

print('The people currently in space are:')
for p in json['people']:
    print(p['name'])



