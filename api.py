import requests

API_URL = 'https://superheroapi.com/api/'
TOKEN = '2619421814940190'
USER_AGENT = {"User-Agent": "Godexd"}

heroes_list = ['Hulk', 'Captain America', 'Thanos']
characteristics = ['intelligence', 'strength', 'combat']


def get_score_by_characteristic(URL, heroes_list, characteristics):
    result = []
    print(f'Loading info about {len(heroes_list)} heroes. Pls wait:')
    for hero_name in (heroes_list):
        response = requests.get(API_URL + TOKEN + '/search/' + hero_name, headers=USER_AGENT)
        data = response.json()
        if data['response'] != 'success':
            continue
        for hero in data['results']:
            if hero['name'] != hero_name:
                continue
            hero['score'] = 0
            for char in characteristics:
                try:
                    hero['score'] += int(hero['powerstats'][char])
                except ValueError:
                    pass
            result.append(hero)
    return result

heroes = get_score_by_characteristic(API_URL + TOKEN + '/search/', heroes_list, characteristics)
print(f'SuperHero is: {heroes[0]["name"]} with score: {heroes[0]["score"]}')

