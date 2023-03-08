import multiprocessing as mp


def pow_2(data: int):
    result = data * data
    return result


if __name__ == '__main__':
    list_integer = list(range(0, 100))
    pool = mp.Pool(processes=10)
    pool_outputs = pool.map(pow_2, list_integer)

    pool.close()
    pool.join()
    print('Pool    :', pool_outputs)
