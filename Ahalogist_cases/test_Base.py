import pytest


@pytest.mark.usefixtures("ses_init")
class Session_base:
    pass


@pytest.mark.usefixtures("temp_ses_init")
class Session_temp_base:
    pass
