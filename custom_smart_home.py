from devices.models import *
from logger_config import logger
import emoji


class DeskLamp(Device):
    def __init__(self, device_id, name, annihilated=False):
        super().__init__(device_id, name, annihilated)

    def annihilate(self):
        logger.info(
            emoji.emojize(
                f"ANNIHILATING {self.__class__.__name__}, WATCH OUT! \U0001F600"
            )
        )
        Apartment.trash.append(Trash(f"some {self.__class__.__name__} trash"))
        Apartment.temperature += 10
        for attribute in list(self.__dict__.keys()):
            delattr(self, attribute)


class Humidifier(Device):
    def __init__(self, device_id, name, annihilated=False):
        super().__init__(device_id, name, annihilated)

    def annihilate(self):
        logger.info(
            f"FLOATING COMES BECAUSE OF {self.__class__.__name__}, WATCH OUT! :thumbs_up:"
        )
        Apartment.trash.append(Trash(f"some {self.__class__.__name__} trash"))
        Apartment.humidity += 10
        for attribute in list(self.__dict__.keys()):
            delattr(self, attribute)
