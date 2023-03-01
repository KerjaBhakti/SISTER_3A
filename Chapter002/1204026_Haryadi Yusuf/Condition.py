import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Pembeli(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def membeli(self):

        with condition:

            if len(items) == 0:
                logging.info('tidak ada barang yang dibeli')
                condition.wait()

            items.pop()
            logging.info('membeli 1 barang')

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.membeli()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def menjual(self):

        with condition:

            if len(items) == 10:
                logging.info('barang diproduksi {}. Stopped'.format(len(items)))
                condition.wait()

            items.append(1)
            logging.info('total barang {}'.format(len(items)))

            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.menjual()


def main():
    producer = Penjual(name='Penjual')
    consumer = Pembeli(name='Pembeli')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
