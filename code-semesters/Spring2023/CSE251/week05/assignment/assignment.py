"""
Course: CSE 251
Lesson Week: 05
File: assignment.py
Author: <Joshua Ludwig>

Purpose: Assignment 05 - Factories and Dealers

Instructions:

- Read the comments in the following code.  
- Implement your code where the TODO comments are found.
- No global variables, all data must be passed to the objects.
- Only the included/imported packages are allowed.  
- Thread/process pools are not allowed
- You MUST use a barrier
- Do not use try...except statements
- You are not allowed to use the normal Python Queue object.  You must use Queue251.
- the shared queue between the threads that are used to hold the Car objects
  can not be greater than MAX_QUEUE_SIZE

"""

from datetime import datetime
import time
import threading
import random

# Include cse 251 common Python files
from cse251 import *

# Global Consts
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

# NO GLOBAL VARIABLES!

class Car:
    """This is the Car class that will be created by the factories"""

    # Class Variables
    car_makes = ('Ford', 'Chevrolet', 'Dodge', 'Fiat', 'Volvo', 'Infiniti', 'Jeep', 'Subaru',
                 'Buick', 'Volkswagen', 'Chrysler', 'Smart', 'Nissan', 'Toyota', 'Lexus',
                 'Mitsubishi', 'Mazda', 'Hyundai', 'Kia', 'Acura', 'Honda')

    car_models = ('A1', 'M1', 'XOX', 'XL', 'XLS', 'XLE', 'Super', 'Tall', 'Flat', 'Middle', 'Round',
                  'A2', 'M1X', 'SE', 'SXE', 'MM', 'Charger', 'Grand', 'Viper', 'F150', 'Town', 'Ranger',
                  'G35', 'Titan', 'M5', 'GX', 'Sport', 'RX')

    car_years = list(range(1990, datetime.now().year))

    def __init__(self):
        # Make a random car
        self.model = random.choice(Car.car_models)
        self.make = random.choice(Car.car_makes)
        self.year = random.choice(Car.car_years)

        # Sleep a little. Last statement in this for loop - don't change
        time.sleep(random.random() / SLEEP_REDUCE_FACTOR)

        # Display the car that has been just created in the terminal
        self.display()

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251:
    """This is the queue object to use for this assignment. Do not modify!!"""

    def __init__(self):
        self.items = []
        self.max_size = 0

    def get_max_size(self):
        return self.max_size

    def put(self, item):
        self.items.append(item)
        if len(self.items) > self.max_size:
            self.max_size = len(self.items)

    def get(self):
        return self.items.pop(0)


class Factory(threading.Thread):
    """This is a factory. It will create cars and place them on the car queue"""

    def __init__(self, car_queue, number_of_cars_empty_semaphore, number_of_cars_semaphore,
                 barrier, factory_number, dealer_count, factory_stats):
        super().__init__()
        self.car_queue = car_queue
        self.number_of_cars_empty_semaphore = number_of_cars_empty_semaphore
        self.number_of_cars_semaphore = number_of_cars_semaphore
        self.barrier = barrier
        self.factory_number = factory_number
        self.dealer_count = dealer_count
        self.factory_stats = factory_stats
        self.cars_to_produce = random.randint(200, 300)  # Don't change

    def run(self):
        for _ in range(self.cars_to_produce):
            car = Car()
            self.car_queue.put(car)
            self.number_of_cars_semaphore.release()
            self.number_of_cars_empty_semaphore.acquire()

            self.factory_stats[self.factory_number] += 1

        self.barrier.wait()

        if self.factory_number == 0:
            for _ in range(self.dealer_count):
                self.car_queue.put("No more cars")
                self.number_of_cars_semaphore.release()
                self.number_of_cars_empty_semaphore.acquire()


class Dealer(threading.Thread):
    """This is a dealer that receives cars"""

    def __init__(self, car_queue, number_of_cars_empty_semaphore, number_of_cars_semaphore,
                 dealer_stats, dealer_number):
        super().__init__()
        self.car_queue = car_queue
        self.number_of_cars_empty_semaphore = number_of_cars_empty_semaphore
        self.number_of_cars_semaphore = number_of_cars_semaphore
        self.dealer_stats = dealer_stats
        self.dealer_number = dealer_number

    def run(self):
        while True:
            self.number_of_cars_empty_semaphore.release()
            self.number_of_cars_semaphore.acquire()

            msg = self.car_queue.get()

            if msg == "No more cars":
                return

            self.dealer_stats[self.dealer_number] += 1

            # Sleep a little - don't change. This is the last line of the loop
            time.sleep(random.random() / SLEEP_REDUCE_FACTOR)


def run_production(factory_count, dealer_count):
    """This function will do a production run with the number of
    factories and dealerships passed in as arguments.
    """

    number_of_cars_semaphore = threading.Semaphore(0)
    number_of_cars_empty_semaphore = threading.Semaphore(MAX_QUEUE_SIZE)

    car_queue = Queue251()

    barrier = threading.Barrier(factory_count)

    dealer_stats = [0] * dealer_count
    factory_stats = [0] * factory_count

    factories = [
        Factory(car_queue, number_of_cars_empty_semaphore, number_of_cars_semaphore, barrier,
                factory_number, dealer_count, factory_stats) for factory_number in range(factory_count)
    ]

    dealerships = [
        Dealer(car_queue, number_of_cars_empty_semaphore, number_of_cars_semaphore,
               dealer_stats, dealer_number) for dealer_number in range(dealer_count)
    ]

    log.start_timer()

    for dealer in dealerships:
        dealer.start()

    for factory in factories:
        factory.start()

    for factory in factories:
        factory.join()

    for dealer in dealerships:
        dealer.join()

    run_time = log.stop_timer(f'{sum(dealer_stats)} cars have been created')

    return run_time, car_queue.get_max_size(), dealer_stats, factory_stats


def main(log):
    """Main function - DO NOT CHANGE!"""

    runs = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 5), (5, 2), (10, 10)]

    for factories, dealerships in runs:
        run_time, max_queue_size, dealer_stats, factory_stats = run_production(factories, dealerships)

        log.write(f'Factories      : {factories}')
        log.write(f'Dealerships    : {dealerships}')
        log.write(f'Run Time       : {run_time:.4f}')
        log.write(f'Max queue size : {max_queue_size}')
        log.write(f'Factory Stats  : {factory_stats}')
        log.write(f'Dealer Stats   : {dealer_stats}')
        log.write('')

        # The number of cars produced needs to match the cars sold
        assert sum(dealer_stats) == sum(factory_stats)


if __name__ == '__main__':
    log = Log(show_terminal=True)
    main(log)

