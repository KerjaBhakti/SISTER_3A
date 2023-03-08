#Using a Process Pool – Chapter 3: Process Based Parallelism
import multiprocessing
from time import ctime, sleep
from random import random

def function_square(data):
    result = data*data
    return result

barang1 = 'Piring'
barang2 = 'Sendok'
barang3 = 'Garpu'
if __name__ == '__main__':
    inputs1 = list(range(8,9))
    inputs2 = list(range(10,11))
    inputs3 = list(range(20,21))
    
    pool = multiprocessing.Pool(processes=4)
    pool_outputs1 = pool.map(function_square, inputs1)
    pool_outputs2 = pool.map(function_square, inputs2)
    pool_outputs3 = pool.map(function_square, inputs3)
    
    produksi1 = barang1
    produksi2 = barang2
    produksi3 = barang3
    
    value = random() * 10
    sleep(value)
    
    print (f'Penempatan Nomor Produksi: \n Nama Produk: %s \n Nomor Produksi: %s \n Waktu : {value} \n Tanggal: %s \n' % (produksi1, pool_outputs1, ctime()))
    print (f'Penempatan Nomor Produksi: \n Nama Produk: %s \n Nomor Produksi: %s \n Waktu : {value} \n Tanggal: %s \n' % (produksi2, pool_outputs2, ctime()))
    print (f'Penempatan Nomor Produksi: \n Nama Produk: %s \n Nomor Produksi: %s \n Waktu : {value} \n Tanggal: %s \n' % (produksi3, pool_outputs3, ctime()))
    
    pool.close() 
    pool.join()  
