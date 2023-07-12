from Event import Event
from Notificator import Notificator
from Storage import Storage
import time
from dotenv import load_dotenv
import os


load_dotenv()
tours_url = os.getenv('TOURS_URL')
event = Event()
storage = Storage('scraper-app10.db')
notificator = Notificator()

if __name__ == "__main__":
    while True:
        page = event.get_page(tours_url)
        tours = event.extract_tour(page)

        if 'No upcoming tours' in tours:
            time.sleep(2)
            continue

        tours = event.preprocess_data(tours)
        if tours and not storage.is_tour_stored(tours):
            notificator.notify(str(tours))
            result = storage.store(tours)

        time.sleep(2)
