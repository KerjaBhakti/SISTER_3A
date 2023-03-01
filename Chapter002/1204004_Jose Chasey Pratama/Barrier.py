from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

runners = ['Jose', 'Haryadi', 'Hanan', 'Kucing']
num_runners = len(runners)
finish_line = Barrier(num_runners)

def runner():
    sleep(randrange(2, 5))
    print(f'{runners.pop()} sampai finish line pada waktu: {ctime()} \n')
    finish_line.wait()

def main():
    threads = []
    print('Mulaiiiiiii')
    for i in range(num_runners):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Aright Selesai yakkkk')

if __name__ == "__main__":
    main()
