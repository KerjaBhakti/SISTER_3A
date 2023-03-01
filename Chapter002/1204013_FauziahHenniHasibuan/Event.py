import threading
import time
import random

class Cook(threading.Thread):
    def __init__(self, name, restaurant, event):
        threading.Thread.__init__(self)
        self.name = name
        self.restaurant = restaurant
        self.event = event

    def run(self):
        print(f"{self.name} siap memasak")
        while True:
            self.event.wait()
            print(f"{self.name} memulai memasak")
            time.sleep(random.randint(1,5))
            print(f"{self.name} selesai memasak")
            self.event.clear()

class Restaurant():
    def __init__(self, num_of_tables, num_of_cooks):
        self.num_of_tables = num_of_tables
        self.num_of_cooks = num_of_cooks
        self.tables = [i for i in range(1, num_of_tables+1)]
        self.current_table = None
        self.event = threading.Event()

    def order_food(self):
        print("Pelanggan memesan makanan")
        self.event.set()

    def serve_food(self):
        print("Makanan siap disajikan")

def main():
    num_of_cooks = 3
    num_of_tables = 5
    restaurant = Restaurant(num_of_tables, num_of_cooks)
    cooks = []
    for i in range(num_of_cooks):
        cook = Cook("Koki-" + str(i+1), restaurant, restaurant.event)
        cooks.append(cook)

    for cook in cooks:
        cook.start()

    for i in range(5):
        restaurant.order_food()
        time.sleep(2)

    for cook in cooks:
        cook.join()

    restaurant.serve_food()

if __name__ == "__main__":
    main()