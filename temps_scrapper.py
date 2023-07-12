import datetime
import sqlite3
import time

from dotenv import load_dotenv
import os
import selectorlib
import requests

load_dotenv()

TEMPS_URL = os.getenv('TEMPERATURES_URL')
connection = sqlite3.connect('scraper-app10.db')
cursor = connection.cursor()


def get_page(url: str) -> str:
    response = requests.get(url)

    return response.text


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    return extractor.extract(source)["temps"]


def store(temp_data):
    current_date = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    cursor.execute("Insert into temps VALUES(Null, ?, ?)", (current_date, temp_data))
    return connection.commit()


if __name__ == "__main__":
    counter = 0
    while True:
        page = get_page(TEMPS_URL)
        temps = extract(page)

        if temps:
            store(temps)

        counter +=1

        if counter == 10:
            break
        time.sleep(2)

