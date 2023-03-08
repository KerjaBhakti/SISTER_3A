# import multiprocessing

# class MyProcess(multiprocessing.Process):

#     def run(self):
#         print ('called run method in %s' %self.name)
#         return

# if __name__ == '__main__':
#     for i in range(10):
#         process = MyProcess()
#         process.start()
#         process.join()


#Try
from multiprocessing import Process

class Supplier(Process):
    
    def return_name(self):
        print("Barang masuk dari %s" % self.name)
        return 
    def run(self):
        return self.return_name()
    
if __name__ == "__main__":
    
        for i in range(5):
                p = Supplier()
                p.start()
                p.join()