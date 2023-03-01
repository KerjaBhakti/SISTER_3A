import multiprocessing
import time

from do_something import do_something

if __name__ == "__main__":
    start_time = time.perf_counter()
    size = 100000000
    procs = 3
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process(
            target=do_something,
            args=(size, out_list)
        )
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.perf_counter()
    print("multiprocesses time = ", end_time - start_time)
