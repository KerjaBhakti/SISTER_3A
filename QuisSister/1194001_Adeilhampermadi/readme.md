mport beberapa modul seperti random, threading, dan time.
Membuat daftar runners yang berisi nama-nama mahasiswa yang belum membayar uang kuliah.
Membuat sebuah Barrier dengan ukuran sebanyak jumlah mahasiswa yang belum membayar uang kuliah.
Mendefinisikan fungsi runner yang akan dijalankan pada masing-masing thread. Fungsi ini akan memilih nama mahasiswa dari runners secara acak, kemudian menunggu selama beberapa detik (2-5 detik) untuk mensimulasikan pembayaran tagihan. Setelah itu, fungsi ini akan mencetak pesan bahwa mahasiswa tersebut belum membayar tagihan pada saat tertentu, kemudian menunggu di Barrier. Setelah semua thread mencapai Barrier, fungsi ini akan menunggu lagi selama beberapa detik (2-5 detik), kemudian mencetak pesan bahwa mahasiswa tersebut telah membayar tagihan pada saat tertentu.
Membuat thread untuk setiap mahasiswa yang belum membayar uang kuliah, kemudian menjalankan thread-thread tersebut. Setelah semua thread selesai dijalankan, program mencetak pesan yang menunjukkan waktu yang diperlukan untuk menjalankan program tersebut.
Dalam program di atas, menggunakan Barrier untuk memastikan bahwa semua thread menunggu sampai semua thread mencapai Barrier sebelum melanjutkan eksekusi selanjutnya. Barrier adalah objek sinkronisasi yang dapat digunakan untuk menunda thread-thread tertentu sampai semua thread mencapai Barrier. Dalam contoh di atas, Barrier akan memastikan bahwa setiap thread menunggu sampai thread-thread lain menyelesaikan pembayaran sebelum melanjutkan untuk mencetak pesan bahwa mereka telah membayar tagihan.

Kode program di atas adalah contoh implementasi multithreading yang sederhana, tetapi dapat memberikan gambaran tentang cara menggunakan threading untuk menjalankan beberapa thread secara simultan dalam sebuah program Pytho

![image](https://user-images.githubusercontent.com/61839170/226373284-66447d1f-a8d1-4d74-9075-ec6e75249fcf.png)
