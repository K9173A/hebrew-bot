import requests


BASE_URL = 'https://www.hebcal.com/converter'


def get_hebrew_month_name(month_number):
    """
    Takes hebrew month name by its number.
    :param month_number: month number (1 to 13).
    :return: month name.
    """
    return ['Nisan', 'Iyyar', 'Sivan', 'Tamuz', 'Av', 'Elul', 'Tishrei',
            'Cheshvan', 'Kislev', 'Tevet', 'Shvat', 'Adar1', 'Adar2'][month_number - 1]


def prepare_url(**kwargs):
    """
    Makes full URL from passed kwargs.

    >>> prepare_url(gy=1995, gm=3, gd=9)
    'https://www.hebcal.com/converter?gy=1995&gm=3&gd=9'

    :param kwargs: URL args.
    :return: full URL.
    """
    url = f'{BASE_URL}?'
    for key, value in kwargs.items():
        url += f'{key}={value}&'
    return url[:-1]


def make_request(url):
    """
    Makes request to `url`.

    >>> make_request('https://www.hebcal.asdfg')
    {}

    >>> make_request('https://www.hebcal.com/converter?cfg=json&hy=5749&hm=Kislev&hd=25&h2g=1')
    {'gy': 1988, 'gm': 12, 'gd': 4, 'afterSunset': False, 'hy': 5749, 'hm': 'Kislev', 'hd': 25, 'hebrew': 'כ״ה בְּכִסְלֵו תשמ״ט', 'events': ['Chanukah: 2 Candles', 'Parashat Miketz']}

    :param url: URL string.
    :return: response content (dict).
    """
    try:
        response = requests.get(url)
    except Exception:
        return {}
    else:
        return response.json()


def from_gregorian_to_hebrew(year, month, day):
    """
    Converts gregorian date to hebrew date.

    >>> from_gregorian_to_hebrew(2011, 6, 2)
    {'gy': 2011, 'gm': 6, 'gd': 2, 'afterSunset': False, 'hy': 5771, 'hm': 'Iyyar', 'hd': 29, 'hebrew': 'כ״ט בְּאִיָיר תשע״א', 'events': ['Parashat Nasso']}

    :param year: gregorian year (e.g. 2007).
    :param month: gregorian month number (e.g. 4).
    :param day: gregorian day (e.g. 31).
    :return: `dict` with hebrew equivalent of gregorian date.
    """
    return make_request(prepare_url(gy=year, gm=month, gd=day, g2h=1, cfg='json'))


def from_hebrew_to_gregorian(year, month, day):
    """
    Converts hebrew date to gregorian date.

    >>> from_hebrew_to_gregorian(5749, 9, 25)
    {'gy': 1988, 'gm': 12, 'gd': 4, 'afterSunset': False, 'hy': 5749, 'hm': 'Kislev', 'hd': 25, 'hebrew': 'כ״ה בְּכִסְלֵו תשמ״ט', 'events': ['Chanukah: 2 Candles', 'Parashat Miketz']}

    :param year: hebrew year (e.g. 5771).
    :param month: hebrew month name (e.g. 'Iyyar').
    :param day: hebrew day (e.g. 17).
    :return: `dict` with gregorian equivalent of hebrew date.
    """
    try:
        month_name = get_hebrew_month_name(month_number=month)
    except IndexError as e:
        print(e)
    else:
        return make_request(prepare_url(hy=year, hm=month_name, hd=day, h2g=1, cfg='json'))


def get_hebrew_date(year, month, day):
    data = from_gregorian_to_hebrew(year, month, day)
    return f'''
    Year: {data['hy']}
    Month: {data['hm']}
    Day: {data['hd']}
    Hebrew: {data['hebrew']}
    Events: {",".join(data['events'])}
    '''


def get_gregorian_date(year, month, day):
    pass
