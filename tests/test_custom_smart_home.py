import pytest
from devices.models import Trash, Apartment
from custom_smart_home import DeskLamp, Humidifier
import os


log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)


@pytest.fixture
def basic_lamp():
    return DeskLamp(device_id=1, name="Basic Lamp")


@pytest.fixture
def basic_humidifier():
    return Humidifier(device_id=2, name="Basic Humidifier")


def test_desklamp_initialization(basic_lamp):
    assert basic_lamp.device_id == 1
    assert basic_lamp.name == "Basic Lamp"
    assert not basic_lamp.annihilated


def test_humidifier_initialization(basic_humidifier):
    assert basic_humidifier.device_id == 2
    assert basic_humidifier.name == "Basic Humidifier"
    assert not basic_humidifier.annihilated


def test_desklamp_annihilate_effects(basic_lamp):
    initial_trash_len = len(Apartment.trash)
    initial_temperature = Apartment.temperature
    basic_lamp.annihilate()
    assert len(Apartment.trash) == initial_trash_len + 1
    assert isinstance(Apartment.trash[-1], Trash)
    assert Apartment.temperature == initial_temperature + 10


def test_humidifier_annihilate_effects(basic_humidifier):
    initial_trash_len = len(Apartment.trash)
    initial_humidity = Apartment.humidity
    basic_humidifier.annihilate()
    assert len(Apartment.trash) == initial_trash_len + 1
    assert isinstance(Apartment.trash[-1], Trash)
    assert Apartment.humidity == initial_humidity + 10
