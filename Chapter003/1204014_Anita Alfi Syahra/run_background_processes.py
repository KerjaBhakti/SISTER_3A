import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Memulai %s \n" %name)
    if name == 'proses berjalan':
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(3)
    else:
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("keluar dari %s \n" %name)
    

if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='proses yang berjalan',\
                          target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='proses yang tidak berjalan',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()