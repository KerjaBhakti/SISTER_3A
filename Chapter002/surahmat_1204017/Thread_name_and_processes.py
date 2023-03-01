from threading import Thread
import time
import os

class MyThreadClass (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name
 
   def run(self):
       if self.name == "Nuklir.vsc ":
           for i in range(5):
               print("ID of process running {}".format(self.name)+"PID "+ str(os.getpid()))
               time.sleep(1)
       if self.name == "Tuhan.exe ":
           for i in range(3):
               print("ID of process running {}".format(self.name)+"PID "+ str(os.getpid()+ 3))
               time.sleep(1)

def main():
    # Thread Creation
    thread1 = MyThreadClass("Nuklir.vsc ")
    thread2 = MyThreadClass("Tuhan.exe ")
  
    # Thread Running
    thread1.start()
    thread2.start()

    # Thread joining
    thread1.join()
    thread2.join()

    # End 
    print("End")


if __name__ == "__main__":
    main()
