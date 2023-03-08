import multiprocessing as mp
import random
import time


class Produser(mp.Process):
    def __init__(self, queue: mp.Queue):
        mp.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f"Prosess Produer : item {item} ditambahkan di antrian {self.name}\n")
            print(f"banyak antrian {self.queue.qsize()}\n")
            time.sleep(1)


class Konsumer(mp.Process):
    def __init__(self, queue: mp.Queue):
        mp.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty\n")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print(f'Process Consumer : item {item} diambil {self.name} \n')
                print(f'sisa antrian {self.queue.qsize()}\n')
                time.sleep(1)


if __name__ == '__main__':
    queue = mp.Queue()
    process_producer = Produser(queue)
    process_consumer = Konsumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
