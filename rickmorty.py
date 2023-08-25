import requests

url = "https://rickandmortyapi.com/api/character"
params = {'name': 'Morty'}  # 'name' alanı 'Morty' olan karakterleri filtrelemek için

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for character in data['results']:
    
        print(character['name'])
else:
    print("İstek başarısız oldu Hata kodu:", response.status_code)