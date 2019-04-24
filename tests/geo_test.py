from requests import exceptions

import pytest

import geo


def test_get_localization():
    try:
        geo.get_localization()
    except exceptions.HTTPError:
        pytest.fail("Unable to get localization")
