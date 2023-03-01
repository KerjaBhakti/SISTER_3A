import threading
import time

class Employee(threading.Thread):
    def __init__(self, name, barrier):
        threading.Thread.__init__(self)
        self.name = name
        self.barrier = barrier

    def run(self):
        print(f"{self.name} mulai bekerja")
        time.sleep(3)
        print(f"{self.name} telah menyelesaikan tugasnya")
        self.barrier.wait()
        print(f"{self.name} selesai!")

def main():
    num_of_employees = 4
    barrier = threading.Barrier(num_of_employees)
    employees = []
    for i in range(num_of_employees):
        employee = Employee("Karyawan-" + str(i+1), barrier)
        employees.append(employee)

    for employee in employees:
        employee.start()

    for employee in employees:
        employee.join()

    print("Laporan bulanan telah selesai dibuat")

if __name__ == "__main__":
    main()