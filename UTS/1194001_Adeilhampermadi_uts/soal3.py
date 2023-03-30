from mpi4py import MPI
import time

def book_ticket(passenger_name, ticket_id, departure_date, destination):
    # Simulasi proses pemesanan tiket bus
    print(f"Proses pemesanan tiket dengan ID {ticket_id} oleh {passenger_name} dimulai...")
    # Proses pemesanan tiket berlangsung selama 2 detik
    time.sleep(2)
    print(f"Proses pemesanan tiket dengan ID {ticket_id} oleh {passenger_name} selesai.")
    print(f"Kode booking untuk tiket dengan ID {ticket_id}: {ticket_id[:4]}-{ticket_id[4:]}")
    print(f"Tiket untuk {passenger_name} pada tanggal {departure_date} ke {destination} telah berhasil dipesan.")

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        passenger_name = 'John'
        ticket_id = 'B001'
        departure_date = '2023-04-01'
        destination = 'Jakarta'
        destination_process = 1
        comm.send((passenger_name, ticket_id, departure_date, destination), dest=destination_process)
        print("Sending data", (passenger_name, ticket_id, departure_date, destination), "to process", destination_process)

    if rank == 1:
        passenger_name, ticket_id, departure_date, destination = comm.recv(source=0)
        book_ticket(passenger_name, ticket_id, departure_date, destination)

    if rank == 2:
        passenger_name = 'Jane'
        ticket_id = 'B002'
        departure_date = '2023-04-02'
        destination = 'Surabaya'
        destination_process = 3
        comm.send((passenger_name, ticket_id, departure_date, destination), dest=destination_process)
        print("Sending data", (passenger_name, ticket_id, departure_date, destination), "to process", destination_process)

    if rank == 3:
        passenger_name, ticket_id, departure_date, destination = comm.recv(source=2)
        book_ticket(passenger_name, ticket_id, departure_date, destination)
