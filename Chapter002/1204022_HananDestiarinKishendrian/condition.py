import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class pengunjung1(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pengunjung(self):

        with condition:

            if len(items) == 0:
                logging.info('Nomor antrean penuh!')
                condition.wait()

            items.pop()
            logging.info('Mendapat nomor antrean')

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(2)
            self.pengunjung()


class pengelola1(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pengelola(self):

        with condition:

            if len(items) == 7:
                logging.info('antrean tersisa {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total antrean {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(10):
            time.sleep(0.5)
            self.pengelola()


def main():
    pengelola = pengelola1(name='Pengelola')
    pengunjung = pengunjung1(name='Pengunjung')

    pengelola.start()
    pengunjung.start()

    pengelola.join()
    pengunjung.join()


if __name__ == "__main__":
    main()
