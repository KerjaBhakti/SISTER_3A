import multiprocessing
import time

def foo():
    print ('Memulai Pekerjaan')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(2)
    print ('Selesai Pekerjaan')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Procses sebelum dimulai:', p, p.is_alive())
    p.start()
    print ('Proses sedang berjalan:', p, p.is_alive())
    p.terminate()
    print ('Proses dihentikan:', p, p.is_alive())
    p.join()
    print ('Process joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)