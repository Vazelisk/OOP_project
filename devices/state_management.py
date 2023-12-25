from logger_config import logger


class State:
    def on(self, m) -> None:
        logger.info("already ON")

    def off(self, m) -> None:
        logger.info("already OFF")

    def __repr__(self):
        return f"<State: {self.__class__.__name__}>"


class ON(State):
    def off(self, m):
        logger.info("going from ON to OFF")
        m._state = OFF()


class OFF(State):
    def on(self, m):
        logger.info("going from OFF to ON")
        m._state = ON()
