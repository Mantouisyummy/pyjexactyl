"""Pydactyl constants."""

__version__ = '2.0.4'
USER_AGENT = 'Pyjexactyl/' + __version__

POWER_SIGNALS = ('start', 'stop', 'restart', 'kill')
REQUEST_TYPES = ('GET', 'POST', 'PATCH', 'DELETE', 'PUT')
SCHEDULE_ACTIONS = ('command', 'power', 'backup')
USE_SSL = {True: 'https', False: 'http'}
