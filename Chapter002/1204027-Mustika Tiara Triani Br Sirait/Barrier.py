from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Ara', 'Ida', 'Ulan']

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s Berangkat kuliah pada: %s \n' % (name, ctime()))
    finish_line.wait()
    print('%s Pulang kuliah pada: %s \n' % (name, ctime()))

def main():
    threads = []
    print('Gas kuliah!!!!')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Udah pada balik!')

if __name__ == "__main__":
    main()
