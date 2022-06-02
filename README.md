# Sistem-Absensi-Mahasiswa-Menggunakan-Face-Recognition
Sistem absensi berbasis pengenalan wajah, tujuan pembuatan adalah untuk menciptakan sistem absensi yang terkomputerisasi dan mengikuti zaman digital saat ini, serta untuk menggantikan sistem absensi manual yang masih sering dipakai.

Langkah dalam menggunakan sistem ini bagi peneliti selanjutnya yang tertarik bukan hanya membuat tapi juga melakukan inovasi yang lebih baik lagi terhadap sistem ini:

## 1. Jalankan file Create_Database.py

File ini berisikan perintah untuk membuat database absensi per kelas di suatu kampus. Pada penelitian ini kami menggunakan sqlite3, data yang dimuat dalam database antara lain:
- Nama absensi disesuaikan dengan nama kelas yang akan dibuatkan tabel absensi
- Berisikan tabel-tabel absensi per mata pelajaran yang diajar pada kelas itu
- Pada setiap tabel dimintakan informasi terkait kelas, no pengenal mahasiswa (NPM), nama mahasiswa, tanda kehadiran, tanggal, dan waktu dilakukannya absensi.

Note*: Diharapkan peneliti selanjutnya bisa membuatkan database langsung pada aplikasi pengolahan database secara langsung, kemudian mengkoneksikannya pada file .py yang ada di sistem ini. Karena peneliti saat ini pun merasa file Create_Database.py ini cukup membuang-buang waktu sehingga terbilang kurang efektif dan efisien.

![Screenshot 2022-06-03 020119](https://user-images.githubusercontent.com/73339446/171714167-2fd68809-99fe-4f8f-9a23-f9f22a377e6a.png)

## Jalankan file Dataset.py

Untuk mengisikan data mahasiswa yang ada didalam kelas maka lakukanlah dengan menjalankan file ini. Diawali dengan mengkoneksikan database kelas yang dituju, lalu isikan 3 data mahasiswa. Data yang perlu diisikan di tahap ini hanyalah:
- Nama mahasiswa
- No pengenal mahasiswa (NPM)
- Kelas

Kemudian secara otomatis sistem akan menambahkan 3 data diatas ke tiap tabel absensi mata pelajaran kelas mereka.

Note*:
1. Bila peneliti selanjutnya ingin menambahkan data wajah secara manual karena menggunakan contoh data wajah random dari social media atau google gambar, maka catatannya adalah PASTIKAN NAMA FOLDER SESUAI NAMA PEMILIK DATA WAJAH DAN SESUAIKAN NAMA ITU JUGA DENGAN NAMA YANG TERCANTUM PADA DATABASE. Ini penting karena sistem akan melakukan identifikasi berdasarkan nama folder dan mencocokkannya juga dengan nama yang tersimpan di database.
2. Bila peneliti selanjutnya ingin mengambil data wajah langsung melalui webcam, pada file Dataset.py ini sudah tersedia kodingan untuk pengambilan data wajah tersebut. Silahkan langsung dihapuskan saja tanda komentar atau # yang terdapat pada kodingan, kemudian barulah menjalankan file Dataset.py. Nantinya setelah mengisikan data diri yang diminta untuk kebutuhan database, sistem akan secara otomatis membuka webcam komputer untuk pengambilan data wajah.

## Jalankan preprocess.py

Gunakan file ini melakukan proses awal terhadap data wajah.

Note*: Sayangnya kodingan disini sangat amat kurang memadai, karena kodingan ini mampu melakukan preprocess tetapi tidak mampu menyimpan hasil preprocess yang telah dilakukan, sehingga data preprocess seperti tidak ada gunanya.

Bagi peneliti selanjutnya diharapkan mampu membenarkan file ini agar mampu digunakan, karena preprocess sangat penting bagi akurasi data nantinya.

## Jalankan file train_data.py

Bila semua data sudah siap dan sudah melewati preprocess juga terhadap data wajah, maka langkah pemrosesan terakhir pada data adalah training data. Pada langkah ini sistem akan mulai melakukan pengenalan terhadap data wajah dan identitas yang dimilikinya. Pada penelitian ini kami menggunakan MTCNN dari pustaka facenet_pytorch dan pretrained 'vggface2'.

## Jalankan file recogabsen.py

Inilah saat yang ditunggu-tunggu, yaitu melakukan absensi menggunakan sistem yang telah kita buat!!!

# Interface 

Kami sudah membuat interface yang bisa diakses dengan menjalankan file interface_mahasiswa.py!

Selamat mencoba dan berinovasi para peneliti selanjutnya, kami harap ini bukan hanya mampu membantu kalian tetapi juga mampu memberikan kalian ide bagaimana cara berinovasi terhadap produk ini.

Kami ucapkan terimakasih sebesar-besarnya juga terhadap para peneliti sebelumnya yang begitu hebat yang bukan hanya mampu membantu kami membuat aplikasi ini tetapi juga mampu menginspirasi kami, sehingga terciptalah aplikasi ini!


#God bless you, aamiin 

#from Vista Sasmita Padmanagara
