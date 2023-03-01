import threading
import time
import random

class Customer(threading.Thread):
    def __init__(self, name, restaurant):
        threading.Thread.__init__(self)
        self.name = name
        self.restaurant = restaurant

    def run(self):
        print(f"{self.name} ingin makan di restoran")
        self.restaurant.take_seat()
        print(f"{self.name} duduk di meja {self.restaurant.current_table}")
        time.sleep(random.randint(1,5))
        self.restaurant.leave_seat()
        print(f"{self.name} meninggalkan restoran")

class Restaurant():
    def __init__(self, num_of_tables):
        self.num_of_tables = num_of_tables
        self.tables = [i for i in range(1, num_of_tables+1)]
        self.current_table = None
        self.condition = threading.Condition()

    def take_seat(self):
        self.condition.acquire()
        while not self.tables:
            self.condition.wait()
        self.current_table = self.tables.pop()
        self.condition.release()

    def leave_seat(self):
        self.condition.acquire()
        self.tables.append(self.current_table)
        self.current_table = None
        self.condition.notify()
        self.condition.release()

def main():
    num_of_customers = 10
    num_of_tables = 5
    restaurant = Restaurant(num_of_tables)
    customers = []
    for i in range(num_of_customers):
        customer = Customer("Pelanggan-" + str(i+1), restaurant)
        customers.append(customer)

    for customer in customers:
        customer.start()

    for customer in customers:
        customer.join()

if __name__ == "__main__":
    main()