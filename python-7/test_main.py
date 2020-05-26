from main import get_temperature
from unittest import mock


def test_get_temperature_by_lat_lng():
    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16

    response = {
        'currently': {
            'temperature': temperature
        }
    }

    fake_api = mock.patch('main.requests.get').start()
    fake_api.return_value.json.return_value = response
    result = get_temperature(lat, lng)
    fake_api.stop()

    assert result is expected
