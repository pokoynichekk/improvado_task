import requests


class VkApi:
    def __init__(self, token: str, version: str):
        self.token = token
        self.version = version

    def get_friends_info(self, user_id: int):
        params = {
            'access_token': self.token,
            'user_id': user_id,
            'v': self.version,
            'fields': 'country, city, bdate, sex',
            'count': 5000,
            'offset': 0
        }
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        yield from response.json()['response']['items']
        while len(response.json()['response']['items']) == 5000:
            params['offset'] += 5000
            response = requests.get('https://api.vk.com/method/friends.get', params=params)
            yield from response.json()['response']['items']
