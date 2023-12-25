import math
from typing import Union, List


class Car:
    def __init__(self, x=0, y=0, speed=0, angle=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.angle = angle


class Command:
    def __init__(self, speed=0, angle=0, created_at=0):
        self.speed = speed
        self.created_at = created_at
        self.angle = angle


class CommandQueue:
    def __init__(self, car: Car, command_queue: Union[Command, List[Command]] = None):
        self.command_queue = command_queue
        self.car = car

        if not isinstance(self.command_queue, list):
            self.command_queue = [self.command_queue]

        commands_times = []
        for command in self.command_queue:
            commands_times.append(command.created_at)

        sorted_commands = commands_times.copy()
        sorted_commands.sort()
        if commands_times != sorted_commands:
            raise Exception("Commands are given in wrong time order")

    def move(self, command_queue):
        for i, command in enumerate(command_queue):
            self.car.speed += command.speed
            try:
                duration = self.command_queue[i+1].created_at - self.command_queue[-i].created_at
            except IndexError:
                duration = 0

            delta_x = self.car.speed * math.cos(command.angle) * duration
            delta_y = self.car.speed * math.sin(command.angle) * duration
            self.car.x += delta_x
            self.car.y += delta_y

    def get_position(self, created_at=0):
        commands = [command for command in self.command_queue if command.created_at < created_at]
        self.move(commands)

        return self.car.x, self.car.y


cmd1 = Command(1, 10, 0)
cmd2 = Command(2, 10, 3)
t = CommandQueue(Car(), [cmd1, cmd2])
t.move(t.command_queue)
t.get_position()
# (-2.517214587229357, -1.6320633326681093)