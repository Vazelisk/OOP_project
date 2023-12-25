from devices.models import *
from logger_config import logger


class DeskLamp(Device):
    def __init__(self, device_id, name, annihilated=False):
        super().__init__(device_id, name, annihilated)

    def annihilate(self):
        logger.info(f"ANNIHILATING {self.__class__.__name__}, WATCH OUT!")
        Apartment.trash.append(Trash(f'some {self.__class__.__name__} trash'))
        Apartment.temperature += 10
        for attribute in list(self.__dict__.keys()):
            delattr(self, attribute)


class Humidifier(Device):
    def __init__(self, device_id, name, annihilated=False):
        super().__init__(device_id, name, annihilated)

    def annihilate(self):
        logger.info(f"ANNIHILATING {self.__class__.__name__}, WATCH OUT!")
        Apartment.trash.append(Trash(f'some {self.__class__.__name__} trash'))
        Apartment.humidity += 10
        for attribute in list(self.__dict__.keys()):
            delattr(self, attribute)


lamp = DeskLamp(device_id=1, name='simple lamp')


lamp.turn_on()
print(lamp.state)

lamp.turn_on()

print(lamp.state)

lamp.turn_off()

print(lamp.state)

lamp.state = ON()
print(lamp.state)


print('####')

ap = Apartment()
print(ap.trash)
lamp.annihilate()
print(ap.trash)
ap2 = Apartment()
print(ap.trash)