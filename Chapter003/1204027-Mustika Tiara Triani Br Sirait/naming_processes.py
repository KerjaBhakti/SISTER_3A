import multiprocessing
import time

def user():
    name = multiprocessing.current_process().name  #mengubah nama prosesnya
    print (name, 'Starting')
    time.sleep(2)
    print (name, 'Exiting')

def my_app():
    name = multiprocessing.current_process().name
    print (name, 'Starting')
    time.sleep(3)
    print (name, 'Exiting')
    
if __name__ == '__main__':
    service = multiprocessing.Process(name='my_app', target=my_app)
    user_1 = multiprocessing.Process(name='user', target=user)
    user_2 = multiprocessing.Process(target=user)  #use default name

    user_1.start()
    user_2.start()
    service.start()

    user_1.join()
    user_2.join()
    service.join()

    print("We're done")