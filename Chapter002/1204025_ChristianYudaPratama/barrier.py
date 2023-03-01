from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

runners = ['Yuda', 'Jose', 'Haryadi', 'Hanan']
num_runners = len(runners)
finish_line = Barrier(num_runners)

def runner():
    sleep(randrange(2, 5))
    print(f'{runners.pop()} selesai mengerjakan tantangan praktek di waktu: {ctime()} \n')
    finish_line.wait()

def main():
    threads = []
    print('siapp.. mulaiii....')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('baik tantangan praktek selesai')

if __name__ == "__main__":
    main()
