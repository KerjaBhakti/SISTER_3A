import multiprocessing
import time

def book_ticket(passenger_name, ticket_id, departure_date, destination):
    # Simulasi proses pemesanan tiket bus
    print(f"Proses pemesanan tiket dengan ID {ticket_id} oleh {passenger_name} dimulai...")
    # Proses pemesanan tiket berlangsung selama 2 detik
    time.sleep(2)
    print(f"Proses pemesanan tiket dengan ID {ticket_id} oleh {passenger_name} selesai.")
    print(f"Tiket untuk {passenger_name} pada tanggal {departure_date} ke {destination} telah berhasil dipesan.")

def process_1():
    passenger_name = 'John'
    ticket_id = 'T001'
    departure_date = '2023-04-01'
    destination = 'Jakarta'
    book_ticket(passenger_name, ticket_id, departure_date, destination)

def process_2():
    passenger_name = 'Jane'
    ticket_id = 'T002'
    departure_date = '2023-04-02'
    destination = 'Surabaya'
    book_ticket(passenger_name, ticket_id, departure_date, destination)

if __name__ == '__main__':
    # Membuat proses anak menggunakan multiprocessing.Process()
    p1 = multiprocessing.Process(target=process_1)
    p2 = multiprocessing.Process(target=process_2)

    # Menjalankan proses anak menggunakan metode .start()
    p1.start()
    p2.start()

    # Menunggu proses anak selesai menggunakan metode .join()
    p1.join()
    p2.join()

    print("Semua proses pemesanan tiket bus selesai.")
