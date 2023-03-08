import multiprocessing

class Employee(multiprocessing.Process):

    def __init__(self, emp_id, emp_name, emp_salary):
        super(Employee, self).__init__()
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display_employee(self):
        print("Pegawai ID: %s\nPegawai Nama: %s\nPegawai Salary: %s\n" %(self.emp_id, self.emp_name, self.emp_salary))

    def run(self):
        print("Memulai Proses Pegawai %s" % self.emp_name)
        self.display_employee()
        print("Selesai Proses Pegawai %s" % self.emp_name)

if __name__ == '__main__':
    emp1 = Employee("E101", "Yuda", 87000)
    emp2 = Employee("E102", "Christian", 6000)

    emp1.start()
    emp2.start()

    emp1.join()
    emp2.join()

    print("Semua Proses Selesai!")