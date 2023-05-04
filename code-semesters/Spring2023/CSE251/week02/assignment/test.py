import json
import threading
import requests
from datetime import datetime, timedelta
from cse251 import Log

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'
call_count = 0

class APICallThread(threading.Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.result = None

    def run(self):
        global call_count
        response = requests.get(self.url)
        self.result = json.loads(response.content.decode())
        call_count += 1

def retrieve_results(details, log, section):
    results = sorted(details[section])
    log.write(f'{section.capitalize()}: {len(results)}')

    result_threads = []
    for url in results:
        result_thread = APICallThread(url)
        result_thread.start()
        result_threads.append(result_thread)

    results_str = ''
    for result_thread in result_threads:
        result_thread.join()
        result_details = result_thread.result
        results_str += str(result_details['name']) + ', '

    results_str = ', '.join(sorted(results_str.split(', ')))
    log.write(results_str[:-2])
    log.write_blank_line()

def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')
    log.write('-----------------------------------------')

    # Retrieve Top API urls
    top_api_thread = APICallThread(TOP_API_URL)
    top_api_thread.start()
    top_api_thread.join()
    top_api_urls = top_api_thread.result

    # Retrieve Details on film 6
    film_url = top_api_urls['films'] + '6/'
    film_thread = APICallThread(film_url)
    film_thread.start()
    film_thread.join()
    film_details = film_thread.result

    log.write(f'Title   : {film_details["title"]}')
    log.write(f'Director: {film_details["director"]}')
    log.write(f'Producer: {film_details["producer"]}')
    log.write(f'Released: {film_details["release_date"]}')
    log.write_blank_line()

    retrieve_results(film_details, log, 'characters')
    retrieve_results(film_details, log, 'planets')
    retrieve_results(film_details, log, 'starships')
    retrieve_results(film_details, log, 'vehicles')
    retrieve_results(film_details, log, 'species')

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')

if __name__ == "__main__":
    main()
