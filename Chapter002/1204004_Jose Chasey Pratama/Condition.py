import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

steps = 5
sleeptime = 1

items = []
condition = threading.Condition()


class Pembeli(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):

        with condition:

            if len(items) == 0:
                logging.info('tidak ada data yang bisa diambil')
                condition.wait()

            items.pop()
            logging.info(f'mengambil 1 data. sisa data {len(items)}')

            condition.notify()

    def run(self):
        for i in range(steps):
            time.sleep(sleeptime+1)
            self.consume()


class Penjual(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):

        with condition:

            if len(items) == 10:
                logging.info(f'produksi data {len(items)}. Stopped')
                condition.wait()

            logging.info("membuat 1 data.")
            items.append(1)
            logging.info(f'total data {len(items)}')

            condition.notify()

    def run(self):
        for i in range(steps):
            time.sleep(sleeptime)
            self.produce()


def main():
    producer = Penjual(name='Penjual')
    consumer = Pembeli(name='Pembeli')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
