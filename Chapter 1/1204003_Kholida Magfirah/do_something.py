import random

#function do_something dengan dua parameter count dan out_list
#funtion do_something digunakan untuk membuat kalkulasi sederhana termasuk membuat list integer yang dipilih random
def do_something(count,out_list): 
	for i in range(count):
		out_list.append(random.random())

