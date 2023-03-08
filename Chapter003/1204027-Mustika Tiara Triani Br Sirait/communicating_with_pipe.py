##Using Pipes with multiprocessing – Chapter 3: Process Based Parallelism

import multiprocessing 

def system(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("Send the message: {}".format(msg))  
    conn.close()   
 
def new_user(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))
 
if __name__== '__main__':

    msgs = ["ERROR!", "Username belum terdaftar", "END"]
    
    pipe_1, pipe_2 = multiprocessing.Pipe()
    
    p1 = multiprocessing.Process(target=system, args=(pipe_1,msgs))
    p2 = multiprocessing.Process(target=new_user, args=(pipe_2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()