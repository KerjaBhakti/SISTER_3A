import multiprocessing
from time import ctime

class barang(multiprocessing.Process):

    def run(self):
        print ('%s Barang masuk pada  %s' %(self.name, ctime()))
        return

if __name__ == '__main__':
    for i in range(10):
        process = barang()
        process.start()
        process.join()
