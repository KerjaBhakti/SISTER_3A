import multiprocessing

def worker(process_id):
    print(f"Process {process_id} is running")

if __name__ == '__main__':
    num_processes = 4
    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()