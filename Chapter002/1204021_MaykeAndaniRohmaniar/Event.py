import threading
import time
import random

class Employee(threading.Thread):
    def __init__(self, name, event):
        threading.Thread.__init__(self)
        self.name = name
        self.event = event

    def run(self):
        while True:
            self.event.wait()
            print(f"{self.name} sedang bekerja")
            time.sleep(random.randint(1,5))
            print(f"{self.name} menunggu perintah")
            self.event.clear()

class Company():
    def __init__(self, num_of_employees):
        self.num_of_employees = num_of_employees
        self.event = threading.Event()

    def start(self):
        employees = []
        for i in range(self.num_of_employees):
            employee = Employee(f"Karyawan-{i+1}", self.event)
            employees.append(employee)

        for employee in employees:
            employee.start()

        for i in range(3):
            time.sleep(random.randint(1,5))
            print("Situasi darurat terjadi")
            self.event.set()

            time.sleep(random.randint(1,5))
            self.event.clear()

        for employee in employees:
            employee.join()

def main():
    num_of_employees = 5
    company = Company(num_of_employees)
    company.start()

if __name__ == "__main__":
    main()
