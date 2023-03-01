from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 4
finish_line = Barrier(num_runners)
runners = ['Haryadi', 'Yuda', 'Jose','surahmi']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s Sampai pada barrier pada waktu: %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('BALAPAN DIMULAi!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Balapan Selesai!')

if __name__ == "__main__":
    main()
