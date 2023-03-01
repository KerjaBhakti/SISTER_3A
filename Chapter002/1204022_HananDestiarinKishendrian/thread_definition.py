import threading
from time import ctime

def my_func(thread_number):
    return print('Thread definition N°{} \n selesai pada {}'.format(thread_number, ctime()))


def main():
    threads = []
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))
        threads.append(t)
        t.start()
        t.join()

if __name__ == "__main__":
    main()