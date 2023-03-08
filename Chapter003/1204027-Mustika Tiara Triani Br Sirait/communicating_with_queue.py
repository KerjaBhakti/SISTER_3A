import multiprocessing
import random
import time

class supplier(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(5):
            item = random.randint(0, 100)
            self.queue.put(item) 
            print ("Process supplier : Stok Barang %d ditambahkan %s"\
                   % (item,self.name))
            time.sleep(1)
            print ("Sisa stok barang adalah %s"\
                   % self.queue.qsize())
       
class user(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            if (self.queue.empty()):
                print("Stok Barang Kosong")
                break
            else :
                time.sleep(2)
                item = self.queue.get()
                print ('Process user: barang %d terjual \
                        oleh %s \n'\
                       % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_supplier = supplier(queue)
        process_user = user(queue)
        process_supplier.start()
        process_user.start()
        process_supplier.join()
        process_user.join()


        
        
         
