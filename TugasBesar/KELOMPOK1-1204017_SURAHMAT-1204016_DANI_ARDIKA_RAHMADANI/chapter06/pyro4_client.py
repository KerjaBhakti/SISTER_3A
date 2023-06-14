import Pyro4

# Membuat proxy ke objek server
gserver = Pyro4.Proxy(input("masukan id object: "))

# Input data pengiriman barang
pengirim = input("Masukkan nama pengirim: ")
penerima = input("Masukkan nama penerima: ")
barang = input("Masukkan nama barang: ")

# Mengirim data pengiriman barang ke server
gserver.process_shipping(pengirim, penerima, barang)
