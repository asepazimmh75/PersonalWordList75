import requests

api_key = '826a6099-855b-40e8-8b73-a542a9d13eae'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definitions in definitions:
    print(definitions)