import pytest


@pytest.mark.usefixtures("ses_init")
class Session_base:
    pass
