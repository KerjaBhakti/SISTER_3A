import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def nasabah():
    logging.info('Harap Menunggu')
    semaphore.acquire()
    logging.info('Nasabah: antrian nomer {}'.format(item))


def admin():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Teller: antrian nomer {}'.format(item))
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=nasabah)
        t2 = threading.Thread(target=admin)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
