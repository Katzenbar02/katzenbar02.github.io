import threading
import time

class Display_hello(threading.Thread):

    def __init__(self,number):

        threading.Thread.__init__(self)

        self.number = number
    
    def run(self):
        time.sleep(self.number)
        print(f'Hello World: {self.number}')

if __name__ == '__main__':
    hello1 = Display_hello(2)
    hello2 = Display_hello(1)

    hello1.start()
    hello2.start()

    hello1.join()
    hello2.join()