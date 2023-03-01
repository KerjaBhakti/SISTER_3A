import threading
import time
import random

class Cook(threading.Thread):
    def __init__(self, name, barrier):
        threading.Thread.__init__(self)
        self.name = name
        self.barrier = barrier

    def run(self):
        while True:
            print(f"{self.name} sedang menyiapkan makanan")
            time.sleep(random.randint(1,5))
            print(f"{self.name} selesai menyiapkan makanan")
            self.barrier.wait()

class Waiter(threading.Thread):
    def __init__(self, name, barrier):
        threading.Thread.__init__(self)
        self.name = name
        self.barrier = barrier

    def run(self):
        while True:
            print(f"{self.name} sedang melayani pelanggan")
            time.sleep(random.randint(1,5))
            print(f"{self.name} selesai melayani pelanggan")
            self.barrier.wait()

class Restaurant():
    def __init__(self, num_of_cooks, num_of_waiters):
        self.num_of_cooks = num_of_cooks
        self.num_of_waiters = num_of_waiters
        self.barrier = threading.Barrier(num_of_cooks + num_of_waiters)

    def start(self):
        cooks = []
        waiters = []
        for i in range(self.num_of_cooks):
            cook = Cook(f"Koki-{i+1}", self.barrier)
            cooks.append(cook)

        for i in range(self.num_of_waiters):
            waiter = Waiter(f"Pelayan-{i+1}", self.barrier)
            waiters.append(waiter)

        for cook in cooks:
            cook.start()

        for waiter in waiters:
            waiter.start()

        for i in range(3):
            print("Pelanggan datang")
            time.sleep(random.randint(1,5))
            print("Pesanan diterima")

            time.sleep(2)
            self.barrier.wait()
            print("Pesanan selesai")

        for cook in cooks:
            cook.join()

        for waiter in waiters:
            waiter.join()

def main():
    num_of_cooks = 3
    num_of_waiters = 5
    restaurant = Restaurant(num_of_cooks, num_of_waiters)
    restaurant.start()

if __name__ == "__main__":
    main()