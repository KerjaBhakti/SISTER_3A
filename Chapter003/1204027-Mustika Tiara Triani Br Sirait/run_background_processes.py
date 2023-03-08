import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name

    if name == 'background_process':
        print ("Response data for client : %s \n" %name)
        for i in range(0,5):
            print('---> %d \n' %i)
        time.sleep(1)
    else:
        print ("Response data for client : %s \n" %name)
        for i in range(5,10):
            print('---> %d \n' %i)
        time.sleep(1)
    print ("Exiting %s \n" %name)
        
if __name__ == '__main__':
    background_process = multiprocessing.Process\
                         (name='background_process',\
                          target=foo)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process\
                            (name='NO_background_process',\
                             target=foo)
    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    

