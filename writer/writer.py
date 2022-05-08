from abc import ABC
from typing import Any


class Writer(ABC):
    def write(self, filename: str, data: list[dict[str, Any]]):
        raise NotImplementedError()
