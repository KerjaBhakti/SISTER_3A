import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = random.randint(0, 1000)


def consumer():
    logging.info('menunggu data')
    semaphore.acquire()
    logging.info(f'mengambil data nomor {item}')


def producer():
    global item
    time.sleep(2)
    item = random.randint(0, 1000)
    logging.info(f'membuat data nomor {item}')
    semaphore.release()


def main():
    steps = 3
    for i in range(steps):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
