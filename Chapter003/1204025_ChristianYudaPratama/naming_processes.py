import multiprocessing

def worker():
    name = multiprocessing.current_process().name
    print(f"Process {name} is running")

if __name__ == '__main__':
    num_processes = 4
    for i in range(num_processes):
        process_name = f"Process-{i}"
        process = multiprocessing.Process(target=worker, name=process_name)
        process.start()