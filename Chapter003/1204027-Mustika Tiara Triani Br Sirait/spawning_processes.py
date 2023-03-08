#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

# def myFunc(i):
#     print ('calling myFunc from process n°: %s' %i)
#     for j in range (0,i):
#         print('output from myFunc is :%s' %j)
#     return

# if __name__ == '__main__':
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i,))
#         process.start()
#         process.join()

from multiprocessing import Process

def stok(n):
    print ('Tambah Barang : ', n)
    for j in range (0,n):
        print('Stok Barang adalah : ', j+1)
    return

def barang_masuk(n):
    print("Jumlah Barang Masuk adalah : ", n)
    
if __name__=="__main__":
    for n in range(6):
        p1=Process(target=stok, args=(n,))
        p2=Process(target=barang_masuk, args=(n,))
        
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("We're done")