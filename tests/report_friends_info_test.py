from unittest import TestCase
from unittest.mock import Mock
from vk.report_friends_info import FriendsReport


class FriendsReportTest(TestCase):
    def setUp(self):
        api = Mock()
        api.get_friends_info.return_value = {
            'items': [{
                'first_name': 'Павел',
                'last_name': 'Дуров',
                'country': {'id': 1, 'title': 'Россия'},
                'city': {'id': 2, 'title': 'Санкт-Петербург'},
                'bdate': '10.10.1984',
                'sex': 2,
            }]
        }
        self.report = FriendsReport(api=api)

    def test_get_city(self):
        self.assertEqual(
            self.report.get_city(
                {}, {'city': {'id': 2, 'title': 'Санкт-Петербург'}}
            ),
            {'city': 'Санкт-Петербург'}
        )

    def test_get_city_no_city(self):
        self.assertEqual(self.report.get_city({}, {}), {'city': 'Unknown'})

    def test_get_country(self):
        self.assertEqual(
            self.report.get_country(
                {}, {'country': {'id': 1, 'title': 'Россия'}}
            ),
            {'country': 'Россия'}
        )

    def test_get_country_no_country(self):
        self.assertEqual(self.report.get_country({}, {}), {'country': 'Unknown'})

    def test_get_sex(self):
        self.assertEqual(self.report.get_sex({}, {'sex': 2}), {'sex': 'Муж.'})

    def test_get_birth_date(self):
        self.assertEqual(
            self.report.get_birth_date(
                {}, {'bdate': '10.10.1984'}
            ),
            {'birth_date': '1984.10.10'}
        )

    def test_get_birth_date_no_year(self):
        self.assertEqual(
            self.report.get_birth_date(
                {}, {'bdate': '17.10'}
            ),
            {'birth_date': '10.17'}
        )

    def test_get_birth_date_no_date(self):
        self.assertEqual(
            self.report.get_birth_date(
                {}, {}
            ),
            {'birth_date': 'Unknown'}
        )
