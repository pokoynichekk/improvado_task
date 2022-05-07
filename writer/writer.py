from abc import ABC


class Writer(ABC):
    def write(self, filename: str, data: dict):
        raise NotImplementedError()
