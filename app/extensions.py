import os


def edge_edit_enabled() -> bool:
    """
    True when ``ALLOW_EDGE_EDIT=1`` switches on the remove-link button.  That is
    the only runtime write: it makes request database connections writable and
    creates the CSRF token.
    """
    return os.environ.get("ALLOW_EDGE_EDIT") == "1"
