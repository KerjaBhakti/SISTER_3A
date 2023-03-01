import random


def do_something(count: int, out_list: list) -> None:
    for i in range(count):
        out_list.append(random.random())
