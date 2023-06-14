from chapter_1.do_something import do_something
import time
import threading

def send_item(item):
    print("Barang", item, "sedang dikirim")
    time.sleep(1)

if __name__ == "__main__":
    start_time = time.time()
    num_items = 100
    threads = 5
    jobs = []

    for i in range(0, num_items):
        thread = threading.Thread(target=send_item, args=(i,))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("Pengiriman barang selesai.")
    end_time = time.time()
    print("Waktu multithreading=", end_time - start_time)
