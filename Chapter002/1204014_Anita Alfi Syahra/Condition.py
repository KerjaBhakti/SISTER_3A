import threading
import time
import random

class Employee(threading.Thread):
    def __init__(self, name, condition):
        threading.Thread.__init__(self)
        self.name = name
        self.condition = condition

    def run(self):
        while True:
            print(f"{self.name} sedang mengajar")
            time.sleep(random.randint(1,5))
            with self.condition:
                self.condition.wait()
            print(f"{self.name} respon dosen kepada mahasiswa")


class Company():
    def __init__(self, num_of_employees):
        self.num_of_employees = num_of_employees
        self.condition = threading.Condition()

    def start(self):
        employees = []
        for i in range(self.num_of_employees):
            employee = Employee(f"Dosen-{i+1}", self.condition)
            employees.append(employee)

        for employee in employees:
            employee.start()

        for i in range(3):
            time.sleep(random.randint(1,5))
            print("Respon dosen kepada mahasiswa")
            with self.condition:
                self.condition.notify_all()

            time.sleep(random.randint(1,5))
            with self.condition:
                self.condition.notify_all()

        for employee in employees:
            employee.join()

def main():
    num_of_employees = 5
    company = Company(num_of_employees)
    company.start()

if __name__ == "__main__":
    main()