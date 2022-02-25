from urllib import response
import requests # bringing request library

try:
    response = requests.get('https://catfact.ninja/fact')#.json() # creating data variable .get will fetch resource need API url and turn response to json
    print(response.status_code)
    print(response.text)
    print(response.json)

    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')
