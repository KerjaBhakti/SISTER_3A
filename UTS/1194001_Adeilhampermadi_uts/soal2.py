import multiprocessing
import time

def book_ticket(customer):
    print(f"Customer {customer} memesan tiket")
    time.sleep(1) # simulasi pemesanan tiket
    print(f"Customer {customer} telah memesan tiket")

if __name__ == '__main__':
    # Daftar customer yang ingin memesan tiket
    customers = ['John', 'Jane', 'Tom', 'Anna', 'David']

    # Membuat proses multiprocessing untuk setiap customer
    processes = []
    for customer in customers:
        p = multiprocessing.Process(target=book_ticket, args=(customer,))
        processes.append(p)

    # Memulai semua proses secara paralel
    for p in processes:
        p.start()

    # Menunggu semua proses selesai
    for p in processes:
        p.join()

    print("Semua customer telah memesan tiket")
