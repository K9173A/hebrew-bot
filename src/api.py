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

    :param service_name: service name.
    :param params: GET-parameters.
    :return: url.
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


def get_category(category: str):
    """
    Converts english titles to russian.

    :param category: category title.
    :return: title in russian language.
    """
    return {
        'hebdate': 'Дата',
        'candles': 'Свечи',
        'parashat': 'Параша',
        'havdalah': 'Хавдала',
        'holiday': 'Праздник',
        'roshchodesh': 'Рош Ходеш'
    }[category]


def _get_current_events():
    """
    Gets list of current date events.

    :return: information for current date events.
    """
    params = {'v': 1, 'cfg': 'json', 'year': 'now', 'month': 'x', 'maj': 'on', 'min': 'on',
              'nx': 'on', 'mf': 'on', 'ss': 'on', 'mod': 'on', 's': 'on', 'c': 'on', 'b': 18,
              'M': 'on', 'm': 50, 'D': 'on', 'd': 'on', 'o': 'on', 'i': 'off', 'geo': 'none',
              'lg': 's'}

    date = datetime.datetime.now()
    params.update({'month': date.month, 'lg': 'ru'})
    url = build_url('hebcal', **params)

    result = make_request(url)
    events = find_events(result, date.strftime('%Y-%m-%d'))

    messages = []
    for event in events:
        messages.append('\n'.join([
            f'Название: {event["title"]}',
            f'Дата: {event["date"]}',
            f'Категория: {get_category(event["category"])}',
            f'Иврит: {event["hebrew"]}'
        ]))

    return '\n\n'.join(messages) if len(messages) > 0 else 'Сегодня событий не найдено'


def _get_current_date():
    """
    Gets information about current date in hebrew calendar.

    :return: information about current date.
    """
    date = datetime.datetime.now()
    params = {
        'gy': date.year,
        'gm': date.month,
        'gd': date.day,
        'g2h': 1,
        'cfg': 'json'
    }

    url = build_url('converter', **params)
    result = make_request(url)

    gregorian_date = date.strftime('%Y-%m-%d')
    hebrew_date = f'{result["hy"]} {result["hm"]} {result["hd"]}'
    events = ', '.join(result['events'])

    return '\n'.join([
        f'Григорианский календарь: {gregorian_date}',
        f'Еврейский календарь: {hebrew_date}',
        f'Иврит: {result["hebrew"]}',
        f'События: {events}'
    ])


def process_action(action: str) -> str:
    """
    Processes data depending on what user passed in.

    :param action: keyboard button title.
    :return: result.
    """
    if action == Action.CURRENT_EVENTS:
        return _get_current_events()
    elif action == Action.CURRENT_DATE:
        return _get_current_date()
    else:
        return 'Unknown'

