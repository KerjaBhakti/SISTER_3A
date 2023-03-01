import threading
import time
import random


class Room:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def luar(self):
        with self.lock:
            self.execute(1)

    def dalam(self):
        with self.lock:
            self.execute(-1)


def keluar(room, items):
    print("Nasabah Selesai Transaksi terdapat {} orang \n".format(items))
    while items:
        room.dalam()
        time.sleep(1)
        items -= 1
        print("Nasabah Selesai Transaksi -->{} orang SELESAI \n".format(items))


def masuk(room, items):
    print("Nasabah Akan Melakukan Transaksi terdapat {} orang \n".format(items))
    while items:
        room.luar()
        time.sleep(1)
        items -= 1
        print("Nasabah Memulai Transaksi -->{} orang MULAI \n".format(items))


def main():
    items = 10
    room = Room()

    t1 = threading.Thread(target=keluar,
                          args=(room, random.randint(10, 20)))
    t2 = threading.Thread(target=masuk,
                          args=(room, random.randint(1, 10)))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
