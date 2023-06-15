import random

def do_something(count, out_queue):
    for i in range(count):
        item = random.random()
        out_queue.put(item)

if __name__ == "__main__":
    from queue import Queue
    import time
    import threading

    start_time = time.time()
    num_items = 100
    threads = 5
    out_queue = Queue()

    jobs = []
    for _ in range(threads):
        thread = threading.Thread(target=do_something, args=(num_items // threads, out_queue))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    while not out_queue.empty():
        item = out_queue.get()
        print("Barang", item, "diterima dan siap untuk dikirim")

    print("Pengiriman barang selesai.")
    end_time = time.time()
    print("Waktu multithreading =", end_time - start_time)
