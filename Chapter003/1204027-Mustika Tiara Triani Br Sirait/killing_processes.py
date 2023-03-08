import multiprocessing
import time

def user():
    print ('Starting Registration Prosess')
    for i in range(0,10):
        print('-->%d\n' %i)
        time.sleep(1)
    print ('Finished Registration')

if __name__ == '__main__':
    p = multiprocessing.Process(target=user)
    print ('Process before Registration:', p, p.is_alive())
    p.start()
    print ('Process running:', p, p.is_alive())
    p.terminate()
    print ('Process terminated:', p, p.is_alive())
    p.join()
    print ('Process joined:', p, p.is_alive())
    print ('Process exit code:', p.exitcode)
