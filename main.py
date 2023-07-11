from dotenv import load_dotenv
import os
import requests
import selectorlib

load_dotenv()

URL = os.getenv('TOURS_URL')


def get_page(url: str) -> str:
    response = requests.get(url)

    return response.text


def extract_tours (source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yml")
    return extractor.extract(source)["tours"]


def notify(message):
    print(f"You Have a Tour!!! \n {message}")


def store(tour: str):
    with open("data.txt", "a") as file:
        file.write(tour + "\n")


def is_tour_stored(tour: str) -> bool:
    with open("data.txt", 'r') as file:
        tour_list = file.read()
    return tour in tour_list


if __name__ == "__main__":
    page = get_page(URL)
    tours = extract_tours(page)

    if tours == 'No upcoming tours':
        exit('')

    if not is_tour_stored(tours):
        notify(tours)
        store(tours)

