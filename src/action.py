"""
State machine of button appearance.
"""


class Action:
    CURRENT_EVENTS = 'События текущего дня'
    CURRENT_DATE = 'Какой сегодня день?'


ACTION_STATE_MAPPER = {
    '1': {
        'title': Action.CURRENT_EVENTS,
        'next': '1'
    }
}
