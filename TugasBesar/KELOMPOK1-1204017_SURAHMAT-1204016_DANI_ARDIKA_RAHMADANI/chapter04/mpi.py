from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Inisialisasi data pengiriman barang
if rank == 0:
    pengirim = "Pengirim Utama"
    barang = ["Barang 1", "Barang 2", "Barang 3", "Barang 4"]
else:
    pengirim = None
    barang = None

# Broadcast data pengiriman barang ke semua proses
pengirim = comm.bcast(pengirim, root=0)
barang = comm.bcast(barang, root=0)

# Penerimaan barang oleh proses dengan rank 6
if rank == 6:
    barang_diterima = random.choice(barang)
else:
    barang_diterima = None

# Kumpulkan informasi penerimaan barang dari semua proses
data_penerimaan_barang = comm.gather(barang_diterima, root=6)

# Tampilkan informasi penerimaan barang dari proses dengan rank 6
if rank == 6:
    print("Informasi Penerimaan Barang:")
    for i in range(size):
        print(f"Proses {i}: Barang diterima = {data_penerimaan_barang[i]}")
