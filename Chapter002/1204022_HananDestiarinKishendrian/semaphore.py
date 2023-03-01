import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


semaphore = threading.Semaphore(0)
item = 0


def mahasiswa():
    logging.info('Menunggu Komputer')
    semaphore.acquire()
    logging.info('Pemberitahuan Mahasiswa: komputer nomor {}'.format(item))


def dosen():
    global item
    time.sleep(3)
    item = random.randint(0, 1000)
    logging.info('Pemberitahuan Dosen: mengawas komputer nomor {}'.format(item))
    semaphore.release()


def main():
    for i in range(10):
        t1 = threading.Thread(target=mahasiswa)
        t2 = threading.Thread(target=dosen)

        t1.start()
        t2.start()

        t1.join()
        t2.join()


if __name__ == "__main__":
    main()
