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

![Picture2_absen](https://user-images.githubusercontent.com/73339446/171724820-55e90330-a8b5-475d-b971-0df0fc0602a9.png)

Note*:
1. Bila peneliti selanjutnya ingin menambahkan data wajah secara manual karena menggunakan contoh data wajah random dari social media atau google gambar, maka catatannya adalah PASTIKAN NAMA FOLDER SESUAI NAMA PEMILIK DATA WAJAH DAN SESUAIKAN NAMA ITU JUGA DENGAN NAMA YANG TERCANTUM PADA DATABASE. Ini penting karena sistem akan melakukan identifikasi berdasarkan nama folder dan mencocokkannya juga dengan nama yang tersimpan di database.
2. Bila peneliti selanjutnya ingin mengambil data wajah langsung melalui webcam, pada file Dataset.py ini sudah tersedia kodingan untuk pengambilan data wajah tersebut. Silahkan langsung dihapuskan saja tanda komentar atau # yang terdapat pada kodingan, kemudian barulah menjalankan file Dataset.py. Nantinya setelah mengisikan data diri yang diminta untuk kebutuhan database, sistem akan secara otomatis membuka webcam komputer untuk pengambilan data wajah.

## Jalankan preprocess.py

Gunakan file ini melakukan proses awal terhadap data wajah.

Note*: Sayangnya kodingan disini sangat amat kurang memadai, karena kodingan ini mampu melakukan preprocess tetapi tidak mampu menyimpan hasil preprocess yang telah dilakukan, sehingga data preprocess seperti tidak ada gunanya.

Bagi peneliti selanjutnya diharapkan mampu membenarkan file ini agar mampu digunakan, karena preprocess sangat penting bagi akurasi data nantinya.

## Jalankan file train_data.py

Bila semua data sudah siap dan data wajah sudah melewati preprocess, maka langkah pemrosesan terakhir pada data adalah training data. Pada langkah ini sistem akan mulai melakukan pengenalan terhadap data wajah dan identitas yang dimilikinya. Pada penelitian ini kami menggunakan MTCNN dari pustaka facenet_pytorch dan pretrained 'vggface2'.

Hasil training data ini menghasilkan: data.pt

## Jalankan file recogabsen.py

Inilah saat yang ditunggu-tunggu, yaitu melakukan absensi menggunakan sistem yang telah kita buat!!! Sistem akan mengenali wajah yang ada dihadapannya, setelah berhasil dikenali sistem akan secara otomatis memasukkan datanya kedalam tabel absensi yang dituju saat itu. Akan ada 3 data tambahan yang terupdate setelah tahap ini, yaitu:
- Tanda kehadiran
- Tanggal
- Waktu dilakukannya absensi

# Interface 

Kami sudah membuat interface yang bisa diakses dengan menjalankan file interface_mahasiswa.py!

![Picture1](https://user-images.githubusercontent.com/73339446/171724289-4a7b5c6a-0f72-411a-89f5-9a8bebaa05e5.png)
![Picture2](https://user-images.githubusercontent.com/73339446/171724306-4520dfa5-1723-40fe-8d7a-e749640237d6.png)
![Picture3](https://user-images.githubusercontent.com/73339446/171724315-0231b154-e574-4481-a168-ecee2a0b0673.png)
![Picture4](https://user-images.githubusercontent.com/73339446/171724329-8484846c-d407-4ea6-9cbb-947f2edf5d98.png)
![Picture5](https://user-images.githubusercontent.com/73339446/171724337-c3c3fd11-10c6-44cb-848b-a010fe32043a.png)

#### Absensi
![Picture6](https://user-images.githubusercontent.com/73339446/171724349-3ead873c-b827-4d24-afab-b2ff6ad217c2.png)

#### Hasil Absensi
![Picture1_absen](https://user-images.githubusercontent.com/73339446/171724687-d6d6de98-761b-4343-b0d4-262dcb90f825.png)


Selamat mencoba dan berinovasi para peneliti selanjutnya, kami harap ini bukan hanya membantu kalian dalam pembuatan aplikasi tetapi juga memberikan kalian ide bagaimana inovasi terbaik yang bisa dibuat untuk selanjutnya.

Kami ucapkan terimakasih sebesar-besarnya juga terhadap para peneliti sebelumnya yang begitu hebat yang membantu kami dalam pembuatan aplikasi ini dan juga telah menginspirasi kami, sehingga terciptalah aplikasi ini!

#
#### God bless you,


#### from: Vista Sasmita Padmanagara
