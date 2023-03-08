##Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing as mp


def buat_items(len_item: int, pipe: mp.Pipe):
    output_pipe, _ = pipe
    for item in range(len_item):
        print('output pipe send dari create_items : ' + str(item))
        output_pipe.send(item)
    output_pipe.close()


def multiply_items(pipe_1: mp.Pipe, pipe_2: mp.Pipe):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            print('output pipe send dari multiply_items : ' + str(item * item))
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()


if __name__ == '__main__':
    # First process pipe with numbers from 0 to 9
    pipe_1 = mp.Pipe(True)
    process_pipe_1 = mp.Process(target=buat_items, args=(10, pipe_1,))
    process_pipe_1.start()

    # second pipe,
    pipe_2 = mp.Pipe(True)
    process_pipe_2 = mp.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:
            print(pipe_2[1].recv())
    except EOFError:
        print("End")
