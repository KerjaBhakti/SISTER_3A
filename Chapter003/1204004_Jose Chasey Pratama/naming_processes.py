import multiprocessing
import time


def fungsi_nama():
    name = multiprocessing.current_process().name
    print(f"memulai proses = {name} \n")
    time.sleep(3)
    print(f"mengakhiri prosess = {name} \n")


if __name__ == '__main__':
    proses_nama = multiprocessing.Process(name='MARKIBUT', target=fungsi_nama)

    proses_tanpa_nama = multiprocessing.Process(target=fungsi_nama)

    proses_nama.start()
    proses_tanpa_nama.start()

    proses_nama.join()
    proses_tanpa_nama.join()
