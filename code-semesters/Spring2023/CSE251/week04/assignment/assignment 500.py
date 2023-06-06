import time
import threading
import random
from datetime import datetime
from cse251 import *

# Global Consts - Do not change
CARS_TO_PRODUCE = 500
MAX_QUEUE_SIZE = 10
SLEEP_REDUCE_FACTOR = 50

class Car:
    """ This is the Car class that will be created by the factories """

    car_makes = ('Ford', 'Chevrolet', 'Dodge', 'Fiat', 'Volvo', 'Infiniti', 'Jeep', 'Subaru', 
                'Buick', 'Volkswagen', 'Chrysler', 'Smart', 'Nissan', 'Toyota', 'Lexus', 
                'Mitsubishi', 'Mazda', 'Hyundai', 'Kia', 'Acura', 'Honda')

    car_models = ('A1', 'M1', 'XOX', 'XL', 'XLS', 'XLE' ,'Super' ,'Tall' ,'Flat', 'Middle', 'Round',
                'A2', 'M1X', 'SE', 'SXE', 'MM', 'Charger', 'Grand', 'Viper', 'F150', 'Town', 'Ranger',
                'G35', 'Titan', 'M5', 'GX', 'Sport', 'RX')

    car_years = [i for i in range(1990, datetime.now().year)]

    def __init__(self):
        self.model = random.choice(Car.car_models)
        self.make = random.choice(Car.car_makes)
        self.year = random.choice(Car.car_years)

        time.sleep(random.random() / SLEEP_REDUCE_FACTOR)

    def display(self):
        print(f'{self.make} {self.model}, {self.year}')


class Queue251:
    """ This is the que object to use for this assignment. Do not modify!! """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, item):
        assert len(self.items) <= MAX_QUEUE_SIZE
        self.items.append(item)

    def get(self):
        return self.items.pop(0)


class Factory(threading.Thread):
    """ This is a factory. It will create cars and place them on the car que """

    def __init__(self, que, number_cars_empty_semaphore, number_of_cars_semaphore):
        super().__init__()
        self.que = que
        self.number_cars_empty_semaphore = number_cars_empty_semaphore
        self.number_of_cars_semaphore = number_of_cars_semaphore

    def run(self):
        for i in range(CARS_TO_PRODUCE):
            car = Car()
            self.que.put(car)
            self.number_of_cars_semaphore.release()
            self.number_cars_empty_semaphore.acquire()

        self.que.put("No more lamo")
        self.number_of_cars_semaphore.release()
        self.number_cars_empty_semaphore.acquire()


class Dealer(threading.Thread):
    """ This is a dealer that receives cars """

    def __init__(self, que, number_cars_empty_semaphore, number_of_cars_semaphore, queue_stats):
        super().__init__()
        self.que = que
        self.number_cars_empty_semaphore = number_cars_empty_semaphore
        self.number_of_cars_semaphore = number_of_cars_semaphore
        self.que.stats = queue_stats

    def run(self):
        while True:
            self.number_cars_empty_semaphore.release()
            self.number_of_cars_semaphore.acquire()

            msg = self.que.get()

            if msg == "No more lamo":
                return
            
            self.queue_stats[self.que.size()] += 1

            time.sleep(random.random() / SLEEP_REDUCE_FACTOR)




def main():
    log = Log(show_terminal=True)
    que = Queue251()
    number_of_cars_semaphore = threading.Semaphore(0)
    number_cars_empty_semaphore = threading.Semaphore(10)


    queue_stats = [0] * MAX_QUEUE_SIZE

    factory = Factory(que, number_cars_empty_semaphore, number_of_cars_semaphore)
    dealer = Dealer(que, number_cars_empty_semaphore,number_of_cars_semaphore, queue_stats)

    log.start_timer()

    factory.start()
    dealer.start()

    factory.join()
    dealer.join()

    log.stop_timer(f'All {CARS_TO_PRODUCE} cars have been created')

    for i in range(MAX_QUEUE_SIZE):
        queue_stats[i] = que.size()
        time.sleep(random.random() / SLEEP_REDUCE_FACTOR)

    xaxis = [i for i in range(1, MAX_QUEUE_SIZE + 1)]
    plot = Plots()
    plot.bar(xaxis, queue_stats, title=f'{CARS_TO_PRODUCE} Produced: Count VS Queue Size', x_label='Queue Size', y_label='Count')




if __name__ == '__main__':
    main()
