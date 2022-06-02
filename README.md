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

