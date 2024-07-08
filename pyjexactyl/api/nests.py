from pyjexactyl.api.base import JexactylAPI
from pyjexactyl.responses import PaginatedResponse
from pyjexactyl.api import base

from pyjexactyl.dataclasses.application.base import NestDataclass, EggDataclass

class Nests(JexactylAPI):
    """Class for interacting with the Pterdactyl Nests API."""

    def list_nests(self, includes=None, params=None):
        """List all nests.

        Args:
            includes(iter): List of includes, e.g. ('eggs', 'servers')
            params(dict): Extra parameters to pass, e.g. {'per_page': 300}
        """
        endpoint = 'application/nests'
        response = self._api_request(endpoint=endpoint, includes=includes,
                                     params=params)
        return PaginatedResponse(self, endpoint, response, dataclass_object=NestDataclass)

    def get_nest_info(self, nest_id, includes=None, params=None):
        """Get detailed info for the specified nest.

        Args:
            nest_id(int): Pterodactyl Nest ID.
            includes(iter): List of includes, e.g. ('eggs', 'servers')
            params(dict): Extra parameters to pass, e.g. {'per_page': 300}
        """
        response = self._api_request(
            endpoint='application/nests/{}'.format(nest_id),
            includes=includes, params=params)
        return NestDataclass(base.parse_response(response))

    def get_eggs_in_nest(self, nest_id, includes=None, params=None):
        """Get detailed info for the specified nest.

        Args:
            nest_id(int): Pterodactyl Nest ID.
            includes(iter): List of includes, e.g. ('config', 'nest', 'script')
            params(dict): Extra parameters to pass, e.g. {'per_page': 300}
        """
        response = self._api_request(
            endpoint='application/nests/{}/eggs'.format(nest_id),
            includes=includes, params=params)
        return [EggDataclass(**egg) for egg in base.parse_response(response)]

    def get_egg_info(self, nest_id, egg_id, includes=None, params=None):
        """Get detailed info for the specified egg.

        Args:
            nest_id(int): Pterodactyl Nest ID.
            egg_id(int): Pterodactyl Egg ID.
            includes(iter): List of includes, e.g. ('config', 'nest', 'script')
            params(dict): Extra parameters to pass, e.g. {'per_page': 300}
        """
        response = self._api_request(
            endpoint='application/nests/{}/eggs/{}'.format(nest_id, egg_id),
            includes=includes, params=params)
        return NestDataclass(base.parse_response(response))
