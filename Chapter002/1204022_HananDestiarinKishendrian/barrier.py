from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_mhs = 5
finish_line = Barrier(num_mhs)
mhs = ['Budi', 'Dewi', 'Mawar', 'Bambang', 'Bunga']

def runner():
    name = mhs.pop()
    sleep(randrange(2, 5))
    print('%s memulai quiz pada : %s \n' % (name, ctime()))
    finish_line.wait()

def main():
    threads = []
    print('QIUZ DIMULAI!!!!')
    for i in range(num_mhs):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('SELESAI!')

if __name__ == "__main__":
    main()