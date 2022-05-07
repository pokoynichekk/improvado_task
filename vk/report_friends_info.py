from vk.report import Report


class FriendsReport(Report):
    def get_city(self, temp: dict, info: dict) -> dict:
        if 'city' in info:
            temp['city'] = info['city']['title']
        else:
            temp['city'] = 'Unknown'
        return temp

    def get_country(self, temp: dict, info: dict) -> dict:
        if 'country' in info:
            temp['country'] = info['country']['title']
        else:
            temp['country'] = 'Unknown'
        return temp

    def get_sex(self, temp: dict, info: dict) -> dict:
        if info['sex'] == 1:
            temp['sex'] = 'Жен.'
        elif info['sex'] == 2:
            temp['sex'] = 'Муж.'
        return temp

    def get_birth_date(self, temp: dict, info: dict) -> dict:
        if 'bdate' in info:
            date = info['bdate'].split('.')
            temp['birth_date'] = '.'.join(reversed(date))
        else:
            temp['birth_date'] = 'Unknown'
        return temp

    def get_data(self, user_id: int):
        data = []
        friends_info = self.api.get_friends_info(user_id)['items']
        for info in friends_info:
            temp = {'first_name': info['first_name'],
                    'last_name': info['last_name']}
            self.get_country(temp, info)
            self.get_city(temp, info)
            self.get_birth_date(temp, info)
            self.get_sex(temp, info)
            data.append(temp)
        return data
