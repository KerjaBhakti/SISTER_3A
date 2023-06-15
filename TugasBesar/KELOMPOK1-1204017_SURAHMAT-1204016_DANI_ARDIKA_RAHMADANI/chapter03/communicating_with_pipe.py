import multiprocessing
import time


def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        print('Barang', item, 'dibuat')
        time.sleep(1)
        output_pipe.send(item)
    output_pipe.close()


def process_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            print('Barang', item, 'sedang diproses')
            time.sleep(2)
            output_pipe.send(item)
    except EOFError:
        output_pipe.close()


def deliver_items(pipe):
    input_pipe, _ = pipe
    try:
        while True:
            item = input_pipe.recv()
            print('Barang', item, 'sedang dikirim')
            time.sleep(1)
    except EOFError:
        print('Semua barang telah dikirim')


if __name__ == '__main__':
    # Pipe pertama untuk membuat barang
    pipe_1 = multiprocessing.Pipe(True)
    process_create_items = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_create_items.start()

    # Pipe kedua untuk memproses barang
    pipe_2 = multiprocessing.Pipe(True)
    process_process_items = multiprocessing.Process(target=process_items, args=(pipe_1, pipe_2,))
    process_process_items.start()

    # Pipe ketiga untuk pengiriman barang
    pipe_3 = multiprocessing.Pipe(True)
    process_deliver_items = multiprocessing.Process(target=deliver_items, args=(pipe_3,))
    process_deliver_items.start()

    pipe_1[0].close()
    pipe_2[0].close()
    pipe_3[1].close()

    try:
        while True:
            item = pipe_2[1].recv()
            print('Barang', item, 'siap untuk dikirim')
            pipe_3[0].send(item)
    except EOFError:
        print("Proses pengiriman selesai")
