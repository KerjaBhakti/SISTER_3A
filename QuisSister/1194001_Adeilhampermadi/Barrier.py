from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep
import time


runners = ['ultaraman', 'ultramen strom', 'kamenrider']
start_time = time.time()
jumlah = Barrier(len(runners))

def runner():
    name = runners.pop()
    sleep(randrange(2, 5))
    print('%s tagihan uang kuliah belum dibayar, terakir pada : %s \n' % (name, ctime()))
    jumlah.wait()
    sleep(randrange(2, 5))
    print('%s telah di bayar pada tanggal : %s \n' % (name, ctime()))

def main():
   
    threads = []
    print('list tagihan mahasiswa yang belum membayar spp')
    for i in range(len(runners)):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print("hasil telah di result dalam waktu --- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
