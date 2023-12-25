from devices.state_management import *
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar, List


class Device(ABC):
    def __init__(self, device_id, name, annihilated=False):
        self.device_id = device_id
        self.name = name
        self.annihilated = annihilated
        self._state = OFF()

    def __repr__(self):
        if self.annihilated:
            raise ValueError(f"This {self.__class__.__name__} object has been annihilated and should not be used "
                             f"anymore.")
        else:
            return f"{self.__class__.__name__}(device_id={self.device_id}, name='{self.name}')"

    def turn_on(self):
        self._state.on(self)

    def turn_off(self):
        self._state.off(self)

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State):
        print(f"Changing state on {self.name} to {state}")
        self._state = state

    @abstractmethod
    def annihilate(self):
        pass


@dataclass
class Trash:
    descr: str = 'Some bunch of trash'


@dataclass
class Apartment:
    trash: ClassVar[List] = []
    temperature: float = 25
    humidity: float = 40

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_apartement'):
            cls._apartement = super(Apartment, cls).__new__(cls, *args, **kwargs)
        return cls._apartement
