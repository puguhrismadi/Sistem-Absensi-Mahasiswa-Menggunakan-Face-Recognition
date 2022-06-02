import sqlite3
# PSIKOLOGI
# Pembuatan absensi-1pa
conn_1pa = sqlite3.connect("ABSENSI_1PA.db")
c_1pa = conn_1pa.cursor()
sql_mp1_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Faal(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Umum_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Digital_Citizenship(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Pengembangan_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Psikologi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Ilmu_Alamiah_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peng_Apl_Komp_Psi_Informatika_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peng_Apl_Komp_Psi_Informatika_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1pa.executescript(sql_mp1_1pa)
c_1pa.executescript(sql_mp2_1pa)
c_1pa.executescript(sql_mp3_1pa)
c_1pa.executescript(sql_mp4_1pa)
c_1pa.executescript(sql_mp5_1pa)
c_1pa.executescript(sql_mp6_1pa)
c_1pa.executescript(sql_mp7_1pa)
c_1pa.executescript(sql_mp8_1pa)
c_1pa.executescript(sql_mp9_1pa)
c_1pa.executescript(sql_mp10_1pa)
conn_1pa.commit()
conn_1pa.close()
# Pembuatan absensi-2pa
conn_2pa = sqlite3.connect("ABSENSI_2PA.db")
c_2pa = conn_2pa.cursor()
sql_mp1_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Social_Networking_Creative_Cont(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Metodologi_Penelitian_Kuantitatif(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Klinis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Kepribadian_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Sosial_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikodiagnostika_2_Observasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kode_Etik_Psikologi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_Lanjut(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Filsafat_Manusia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2pa.executescript(sql_mp1_2pa)
c_2pa.executescript(sql_mp2_2pa)
c_2pa.executescript(sql_mp3_2pa)
c_2pa.executescript(sql_mp4_2pa)
c_2pa.executescript(sql_mp5_2pa)
c_2pa.executescript(sql_mp6_2pa)
c_2pa.executescript(sql_mp7_2pa)
c_2pa.executescript(sql_mp8_2pa)
c_2pa.executescript(sql_mp9_2pa)
conn_2pa.commit()
conn_2pa.close()
# Pembuatan absensi-3pa
conn_3pa = sqlite3.connect("ABSENSI_3PA.db")
c_3pa = conn_3pa.cursor()
sql_mp1_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Kognitif(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikometri(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ergonomi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengembangan_Kreativitas_Kebe(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Test_Proyektif(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Konseling(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Anak_Khusus(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Lintas_Budaya(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sains_Data_Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3pa.executescript(sql_mp1_3pa)
c_3pa.executescript(sql_mp2_3pa)
c_3pa.executescript(sql_mp3_3pa)
c_3pa.executescript(sql_mp4_3pa)
c_3pa.executescript(sql_mp5_3pa)
c_3pa.executescript(sql_mp6_3pa)
c_3pa.executescript(sql_mp7_3pa)
c_3pa.executescript(sql_mp8_3pa)
c_3pa.executescript(sql_mp9_3pa)
c_3pa.executescript(sql_mp10_3pa)
conn_3pa.commit()
conn_3pa.close()
# Pembuatan absensi-4pa
conn_4pa = sqlite3.connect("ABSENSI_4PA.db")
c_4pa = conn_4pa.cursor()
sql_mp1_4pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Apl_Psi_Kognitif_Sain_dlm_TIK(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konstruksi_Alat_Ukur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4pa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kecerdasan_Artifisial_Masy(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4pa.executescript(sql_mp1_4pa)
c_4pa.executescript(sql_mp2_4pa)
c_4pa.executescript(sql_mp3_4pa)
conn_4pa.commit()
conn_4pa.close()

# SASTRA
# Pembuatan absensi-1sa
conn_1sa = sqlite3.connect("ABSENSI_1SA.db")
c_1sa = conn_1sa.cursor()
sql_mp1_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Digital_Citizenship(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Agama_Islam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kosa_Kata(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Berbicara_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Berbicara_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Membaca_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tata_Bahasa_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1sa.executescript(sql_mp1_1sa)
c_1sa.executescript(sql_mp2_1sa)
c_1sa.executescript(sql_mp3_1sa)
c_1sa.executescript(sql_mp4_1sa)
c_1sa.executescript(sql_mp5_1sa)
c_1sa.executescript(sql_mp6_1sa)
c_1sa.executescript(sql_mp7_1sa)
c_1sa.executescript(sql_mp8_1sa)
c_1sa.executescript(sql_mp9_1sa)
c_1sa.executescript(sql_mp10_1sa)
c_1sa.executescript(sql_mp11_1sa)
c_1sa.executescript(sql_mp12_1sa)
conn_1sa.commit()
conn_1sa.close()
# Pembuatan absensi-2sa
conn_2sa = sqlite3.connect("ABSENSI_2SA.db")
c_2sa = conn_2sa.cursor()
sql_mp1_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Social_Networking_Creative_Cont(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peng_Filsafat_Pemikiran_Modern(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Basic_Acting_Stage_Production(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kosa_Kata_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Berbicara_4A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Berbicara_4B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fonologi_Bahasa_Inggris(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Hubungan_Masyarakat_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penerjemahan_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Reading_Images_Semiotika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tata_Bahasa_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_4A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_4B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp14_2sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menyimak_4C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2sa.executescript(sql_mp1_2sa)
c_2sa.executescript(sql_mp2_2sa)
c_2sa.executescript(sql_mp3_2sa)
c_2sa.executescript(sql_mp4_2sa)
c_2sa.executescript(sql_mp5_2sa)
c_2sa.executescript(sql_mp6_2sa)
c_2sa.executescript(sql_mp7_2sa)
c_2sa.executescript(sql_mp8_2sa)
c_2sa.executescript(sql_mp9_2sa)
c_2sa.executescript(sql_mp10_2sa)
c_2sa.executescript(sql_mp11_2sa)
c_2sa.executescript(sql_mp12_2sa)
c_2sa.executescript(sql_mp13_2sa)
c_2sa.executescript(sql_mp14_2sa)
conn_2sa.commit()
conn_2sa.close()
# Pembuatan absensi-3sa
conn_3sa = sqlite3.connect("ABSENSI_3SA.db")
c_3sa = conn_3sa.cursor()
sql_mp1_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penerjemahan_Berbantuan_Komp(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Jurnalistik2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengkajian_Prosa(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sintaksis_Bahasa_Inggris(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Public_Speaking(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penerjemahan_Audiovisual(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Language_Assessment(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kejurubahasaan_Indonesia_Inggris(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sains_Data_Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3sa.executescript(sql_mp1_3sa)
c_3sa.executescript(sql_mp2_3sa)
c_3sa.executescript(sql_mp3_3sa)
c_3sa.executescript(sql_mp4_3sa)
c_3sa.executescript(sql_mp5_3sa)
c_3sa.executescript(sql_mp6_3sa)
c_3sa.executescript(sql_mp7_3sa)
c_3sa.executescript(sql_mp8_3sa)
c_3sa.executescript(sql_mp9_3sa)
c_3sa.executescript(sql_mp10_3sa)
conn_3sa.commit()
conn_3sa.close()
# Pembuatan absensi-4sa
conn_4sa = sqlite3.connect("ABSENSI_4SA.db")
c_4sa = conn_4sa.cursor()
sql_mp1_4sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Analisis_Wacana(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengajaran_Mikro(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengkajian_Puisi_Inggris(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4sa = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kecerdasan_Artifisial_Masy(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4sa.executescript(sql_mp1_4sa)
c_4sa.executescript(sql_mp2_4sa)
c_4sa.executescript(sql_mp3_4sa)
c_4sa.executescript(sql_mp4_4sa)
conn_4sa.commit()
conn_4sa.close()

# SISTEM INFORMASI
# Pembuatan absensi-1ka
conn_1ka = sqlite3.connect("ABSENSI_1KA.db")
c_1ka = conn_1ka.cursor()
sql_mp1_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ilmu_Budaya_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Dasar_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp14_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Dasar_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp15_1ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Organisasi_Umum_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ka.executescript(sql_mp1_1ka)
c_1ka.executescript(sql_mp2_1ka)
c_1ka.executescript(sql_mp3_1ka)
c_1ka.executescript(sql_mp4_1ka)
c_1ka.executescript(sql_mp5_1ka)
c_1ka.executescript(sql_mp6_1ka)
c_1ka.executescript(sql_mp7_1ka)
c_1ka.executescript(sql_mp8_1ka)
c_1ka.executescript(sql_mp9_1ka)
c_1ka.executescript(sql_mp10_1ka)
c_1ka.executescript(sql_mp11_1ka)
c_1ka.executescript(sql_mp12_1ka)
c_1ka.executescript(sql_mp13_1ka)
c_1ka.executescript(sql_mp14_1ka)
c_1ka.executescript(sql_mp15_1ka)
conn_1ka.commit()
conn_1ka.close()
# Pembuatan absensi-2ka
conn_2ka = sqlite3.connect("ABSENSI_2KA.db")
c_2ka = conn_2ka.cursor()
sql_mp1_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Lanjut_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Sistem_Informasi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Struktur_Organisasi_Data_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Akuntansi_Keuangan_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manaj_Layanan_Sistem_Informasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Operasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_SIM_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_2ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Pemrog_Terstruktur_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ka.executescript(sql_mp1_2ka)
c_2ka.executescript(sql_mp2_2ka)
c_2ka.executescript(sql_mp3_2ka)
c_2ka.executescript(sql_mp4_2ka)
c_2ka.executescript(sql_mp5_2ka)
c_2ka.executescript(sql_mp6_2ka)
c_2ka.executescript(sql_mp7_2ka)
c_2ka.executescript(sql_mp8_2ka)
c_2ka.executescript(sql_mp9_2ka)
c_2ka.executescript(sql_mp10_2ka)
c_2ka.executescript(sql_mp11_2ka)
conn_2ka.commit()
conn_2ka.close()
# Pembuatan absensi-3ka
conn_3ka = sqlite3.connect("ABSENSI_3KA.db")
c_3ka = conn_3ka.cursor()
sql_mp1_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Data_Mining(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Desain_Manaj_Jaringan_Komp(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Anali_Peranc_Sistem_Inf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Penunjang_Keputusan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Animasi_Desain_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Basis_Data_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Teknik_Kompilasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ka.executescript(sql_mp1_3ka)
c_3ka.executescript(sql_mp2_3ka)
c_3ka.executescript(sql_mp3_3ka)
c_3ka.executescript(sql_mp4_3ka)
c_3ka.executescript(sql_mp5_3ka)
c_3ka.executescript(sql_mp6_3ka)
c_3ka.executescript(sql_mp7_3ka)
c_3ka.executescript(sql_mp8_3ka)
c_3ka.executescript(sql_mp9_3ka)
conn_3ka.commit()
conn_3ka.close()
# Pembuatan absensi-4ka
conn_4ka = sqlite3.connect("ABSENSI_4KA.db")
c_4ka = conn_4ka.cursor()
sql_mp1_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Bisnis_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Bisnis_Teknologi_Inf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Informasi_Perbankan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Etika_Profesionalisme_TSI(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Informasi_SDM(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Informasi_Geografis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4ka = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ka.executescript(sql_mp1_4ka)
c_4ka.executescript(sql_mp2_4ka)
c_4ka.executescript(sql_mp3_4ka)
c_4ka.executescript(sql_mp4_4ka)
c_4ka.executescript(sql_mp5_4ka)
c_4ka.executescript(sql_mp6_4ka)
c_4ka.executescript(sql_mp7_4ka)
conn_4ka.commit()
conn_4ka.close()

# SISTEM KOMPUTER
# Pembuatan absensi-1kb
conn_1kb = sqlite3.connect("ABSENSI_1KB.db")
c_1kb = conn_1kb.cursor()
sql_mp1_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Agama_Islam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Dasar_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Dasar_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_dasar_Telekomunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1kb.executescript(sql_mp1_1kb)
c_1kb.executescript(sql_mp2_1kb)
c_1kb.executescript(sql_mp3_1kb)
c_1kb.executescript(sql_mp4_1kb)
c_1kb.executescript(sql_mp5_1kb)
c_1kb.executescript(sql_mp6_1kb)
c_1kb.executescript(sql_mp7_1kb)
c_1kb.executescript(sql_mp8_1kb)
c_1kb.executescript(sql_mp9_1kb)
c_1kb.executescript(sql_mp10_1kb)
c_1kb.executescript(sql_mp11_1kb)
conn_1kb.commit()
conn_1kb.close()
# Pembuatan absensi-2kb
conn_2kb = sqlite3.connect("ABSENSI_2KB.db")
c_2kb = conn_2kb.cursor()
sql_mp1_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_Probabilitas_Terapan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Terdistribusi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengolahan_Sinyal_Digital(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Jaringan_Komputer_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Digital(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Bisnis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Diskrit_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Lanjut_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2kb.executescript(sql_mp1_2kb)
c_2kb.executescript(sql_mp2_2kb)
c_2kb.executescript(sql_mp3_2kb)
c_2kb.executescript(sql_mp4_2kb)
c_2kb.executescript(sql_mp5_2kb)
c_2kb.executescript(sql_mp6_2kb)
c_2kb.executescript(sql_mp7_2kb)
c_2kb.executescript(sql_mp8_2kb)
c_2kb.executescript(sql_mp9_2kb)
conn_2kb.commit()
conn_2kb.close()
# Pembuatan absensi-3kb
conn_3kb = sqlite3.connect("ABSENSI_3KB.db")
c_3kb = conn_3kb.cursor()
sql_mp1_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Proyek_Sistem_Komputer(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Internet_of_Things(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Tertanam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Cerdas_Lanjut(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantarmukaan_Periferal_Komp(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3kb.executescript(sql_mp1_3kb)
c_3kb.executescript(sql_mp2_3kb)
c_3kb.executescript(sql_mp3_3kb)
c_3kb.executescript(sql_mp4_3kb)
c_3kb.executescript(sql_mp5_3kb)
c_3kb.executescript(sql_mp6_3kb)
c_3kb.executescript(sql_mp7_3kb)
c_3kb.executescript(sql_mp8_3kb)
conn_3kb.commit()
conn_3kb.close()
# Pembuatan absensi-4kb
conn_4kb = sqlite3.connect("ABSENSI_4KB.db")
c_4kb = conn_4kb.cursor()
sql_mp1_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Simulasi_Pemodelan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Terdistribusi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kewirausahaan_Teknologi_Informasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Computer_Vision(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Ubiquitas_Computing(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_4kb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Waktu_Nyata(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4kb.executescript(sql_mp1_4kb)
c_4kb.executescript(sql_mp2_4kb)
c_4kb.executescript(sql_mp3_4kb)
c_4kb.executescript(sql_mp4_4kb)
c_4kb.executescript(sql_mp5_4kb)
c_4kb.executescript(sql_mp6_4kb)
c_4kb.executescript(sql_mp7_4kb)
c_4kb.executescript(sql_mp8_4kb)
conn_4kb.commit()
conn_4kb.close()

# TEKNIK INDUSTRI
# Pembuatan absensi-1id
conn_1id = sqlite3.connect("ABSENSI_1ID.db")
c_1id = conn_1id.cursor()
sql_mp1_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekanika_Teknik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Probabilitas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komp_Pemrog_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komp_Pemrog_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Agama_Islam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Dasar_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ilmu_Sosial_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1id.executescript(sql_mp1_1id)
c_1id.executescript(sql_mp2_1id)
c_1id.executescript(sql_mp3_1id)
c_1id.executescript(sql_mp4_1id)
c_1id.executescript(sql_mp5_1id)
c_1id.executescript(sql_mp6_1id)
c_1id.executescript(sql_mp7_1id)
c_1id.executescript(sql_mp8_1id)
c_1id.executescript(sql_mp9_1id)
c_1id.executescript(sql_mp10_1id)
c_1id.executescript(sql_mp11_1id)
conn_1id.commit()
conn_1id.close()
# Pembuatan absensi-2id
conn_2id = sqlite3.connect("ABSENSI_2ID.db")
c_2id = conn_2id.cursor()
sql_mp1_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputer_Industri_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Hukum_Industri(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perencanaan_Perancangan_Produk(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peranc_Sistem_Kerja_Ergonomi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Metode_Stokastik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Proses_Manufaktur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2id.executescript(sql_mp1_2id)
c_2id.executescript(sql_mp2_2id)
c_2id.executescript(sql_mp3_2id)
c_2id.executescript(sql_mp4_2id)
c_2id.executescript(sql_mp5_2id)
c_2id.executescript(sql_mp6_2id)
c_2id.executescript(sql_mp7_2id)
c_2id.executescript(sql_mp8_2id)
conn_2id.commit()
conn_2id.close()
# Pembuatan absensi-3id
conn_3id = sqlite3.connect("ABSENSI_3ID.db")
c_3id = conn_3id.cursor()
sql_mp1_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengen_Penjaminan_Mutu(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ekonomi_Teknik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengetahuan_Lingkungan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Pendukung_Keputusan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peranc_Tata_Letak_Fasilitas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Produksi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3id.executescript(sql_mp1_3id)
c_3id.executescript(sql_mp2_3id)
c_3id.executescript(sql_mp3_3id)
c_3id.executescript(sql_mp4_3id)
c_3id.executescript(sql_mp5_3id)
c_3id.executescript(sql_mp6_3id)
c_3id.executescript(sql_mp7_3id)
c_3id.executescript(sql_mp8_3id)
conn_3id.commit()
conn_3id.close()
# Pembuatan absensi-4id
conn_4id = sqlite3.connect("ABSENSI_4ID.db")
c_4id = conn_4id.cursor()
sql_mp1_4id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perencanaan_Eksperimen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kewirausahaan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kimia_Lanjut(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4id = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4id.executescript(sql_mp1_4id)
c_4id.executescript(sql_mp2_4id)
c_4id.executescript(sql_mp3_4id)
c_4id.executescript(sql_mp4_4id)
conn_4id.commit()
conn_4id.close()

# TEKNIK INFORMATIKA
# Pembuatan absensi-1ia
conn_1ia = sqlite3.connect("ABSENSI_1IA.db")
c_1ia = conn_1ia.cursor()
sql_mp1_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Teknologi_Informasi_C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrograman_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Legal_Aspek_TIK(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Informatika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp14_1ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Dasar_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ia.executescript(sql_mp1_1ia)
c_1ia.executescript(sql_mp2_1ia)
c_1ia.executescript(sql_mp3_1ia)
c_1ia.executescript(sql_mp4_1ia)
c_1ia.executescript(sql_mp5_1ia)
c_1ia.executescript(sql_mp6_1ia)
c_1ia.executescript(sql_mp7_1ia)
c_1ia.executescript(sql_mp8_1ia)
c_1ia.executescript(sql_mp9_1ia)
c_1ia.executescript(sql_mp10_1ia)
c_1ia.executescript(sql_mp11_1ia)
c_1ia.executescript(sql_mp12_1ia)
c_1ia.executescript(sql_mp13_1ia)
c_1ia.executescript(sql_mp14_1ia)
conn_1ia.commit()
conn_1ia.close()
# Pembuatan absensi-2ia
conn_2ia = sqlite3.connect("ABSENSI_2IA.db")
c_2ia = conn_2ia.cursor()
sql_mp1_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Lanjut_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Informatika_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Legal_Aspek_Produk_TIK(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Web_Science(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Informasi_Manajemen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Informatika_Kesehatan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pemrograman_Berbasis_Obyek(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Arsitektur_Komputer(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_2ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Berkas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ia.executescript(sql_mp1_2ia)
c_2ia.executescript(sql_mp2_2ia)
c_2ia.executescript(sql_mp3_2ia)
c_2ia.executescript(sql_mp4_2ia)
c_2ia.executescript(sql_mp5_2ia)
c_2ia.executescript(sql_mp6_2ia)
c_2ia.executescript(sql_mp7_2ia)
c_2ia.executescript(sql_mp8_2ia)
c_2ia.executescript(sql_mp9_2ia)
c_2ia.executescript(sql_mp10_2ia)
c_2ia.executescript(sql_mp11_2ia)
conn_2ia.commit()
conn_2ia.close()
# Pembuatan absensi-3ia
conn_3ia = sqlite3.connect("ABSENSI_3IA.db")
c_3ia = conn_3ia.cursor()
sql_mp1_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Bahasa_dan_Otomata(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Komputasional(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Desain_Pemodelan_Grafik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Grafik_Komputer_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Interaksi_Manusia_dan_Komputer(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Basis_Data_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Keamanan_Komputer(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Game(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_pi_3ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ia.executescript(sql_mp1_3ia)
c_3ia.executescript(sql_mp2_3ia)
c_3ia.executescript(sql_mp3_3ia)
c_3ia.executescript(sql_mp4_3ia)
c_3ia.executescript(sql_mp5_3ia)
c_3ia.executescript(sql_mp6_3ia)
c_3ia.executescript(sql_mp7_3ia)
c_3ia.executescript(sql_mp8_3ia)
c_3ia.executescript(sql_mp9_3ia)
c_3ia.executescript(sql_pi_3ia)
conn_3ia.commit()
conn_3ia.close()
# Pembuatan absensi-4ia
conn_4ia = sqlite3.connect("ABSENSI_4IA.db")
c_4ia = conn_4ia.cursor()
sql_mp1_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Terdistribusi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Multimedia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Konsep_Data_Mining(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Perangkat_Lunak_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Bisnis_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pemrograman_Jaringan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengel_Proyek_Perangkat_Lunak_A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengel_Proyek_Perangkat_Lunak_B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Modern(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pemrograman_Multimedia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_4ia = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Deep_Learning(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ia.executescript(sql_mp1_4ia)
c_4ia.executescript(sql_mp2_4ia)
c_4ia.executescript(sql_mp3_4ia)
c_4ia.executescript(sql_mp4_4ia)
c_4ia.executescript(sql_mp5_4ia)
c_4ia.executescript(sql_mp6_4ia)
c_4ia.executescript(sql_mp7_4ia)
c_4ia.executescript(sql_mp8_4ia)
c_4ia.executescript(sql_mp9_4ia)
c_4ia.executescript(sql_mp10_4ia)
c_4ia.executescript(sql_mp11_4ia)
c_4ia.executescript(sql_mp12_4ia)
conn_4ia.commit()
conn_4ia.close()

# TEKNIK MESIN
conn_1ic = sqlite3.connect("ABSENSI_1IC.db")
c_1ic = conn_1ic.cursor()
sql_mp1_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komputer_Pemrog_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komputer_Pemrog_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_Dasar_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ilmu_Budaya_Dasar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Menggambar_Mesin(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Proses_Produksi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_1ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Ekonomi_Manaj_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ic.executescript(sql_mp1_1ic)
c_1ic.executescript(sql_mp2_1ic)
c_1ic.executescript(sql_mp3_1ic)
c_1ic.executescript(sql_mp4_1ic)
c_1ic.executescript(sql_mp5_1ic)
c_1ic.executescript(sql_mp6_1ic)
c_1ic.executescript(sql_mp7_1ic)
c_1ic.executescript(sql_mp8_1ic)
c_1ic.executescript(sql_mp9_1ic)
c_1ic.executescript(sql_mp10_1ic)
c_1ic.executescript(sql_mp11_1ic)
c_1ic.executescript(sql_mp12_1ic)
c_1ic.executescript(sql_mp13_1ic)
conn_1ic.commit()
conn_1ic.close()
# Pembuatan absensi-2ic
conn_2ic = sqlite3.connect("ABSENSI_2IC.db")
c_2ic = conn_2ic.cursor()
sql_mp1_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Teknik_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tugas_Perencanaan_Elemen_Mesin_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Pembentukan_Material(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elemen_Mesin_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Dasar_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pemilihan_Bahan_Proses(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Kewarganegaraan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekanika_Kekuatan_Material(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_2ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perpindahan_Kalor_Massa(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ic.executescript(sql_mp1_2ic)
c_2ic.executescript(sql_mp2_2ic)
c_2ic.executescript(sql_mp3_2ic)
c_2ic.executescript(sql_mp4_2ic)
c_2ic.executescript(sql_mp5_2ic)
c_2ic.executescript(sql_mp6_2ic)
c_2ic.executescript(sql_mp7_2ic)
c_2ic.executescript(sql_mp8_2ic)
c_2ic.executescript(sql_mp9_2ic)
c_2ic.executescript(sql_mp10_2ic)
c_2ic.executescript(sql_mp11_2ic)
conn_2ic.commit()
conn_2ic.close()
# Pembuatan absensi-3ic
conn_3ic = sqlite3.connect("ABSENSI_3IC.db")
c_3ic = conn_3ic.cursor()
sql_mp1_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistik_Teknik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Energi_Alternatif_Terbarukan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekatronika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kewirausahaan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mesin_Konversi_Energi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tugas_Peranc_Elemen_Mesin_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elemen_Mesin_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputer_Numerical_Control(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ic.executescript(sql_mp1_3ic)
c_3ic.executescript(sql_mp2_3ic)
c_3ic.executescript(sql_mp3_3ic)
c_3ic.executescript(sql_mp4_3ic)
c_3ic.executescript(sql_mp5_3ic)
c_3ic.executescript(sql_mp6_3ic)
c_3ic.executescript(sql_mp7_3ic)
c_3ic.executescript(sql_mp8_3ic)
c_3ic.executescript(sql_mp9_3ic)
c_3ic.executescript(sql_mp10_3ic)
conn_3ic.commit()
conn_3ic.close()
# Pembuatan absensi-4ic
conn_4ic = sqlite3.connect("ABSENSI_4IC.db")
c_4ic = conn_4ic.cursor()
sql_mp1_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Lingkungan_AMDAL(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Etika_Profesi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Audit_Energi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Perawatan_Mesin(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Aerodinamika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4ic = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ic.executescript(sql_mp1_4ic)
c_4ic.executescript(sql_mp2_4ic)
c_4ic.executescript(sql_mp3_4ic)
c_4ic.executescript(sql_mp4_4ic)
c_4ic.executescript(sql_mp5_4ic)
c_4ic.executescript(sql_mp6_4ic)
conn_4ic.commit()
conn_4ic.close()

# TEKNIK ELEKTRO
# Pembuatan absensi-1ib
conn_1ib = sqlite3.connect("ABSENSI_1IB.db")
c_1ib = conn_1ib.cursor()
sql_mp1_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rangkaian_Logika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rangkaian_Elektrik_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komputer_Pemrog_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Komputer_Pemrog_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_Kimia_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rangkaian_Logika_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rangkaian_Elektrik_2R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matemaika_Teknik_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_1ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Telekomunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ib.executescript(sql_mp1_1ib)
c_1ib.executescript(sql_mp2_1ib)
c_1ib.executescript(sql_mp3_1ib)
c_1ib.executescript(sql_mp4_1ib)
c_1ib.executescript(sql_mp5_1ib)
c_1ib.executescript(sql_mp6_1ib)
c_1ib.executescript(sql_mp7_1ib)
c_1ib.executescript(sql_mp8_1ib)
c_1ib.executescript(sql_mp9_1ib)
c_1ib.executescript(sql_mp10_1ib)
c_1ib.executescript(sql_mp11_1ib)
c_1ib.executescript(sql_mp12_1ib)
c_1ib.executescript(sql_mp13_1ib)
conn_1ib.commit()
conn_1ib.close()
# Pembuatan absensi-2ib
conn_2ib = sqlite3.connect("ABSENSI_2IB.db")
c_2ib = conn_2ib.cursor()
sql_mp1_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Tenaga_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Mikroprosesor(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_Probabilitas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kalkulus_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Kewarganegaraan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengukuran_Besaran_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Medan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Konversi_Energi_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ib.executescript(sql_mp1_2ib)
c_2ib.executescript(sql_mp2_2ib)
c_2ib.executescript(sql_mp3_2ib)
c_2ib.executescript(sql_mp4_2ib)
c_2ib.executescript(sql_mp5_2ib)
c_2ib.executescript(sql_mp6_2ib)
c_2ib.executescript(sql_mp7_2ib)
c_2ib.executescript(sql_mp8_2ib)
c_2ib.executescript(sql_mp9_2ib)
c_2ib.executescript(sql_mp10_2ib)
conn_2ib.commit()
conn_2ib.close()
# Pembuatan absensi-3ib
conn_3ib = sqlite3.connect("ABSENSI_3IB.db")
c_3ib = conn_3ib.cursor()
sql_mp1_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Analog(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Radio_Televisi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Alg_Pemrog_Kasus_Tek_Elek(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Pemrosesan_Sinyal(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Telekomunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Daya_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sist_Pembangkit_Tenaga_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Instrumentasi_Elektronika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Tegangan_Arus_Tinggi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Saluran_Transmisi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Daya(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp14_3ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mesin_Elektrik_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ib.executescript(sql_mp1_3ib)
c_3ib.executescript(sql_mp2_3ib)
c_3ib.executescript(sql_mp3_3ib)
c_3ib.executescript(sql_mp4_3ib)
c_3ib.executescript(sql_mp5_3ib)
c_3ib.executescript(sql_mp6_3ib)
c_3ib.executescript(sql_mp7_3ib)
c_3ib.executescript(sql_mp8_3ib)
c_3ib.executescript(sql_mp9_3ib)
c_3ib.executescript(sql_mp10_3ib)
c_3ib.executescript(sql_mp11_3ib)
c_3ib.executescript(sql_mp12_3ib)
c_3ib.executescript(sql_mp13_3ib)
c_3ib.executescript(sql_mp14_3ib)
conn_3ib.commit()
conn_3ib.close()
# Pembuatan absensi-4ib
conn_4ib = sqlite3.connect("ABSENSI_4IB.db")
c_4ib = conn_4ib.cursor()
sql_mp1_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komponen_Elektronika_Industri(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Medis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Elektronika_Optik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Proteksi_Tenaga_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Gelombang_Mikro(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sist_Jaringan_Telekomunikasi_Ljt(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Selular(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Transformator_Tenaga_Elektrik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_4ib = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Otomatisasi_Sist_Elekt(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ib.executescript(sql_mp1_4ib)
c_4ib.executescript(sql_mp2_4ib)
c_4ib.executescript(sql_mp3_4ib)
c_4ib.executescript(sql_mp4_4ib)
c_4ib.executescript(sql_mp5_4ib)
c_4ib.executescript(sql_mp6_4ib)
c_4ib.executescript(sql_mp7_4ib)
c_4ib.executescript(sql_mp8_4ib)
c_4ib.executescript(sql_mp9_4ib)
c_4ib.executescript(sql_mp10_4ib)
conn_4ib.commit()
conn_4ib.close()

# AKUNTANSI
# Pembuatan absensi-1eb
conn_1eb = sqlite3.connect("ABSENSI_1EB.db")
c_1eb = conn_1eb.cursor()
sql_mp1_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Digital_Citizenship(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Ekonomi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sosiologi_Politik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Akuntansi_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Akuntansi_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perekonomian_Indonesia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Ekonomi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1eb.executescript(sql_mp1_1eb)
c_1eb.executescript(sql_mp2_1eb)
c_1eb.executescript(sql_mp3_1eb)
c_1eb.executescript(sql_mp4_1eb)
c_1eb.executescript(sql_mp5_1eb)
c_1eb.executescript(sql_mp6_1eb)
c_1eb.executescript(sql_mp7_1eb)
c_1eb.executescript(sql_mp8_1eb)
c_1eb.executescript(sql_mp9_1eb)
c_1eb.executescript(sql_mp10_1eb)
c_1eb.executescript(sql_mp11_1eb)
c_1eb.executescript(sql_mp12_1eb)
conn_1eb.commit()
conn_1eb.close()
# Pembuatan absensi-2eb
conn_2eb = sqlite3.connect("ABSENSI_2EB.db")
c_2eb = conn_2eb.cursor()
sql_mp1_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Social_Networking_Creative_Cont(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Manajemen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perangkat_Lunak_Akuntansi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Ekonomi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Aspek_Hukum_Dalam_Ekonomi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bank_Lembaga_Keuangan2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Keu_Menengah2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Keuangan2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Informasi_Akuntansi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2eb.executescript(sql_mp1_2eb)
c_2eb.executescript(sql_mp2_2eb)
c_2eb.executescript(sql_mp3_2eb)
c_2eb.executescript(sql_mp4_2eb)
c_2eb.executescript(sql_mp5_2eb)
c_2eb.executescript(sql_mp6_2eb)
c_2eb.executescript(sql_mp7_2eb)
c_2eb.executescript(sql_mp8_2eb)
c_2eb.executescript(sql_mp9_2eb)
c_2eb.executescript(sql_mp10_2eb)
conn_2eb.commit()
conn_2eb.close()
# Pembuatan absensi-3eb
conn_3eb = sqlite3.connect("ABSENSI_3EB.db")
c_3eb = conn_3eb.cursor()
sql_mp1_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Pajak(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Internasional(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Bisnis2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Operasional(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Analisis_Perancangan_SIA(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Akuntansi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pemeriksaan_Akuntansi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Keuangan_Lanjut2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sains_Data_Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3eb.executescript(sql_mp1_3eb)
c_3eb.executescript(sql_mp2_3eb)
c_3eb.executescript(sql_mp3_3eb)
c_3eb.executescript(sql_mp4_3eb)
c_3eb.executescript(sql_mp5_3eb)
c_3eb.executescript(sql_mp6_3eb)
c_3eb.executescript(sql_mp7_3eb)
c_3eb.executescript(sql_mp8_3eb)
c_3eb.executescript(sql_mp9_3eb)
c_3eb.executescript(sql_mp10_3eb)
conn_3eb.commit()
conn_3eb.close()
# Pembuatan absensi-4eb
conn_4eb = sqlite3.connect("ABSENSI_4EB.db")
c_4eb = conn_4eb.cursor()
sql_mp1_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kewirausahaan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Studi_Kelayakan_Bisnis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Seminar_Kajian_Bidang_Akuntansi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akun_Forensik_AuditInvestigatif(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Syariah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Perpajakan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4eb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kecerdasan_Artifisial_Masy(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4eb.executescript(sql_mp1_4eb)
c_4eb.executescript(sql_mp2_4eb)
c_4eb.executescript(sql_mp3_4eb)
c_4eb.executescript(sql_mp4_4eb)
c_4eb.executescript(sql_mp5_4eb)
c_4eb.executescript(sql_mp6_4eb)
c_4eb.executescript(sql_mp7_4eb)
conn_4eb.commit()
conn_4eb.close()

# MANAJEMEN
# Pembuatan absensi-1ea
conn_1ea = sqlite3.connect("ABSENSI_1EA.db")
c_1ea = conn_1ea.cursor()
sql_mp1_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2A(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2B(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Komputer_TI_2C(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Digital_Citizenship(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_Ekonomi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Akuntansi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Pemasaran(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Manajemen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_1ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Ekonomi2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ea.executescript(sql_mp1_1ea)
c_1ea.executescript(sql_mp2_1ea)
c_1ea.executescript(sql_mp3_1ea)
c_1ea.executescript(sql_mp4_1ea)
c_1ea.executescript(sql_mp5_1ea)
c_1ea.executescript(sql_mp6_1ea)
c_1ea.executescript(sql_mp7_1ea)
c_1ea.executescript(sql_mp8_1ea)
c_1ea.executescript(sql_mp9_1ea)
c_1ea.executescript(sql_mp10_1ea)
c_1ea.executescript(sql_mp11_1ea)
c_1ea.executescript(sql_mp12_1ea)
conn_1ea.commit()
conn_1ea.close()
# Pembuatan absensi-2ea
conn_2ea = sqlite3.connect("ABSENSI_2EA.db")
c_2ea = conn_2ea.cursor()
sql_mp1_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Social_Networking_Creative_Cont(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Manajemen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Ekonomi_Manajerial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Riset_Operasional_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Ekonomi_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pengantar_Teknologi_SIM_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mnj_Keu_Era_Rev_Industri_4(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komp_Lembaga_Keu_Perbankan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ea.executescript(sql_mp1_2ea)
c_2ea.executescript(sql_mp2_2ea)
c_2ea.executescript(sql_mp3_2ea)
c_2ea.executescript(sql_mp4_2ea)
c_2ea.executescript(sql_mp5_2ea)
c_2ea.executescript(sql_mp6_2ea)
c_2ea.executescript(sql_mp7_2ea)
c_2ea.executescript(sql_mp8_2ea)
c_2ea.executescript(sql_mp9_2ea)
conn_2ea.commit()
conn_2ea.close()
# Pembuatan absensi-3ea
conn_3ea = sqlite3.connect("ABSENSI_3EA.db")
c_3ea = conn_3ea.cursor()
sql_mp1_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komp_Perpajakan_Untuk_Manaj(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Proyeksi_Bisnis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perilaku_Konsumen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perekonomian_Indonesia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_Bisnis_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Sumber_Daya_Manusia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Etika_Bisnis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sains_Data_Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Studi_Kelayakan_Bisnis(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ea.executescript(sql_mp1_3ea)
c_3ea.executescript(sql_mp2_3ea)
c_3ea.executescript(sql_mp3_3ea)
c_3ea.executescript(sql_mp4_3ea)
c_3ea.executescript(sql_mp5_3ea)
c_3ea.executescript(sql_mp6_3ea)
c_3ea.executescript(sql_mp7_3ea)
c_3ea.executescript(sql_mp8_3ea)
c_3ea.executescript(sql_mp9_3ea)
conn_3ea.commit()
conn_3ea.close()
# Pembuatan absensi-4ea
conn_4ea = sqlite3.connect("ABSENSI_4EA.db")
c_4ea = conn_4ea.cursor()
sql_mp1_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Akuntansi_Manajemen_Lanjut(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kapita_Selekta_Pasar_Modal(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Kinerja(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Pemasaran_Industri(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Seminar_Kajian_Bidang_Manajemen(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Risiko(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_4ea = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kecerdasan_Artifisial_Masy(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ea.executescript(sql_mp1_4ea)
c_4ea.executescript(sql_mp2_4ea)
c_4ea.executescript(sql_mp3_4ea)
c_4ea.executescript(sql_mp4_4ea)
c_4ea.executescript(sql_mp5_4ea)
c_4ea.executescript(sql_mp6_4ea)
c_4ea.executescript(sql_mp7_4ea)
conn_4ea.commit()
conn_4ea.close()

# ARSITEKTUR
# Pembuatan absensi-1tb
conn_1tb = sqlite3.connect("ABSENSI_1TB.db")
c_1tb = conn_1tb.cursor()
sql_mp1_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Estetika_Bentuk_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Auto_CAD_J(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Auto_CAD_I(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Struktur_Konstruksi_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Studio_Peranc_Arsitektur_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Metode_Perancangan_Arsitektur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Arsitektur_1(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1tb.executescript(sql_mp1_1tb)
c_1tb.executescript(sql_mp2_1tb)
c_1tb.executescript(sql_mp3_1tb)
c_1tb.executescript(sql_mp4_1tb)
c_1tb.executescript(sql_mp5_1tb)
c_1tb.executescript(sql_mp6_1tb)
c_1tb.executescript(sql_mp7_1tb)
c_1tb.executescript(sql_mp8_1tb)
c_1tb.executescript(sql_mp9_1tb)
conn_1tb.commit()
conn_1tb.close()
# Pembuatan absensi-2tb
conn_2tb = sqlite3.connect("ABSENSI_2TB.db")
c_2tb = conn_2tb.cursor()
sql_mp1_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Studio_Peranc_Arsitektur_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknik_Komunikasi_Arsitektural(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Filsafat_Arsitektur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Struktur_Konstruksi_3(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Utilitas_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Kewarganegaraan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perkembangan_Arsitektur_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Bahan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Tapak(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2tb.executescript(sql_mp1_2tb)
c_2tb.executescript(sql_mp2_2tb)
c_2tb.executescript(sql_mp3_2tb)
c_2tb.executescript(sql_mp4_2tb)
c_2tb.executescript(sql_mp5_2tb)
c_2tb.executescript(sql_mp6_2tb)
c_2tb.executescript(sql_mp7_2tb)
c_2tb.executescript(sql_mp8_2tb)
c_2tb.executescript(sql_mp9_2tb)
c_2tb.executescript(sql_mp10_2tb)
conn_2tb.commit()
conn_2tb.close()
# Pembuatan absensi-3tb
conn_3tb = sqlite3.connect("ABSENSI_3TB.db")
c_3tb = conn_3tb.cursor()
sql_mp1_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kerja_Praktek(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kuliah_Lapangan_Studi_Ekskursi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fotografi_Arsitektur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Studio_Perancangan_Arsitektur_5(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tata_Ruang_Dalam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tata_Ruang_Luar(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sinematografi_Arsitektur(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3tb.executescript(sql_mp1_3tb)
c_3tb.executescript(sql_mp2_3tb)
c_3tb.executescript(sql_mp3_3tb)
c_3tb.executescript(sql_mp4_3tb)
c_3tb.executescript(sql_mp5_3tb)
c_3tb.executescript(sql_mp6_3tb)
c_3tb.executescript(sql_mp7_3tb)
c_3tb.executescript(sql_mp8_3tb)
conn_3tb.commit()
conn_3tb.close()
# Pembuatan absensi-4tb
conn_4tb = sqlite3.connect("ABSENSI_4TB.db")
c_4tb = conn_4tb.cursor()
sql_mp1_4tb = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4tb.executescript(sql_mp1_4tb)
conn_4tb.commit()
conn_4tb.close()

# TEKNIK SIPIL
# Pembuatan absensi-1ta
conn_1ta = sqlite3.connect("ABSENSI_1TA.db")
c_1ta = conn_1ta.cursor()
sql_mp1_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Matematika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Etika_Profesi_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teknologi_Kecerdasan_Artifisial(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekanika_Bahan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Fisika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekanika_Bahan_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kewirausahaan_Bisnis_Jasa_Konstru(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Pancasila(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ta.executescript(sql_mp1_1ta)
c_1ta.executescript(sql_mp2_1ta)
c_1ta.executescript(sql_mp3_1ta)
c_1ta.executescript(sql_mp4_1ta)
c_1ta.executescript(sql_mp5_1ta)
c_1ta.executescript(sql_mp6_1ta)
c_1ta.executescript(sql_mp7_1ta)
c_1ta.executescript(sql_mp8_1ta)
c_1ta.executescript(sql_mp9_1ta)
conn_1ta.commit()
conn_1ta.close()
# Pembuatan absensi-2ta
conn_2ta = sqlite3.connect("ABSENSI_2TA.db")
c_2ta = conn_2ta.cursor()
sql_mp1_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Komputasi_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Agama_Islam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Hidrologi_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Analisis_Struk_Statis_Tak_Tentu_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Hidrolika_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Lalu_Lintas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Hidrolika(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Mekanika_Tanah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Analisis_Struk_Statis_Tak_Tentu(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Konstruksi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_2ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Hidrologi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ta.executescript(sql_mp1_2ta)
c_2ta.executescript(sql_mp2_2ta)
c_2ta.executescript(sql_mp3_2ta)
c_2ta.executescript(sql_mp4_2ta)
c_2ta.executescript(sql_mp5_2ta)
c_2ta.executescript(sql_mp6_2ta)
c_2ta.executescript(sql_mp7_2ta)
c_2ta.executescript(sql_mp8_2ta)
c_2ta.executescript(sql_mp9_2ta)
c_2ta.executescript(sql_mp10_2ta)
c_2ta.executescript(sql_mp11_2ta)
conn_2ta.commit()
conn_2ta.close()
# Pembuatan absensi-3ta
conn_3ta = sqlite3.connect("ABSENSI_3TA.db")
c_3ta = conn_3ta.cursor()
sql_mp1_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Struktur_Jembatan_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Struktur_Baja_2R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Perkerasan_Jalan_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Metode_Numerik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peranc_Stru_Beton_Bertulang_2R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Pondasi_Dalam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kerja_Praktek(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Struktur_Jembatan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Perkerasan_Jalan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp10_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Struktur_Baja_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp11_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Terapan_Teori_Graf(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp12_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Pondasi_Dalam_R(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp13_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peranc_Struk_Beton_Bertulang_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp14_3ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perancangan_Pelabuhan_Udara(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ta.executescript(sql_mp1_3ta)
c_3ta.executescript(sql_mp2_3ta)
c_3ta.executescript(sql_mp3_3ta)
c_3ta.executescript(sql_mp4_3ta)
c_3ta.executescript(sql_mp5_3ta)
c_3ta.executescript(sql_mp6_3ta)
c_3ta.executescript(sql_mp7_3ta)
c_3ta.executescript(sql_mp8_3ta)
c_3ta.executescript(sql_mp9_3ta)
c_3ta.executescript(sql_mp10_3ta)
c_3ta.executescript(sql_mp11_3ta)
c_3ta.executescript(sql_mp12_3ta)
c_3ta.executescript(sql_mp13_3ta)
c_3ta.executescript(sql_mp14_3ta)
conn_3ta.commit()
conn_3ta.close()
# Pembuatan absensi-4ta
conn_4ta = sqlite3.connect("ABSENSI_4TA.db")
c_4ta = conn_4ta.cursor()
sql_mp1_4ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Robotika_Cerdas(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Rekayasa_Perbaikan_Tanah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Material_Beton_Berkelanjutan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ta = """
DROP TABLE IF EXISTS users;
CREATE TABLE Utilitas_Bangunan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ta.executescript(sql_mp1_4ta)
c_4ta.executescript(sql_mp2_4ta)
c_4ta.executescript(sql_mp3_4ta)
c_4ta.executescript(sql_mp4_4ta)
conn_4ta.commit()
conn_4ta.close()

# KOMUNIKASI
# Pembuatan absensi-1ma
conn_1ma = sqlite3.connect("ABSENSI_1MA.db")
c_1ma = conn_1ma.cursor()
sql_mp1_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Teori_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Algoritma_Pemrog_2_Processing(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Agama_Islam(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Digital_Citizenship(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Inggris_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Pendidikan_Kewarganegaraan(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Bahasa_Indonesia(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sosiologi_Komunikasi_Informasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp9_1ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Dasar_Dasar_Jurnalistik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_1ma.executescript(sql_mp1_1ma)
c_1ma.executescript(sql_mp2_1ma)
c_1ma.executescript(sql_mp3_1ma)
c_1ma.executescript(sql_mp4_1ma)
c_1ma.executescript(sql_mp5_1ma)
c_1ma.executescript(sql_mp6_1ma)
c_1ma.executescript(sql_mp7_1ma)
c_1ma.executescript(sql_mp8_1ma)
c_1ma.executescript(sql_mp9_1ma)
conn_1ma.commit()
conn_1ma.close()
# Pembuatan absensi-2ma
conn_2ma = sqlite3.connect("ABSENSI_2MA.db")
c_2ma = conn_2ma.cursor()
sql_mp1_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Social_Networking_Creative_Cont(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Manajemen_Komunikasi_Organisasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Human_Relations(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Grafika_Komp_untuk_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Opini_Publik(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Peng_Teknologi_Radio_TV(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Statistika_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp8_2ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Media_Relations(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_2ma.executescript(sql_mp1_2ma)
c_2ma.executescript(sql_mp2_2ma)
c_2ma.executescript(sql_mp3_2ma)
c_2ma.executescript(sql_mp4_2ma)
c_2ma.executescript(sql_mp5_2ma)
c_2ma.executescript(sql_mp6_2ma)
c_2ma.executescript(sql_mp7_2ma)
c_2ma.executescript(sql_mp8_2ma)
conn_2ma.commit()
conn_2ma.close()
# Pembuatan absensi-3ma
conn_3ma = sqlite3.connect("ABSENSI_3MA.db")
c_3ma = conn_3ma.cursor()
sql_mp1_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Ilmiah(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sistem_Multimedia_2(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Etika_Filsafat_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Penulisan_Naskah_Komunikasi_II(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp5_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Event_Management(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp6_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Perencanaan_Kampanye_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp7_3ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Sains_Data_Analisis_Big_Data(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_3ma.executescript(sql_mp1_3ma)
c_3ma.executescript(sql_mp2_3ma)
c_3ma.executescript(sql_mp3_3ma)
c_3ma.executescript(sql_mp4_3ma)
c_3ma.executescript(sql_mp5_3ma)
c_3ma.executescript(sql_mp6_3ma)
c_3ma.executescript(sql_mp7_3ma)
conn_3ma.commit()
conn_3ma.close()
# Pembuatan absensi-4ma
conn_4ma = sqlite3.connect("ABSENSI_4MA.db")
c_4ma = conn_4ma.cursor()
sql_mp1_4ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Cyber_Public_Relations(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp2_4ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Kecerdasan_Artifisial_Masy(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp3_4ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Psikologi_Komunikasi(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
sql_mp4_4ma = """
DROP TABLE IF EXISTS users;
CREATE TABLE Tourism_Communication(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    KELAS VARCHAR,
    NPM VARCHAR UNIQUE,
    NAME TEXT,
    ATTENDANCE TEXT,
    DATE VARCHAR,
    TIME VARCHAR
);
"""
print("Table Created Succesfully")
c_4ma.executescript(sql_mp1_4ma)
c_4ma.executescript(sql_mp2_4ma)
c_4ma.executescript(sql_mp3_4ma)
c_4ma.executescript(sql_mp4_4ma)
conn_4ma.commit()
conn_4ma.close()