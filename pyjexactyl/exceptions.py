"""Error classes for PyJexactyl."""


class PyJexactylError(Exception):
    """Base error class."""
    pass

class BadRequestError(PyJexactylError):
    """Raised when a request is passed invalid parameters."""
    pass


class ClientConfigError(PyJexactylError):
    """Raised when a client configuration error exists."""
    pass


class JexactylApiError(PyJexactylError):
    """Used to re-raise errors from the Jexactyl API."""
    pass
