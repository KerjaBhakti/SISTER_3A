import logging
import threading
import time

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

items = []
condition = threading.Condition()


class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:
            while len(items) == 0:
                logging.info('Tidak ada barang untuk dikonsumsi. Menunggu...')
                condition.wait()

            items.pop()
            logging.info('Barang dikonsumsi.')
            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(2)
            self.consume()


class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:
            while len(items) == 10:
                logging.info('Jumlah barang sudah mencapai batas. Menunggu...')
                condition.wait()

            items.append(1)
            logging.info('Barang diproduksi. Total barang: {}'.format(len(items)))
            condition.notify()

    def run(self):
        for i in range(20):
            time.sleep(0.5)
            self.produce()


def main():
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()


if __name__ == "__main__":
    main()
