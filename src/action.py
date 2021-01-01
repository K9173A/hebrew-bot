"""
State machine of button appearance.
"""


class Action:
    GET_TODAY_INFORMATION = 'Какой сегодня день?'


ACTION_STATE_MAPPER = {
    '1': {
        'title': Action.GET_TODAY_INFORMATION,
        'next': '1'
    }
}
