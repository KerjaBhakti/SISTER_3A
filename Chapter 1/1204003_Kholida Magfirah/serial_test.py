import time
from do_something import *

#implementasi dari penggunaan function dosometing 
if __name__ == "__main__":
    start_time = time.time()
    size = 1200000   #variabel size dimana ukurannya 10jt
    n_exec = 11   #jumlah eksekusi berapa kali
    for i in range(0, n_exec):    #looping,jadi setiap ada nilai di range didalam kurung sampai 10, sehingga proses diulang 10x
        out_list = list()  #variabel outlist dan class list
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
