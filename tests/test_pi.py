import pytest

from bumle_service_event_scraper_cron.pi import pi


def test_pi():
    assert 3.14 == pytest.approx(pi, 0.01)
