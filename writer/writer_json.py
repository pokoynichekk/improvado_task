import json
from writer.writer import Writer


class WriterJson(Writer):
    def __init__(self, indent: int):
        self.indent = indent

    def write(self, filename: str, data: dict) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=self.indent)
