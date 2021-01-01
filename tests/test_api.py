import json
import os
import unittest
from unittest.mock import patch

import requests

from src.api import build_url, make_request, find_events


class TestBuildUrl(unittest.TestCase):
    def test_url_with_params(self):
        result = build_url('my_cool_service', foo=True, bar=42, baz=None)
        self.assertEqual(
            first=result,
            second='https://www.hebcal.com/my_cool_service?foo=True&bar=42&baz=None'
        )

    def test_url_without_params(self):
        result = build_url('my_cool_service')
        self.assertEqual(
            first=result,
            second='https://www.hebcal.com/my_cool_service'
        )


class TestFindEvents(unittest.TestCase):
    def setUp(self) -> None:
        path = os.path.join(os.path.dirname(__file__), 'sample_data.json')
        with open(path, encoding='utf-8') as f:
            self.data = json.load(f)

    def test_events_found(self):
        result = find_events(self.data, '2020-12-16')
        self.assertEqual(
            first=result,
            second=[
                {
                    "title": "Ханука: 7 Свечей",
                    "date": "2020-12-16T19:15:00-03:00",
                    "category": "holiday",
                    "subcat": "major",
                    "title_orig": "Chanukah: 7 Candles",
                    "hebrew": "חנוכה: ז׳ נרות",
                    "leyning": {
                        "1": "Numbers 28:1 - 28:5",
                        "2": "Numbers 28:6 - 28:10",
                        "3": "Numbers 28:11 - 28:15",
                        "torah": "Numbers 28:1-28:15; 7:42-7:47",
                        "maftir": "Numbers 7:42 - 7:47"
                    },
                    "link": "https://www.hebcal.com/holidays/chanukah-2020?utm_source=js&utm_medium=api",
                    "memo": "Hanukkah, the Jewish festival of rededication. Also known as the Festival of Lights"
                },
                {
                    "title": "Новый Месяц Тевет",
                    "date": "2020-12-16",
                    "category": "roshchodesh",
                    "title_orig": "Rosh Chodesh Tevet",
                    "hebrew": "ראש חודש טבת",
                    "link": "https://www.hebcal.com/holidays/rosh-chodesh-tevet-2020?utm_source=js&utm_medium=api",
                    "memo": "Beginning of new Hebrew month of Tevet. Tevet is the 10th month of the Hebrew year. Corresponds to December or January on the Gregorian calendar"
                }
            ]
        )


class TestMakeRequest(unittest.TestCase):
    @patch('requests.get')
    def test_request_timeout(self, m_get):
        def get(*args, **kwargs):
            raise requests.Timeout()

        m_get.side_effect = get
        result = make_request('https://jsonplaceholder.typicode.com/todos/1')
        self.assertEqual(first=result, second={})


if __name__ == '__main__':
    unittest.main()
