import multiprocessing
from datetime import datetime
from multiprocessing import Barrier, Lock, Process
from time import time


def test_with_barrier(sync: Barrier, serial: Lock):
    name = multiprocessing.current_process().name
    sync.wait()
    now = time()
    with serial:
        print(f"proses {name} ----> {datetime.fromtimestamp(now)}")


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print(f"proses {name} ----> {datetime.fromtimestamp(now)}")


if __name__ == '__main__':
    syncer = Barrier(2)
    serialler = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(syncer, serialler)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(syncer, serialler)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
