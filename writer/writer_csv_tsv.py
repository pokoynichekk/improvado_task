from writer.writer import Writer
import csv


class WriterCsvTsv(Writer):
    def __init__(self, delimiter: str):
        self.delimiter = delimiter

    def write(self, filename: str, data: dict) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            fieldnames = ['first_name', 'last_name', 'country', 'city', 'birth_date', 'sex']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self.delimiter)
            writer.writeheader()
            for info in data:
                writer.writerow({'first_name': info['first_name'], 'last_name': info['last_name'],
                                 'country': info['country'], 'city': info['city'],
                                 'birth_date': info['birth_date'], 'sex': info['sex']})
