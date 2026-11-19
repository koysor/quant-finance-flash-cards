import os

from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

cache = Cache()
limiter = Limiter(key_func=get_remote_address)


def edge_edit_enabled() -> bool:
    """
    True when ``ALLOW_EDGE_EDIT=1`` switches on the remove-link button.  That is
    the only runtime write: it turns off page caching, caching headers and
    read-only database connections, and creates the CSRF token.
    """
    return os.environ.get("ALLOW_EDGE_EDIT") == "1"
