"""
hebcal.com API wrapper.
"""
import datetime
import requests
import typing

from src.action import Action


def build_url(service_name: str, **params) -> str:
    """
    Builds API url string.

    :param service_name: service name ()
    :param params:
    :return:
    """
    url = f'https://www.hebcal.com/{service_name}?'

    for key, value in params.items():
        url += f'{key}={value}&'

    return url[:-1]


def find_events(data: typing.Dict, date: str) -> typing.List:
    """
    Searches events for current `date` in `data`.

    :param data: hebcal JSON response with calendar events.
    :param date: date of the event.
    :return: list with events.
    """
    matched_events = []

    if 'items' in data:
        for event in data['items']:
            if event['date'].startswith(date):
                matched_events.append(event)

    return matched_events


def make_request(url: str) -> typing.Dict:
    """
    Calls API url and returns data as json.

    :param url: URL to be called.
    :returns: dict with response data.
    """
    try:
        response = requests.get(url)
    except requests.Timeout:
        return {}
    else:
        return response.json()


def _get_current_events():
    params = {'v': 1, 'cfg': 'json', 'year': 'now', 'month': 'x', 'maj': 'on', 'min': 'on',
              'nx': 'on', 'mf': 'on', 'ss': 'on', 'mod': 'on', 's': 'on', 'c': 'on', 'b': 18,
              'M': 'on', 'm': 50, 'D': 'on', 'd': 'on', 'o': 'on', 'i': 'off', 'geo': 'none',
              'lg': 's'}

    date = datetime.datetime.now()
    params.update({'month': date.month, 'lg': 'ru'})
    url = build_url('hebcal', **params)

    result = make_request(url)
    events = find_events(result, date.strftime('%Y-%m-%d'))

    print(events)


def _get_converted_date():
    default_params = {'gy': 2011, 'gm': 6, 'gd': 2, 'g2h': 1, 'gs': 'on', 'cfg': 'json',
                      'hy': 5749, 'hm': 'Kislev', 'hd': 25, 'h2g': 1}
    service_name = 'converter'


def process_action(action):
    if action == Action.GET_TODAY_INFORMATION:
        _get_current_events()
    else:
        _get_converted_date()
