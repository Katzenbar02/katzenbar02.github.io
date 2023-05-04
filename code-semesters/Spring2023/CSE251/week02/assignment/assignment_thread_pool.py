from datetime import datetime, timedelta
import requests
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


class APICall:
    def __init__(self, url):
        self.url = url
        self.result = None
        self.call_count = 0

    def run(self):
        response = requests.get(self.url)
        self.result = json.loads(response.content.decode())
        self.call_count += 1


def retrieve_results(details, log, section):
    results = sorted(details[section])
    log.write(f'{section.capitalize()}: {len(results)}')

    with ThreadPoolExecutor() as executor:
        result_futures = [executor.submit(APICall(url).run) for url in results]

    results_list = [result['name'] for result in result_futures]
    results_str = ', '.join(sorted(results_list))
    log.write(results_str)
    log.write_blank_line()


def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')
    log.write('-----------------------------------------')

    # Retrieve Top API urls
    top_api_call = APICall(TOP_API_URL)
    top_api_call.run()
    top_api_urls = top_api_call.result

    # Retrieve Details on film 6
    film_url = top_api_urls['films'] + '6/'
    film_call = APICall(film_url)
    film_call.run()
    film_details = film_call.result

    log.write(f'Title   : {film_details["title"]}')
    log.write(f'Director: {film_details["director"]}')
    log.write(f'Producer: {film_details["producer"]}')
    log.write(f'Released: {film_details["release_date"]}')
    log.write_blank_line()

    retrieve_results(film_details, log, 'characters')
    retrieve_results(film_details, log, 'planets')


if __name__ == '__min__':
    main()