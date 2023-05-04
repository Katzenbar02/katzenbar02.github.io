import threading

class Add_Two(threading.Thread):

    def __init(self, number, name=''):
        super().__init__()
        self.number = number

    def run(self):
        self.results = self.number + 2

if __name__ == '__main__':
    add1 = Add_Two(100)
    add2 = Add_Two(200, 'Bob')

    add1.start()
    add2.start()

    add1.join()
    add2.join()

    print(f'Add_Two(100) returns {add1.results}')
    print(f'Add_Two(200) returns {add2.results}')