import pytest
from devices.models import Device, Trash, Apartment
from custom_smart_home import DeskLamp
from devices.state_management import ON, OFF


class TestDevice(Device):
    def annihilate(self):
        pass


@pytest.fixture
def device():
    return TestDevice(device_id=1, name="TestDevice")


def test_device_initial_state(device):
    assert isinstance(device.state, OFF)


def test_device_turn_on(device):
    device.turn_on()
    assert isinstance(device.state, ON)


def test_device_turn_off(device):
    device.turn_on()
    device.turn_off()
    assert isinstance(device.state, OFF)


def test_device_turn_off(caplog, device):
    device.turn_on()
    device.turn_on()
    with caplog.at_level("INFO"):
        assert "already ON" in caplog.text


def test_desklamp_initial_state():
    lamp = DeskLamp(device_id=2, name="DeskLamp")
    assert isinstance(lamp.state, OFF)


def test_desklamp_annihilate():
    lamp = DeskLamp(device_id=2, name="DeskLamp")
    lamp.annihilate()
    assert hasattr(lamp, "device_id") is False


def test_apartment_singleton():
    ap1 = Apartment()
    ap2 = Apartment()
    assert ap1 is ap2


def test_apartment_trash_collection():
    previous_trash_length = len(Apartment.trash)
    lamp = DeskLamp(device_id=3, name="DeskTrashLamp")
    lamp.annihilate()
    assert len(Apartment.trash) == previous_trash_length + 1
    assert isinstance(Apartment.trash[-1], Trash)
