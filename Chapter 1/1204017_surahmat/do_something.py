import random

def do_something(count,out_list):
	for i in range(count):
		out_list.append(random.random())
	

my_list = []
do_something(2, my_list)
print(my_list) 