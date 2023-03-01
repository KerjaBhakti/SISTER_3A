condition = modul threading menyediakan kelas kondisi yang dapat digunakan untuk mengoordinasikan utas 
dalam program paralel. Objek kondisi pada dasarnya adalah pembungkus di sekitar objek kunci 
yang memungkinkan satu atau lebih utas untuk menunggu sampai kondisi tertentu dipenuhi, dan kemudian lanjutkan

barier = dalam komputasi paralel mengacu pada mekanisme sinkronisasi yang memungkinkan satu set utas 
untuk menunggu satu sama lain pada titik tertentu dalam eksekusi. 
Penghalang memastikan bahwa semua utas telah mencapai titik sinkronisasi sebelum 
memungkinkan salah satu dari mereka untuk melangkah lebih jauh dalam ekseku

event = Utas produser menghasilkan nomor acak dan menambahkannya ke daftar item. 
Setelah menambahkan item, ia mengatur bendera acara untuk memberi sinyal utas konsumen untuk bangun dan 
mengkonsumsi item.Utas konsumen menunggu bendera acara diatur, 
menunjukkan bahwa ada item baru untuk dikonsumsi.
Kemudian muncul item dari daftar item dan mencatat pesan yang menunjukkan bahwa 
mereka telah mengkonsumsi item tersebut.