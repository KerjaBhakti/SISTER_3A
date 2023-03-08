import multiprocessing
import time


def foo():
    print('Memulai prosess....')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('prosess selesai.....')


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print(f'apakah prosess {p} aktif ? {p.is_alive()}\n')
    p.start()
    print(f'prosess aktif: {p.is_alive()}')
    p.terminate()
    print(f'prosess mati : {not p.is_alive()}')
    p.join()
    print('exit code dari process : ', p.exitcode)
