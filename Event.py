import requests
import selectorlib
import datetime

class Event:
    def get_page(self, url: str) -> str:
        response = requests.get(url)

        return response.text

    def extract_tour(self, source: str) -> list:
        extractor = selectorlib.Extractor.from_yaml_file("extract.yml")

        return extractor.extract(source)["tours"].split(',')

    def preprocess_data(self, data):
        date = datetime.datetime.strptime(data.pop(), '%d.%m.%Y')
        date = date.strftime('%Y.%m.%d')
        data.append(date)

        return [row.strip() for row in data]