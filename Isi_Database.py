import sqlite3

conn = sqlite3.connect('ABSENSI_3IA.db')
c = conn.cursor()

# def view1():
#     print("DESAIN PEMODELAN GRAFIK")
#     data = c.execute('''SELECT*FROM Sistem_Keamanan_Komputer''')
#     for row in data:
#         print(row)
# view1()
#  ---------

# def view2():
#     print("INTERAKSI MANUSIA & KOMPUTER")
#     data = c.execute('''SELECT*FROM Interaksi_Manusia_dan_Komputer''')
#     for row in data:
#         print(row)
# view2()
#  ---------

# def view3():
#     print("REKAYASA KOMPUTASIONAL")
#     data = c.execute('''SELECT*FROM Rekayasa_Komputasional''')
#     for row in data:
#         print(row)
# view3()
#  ---------

def view4():
    print("TEORI BAHASA & OTOMATA")
    data = c.execute('''SELECT*FROM Teori_Bahasa_dan_Otomata''')
    for row in data:
        print(row)
view4()
#  ---------

# def view5():
#     print("SISTEM KEAMANAN KOMPUTER")
#     data = c.execute('''SELECT*FROM Sistem_Keamanan_Komputer''')
#     for row in data:
#         print(row)
# view5()
#  ---------

# def view6():
#     print("SISTEM BASIS DATA 2")
#     data = c.execute('''SELECT*FROM Sistem_Basis_Data_2''')
#     for row in data:
#         print(row)
# view6()
#  ---------

# def view7():
#     print("GRAFIK KOMPUTER")
#     data = c.execute('''SELECT*FROM Grafik_Komputer_2''')
#     for row in data:
#         print(row)
# view7()
#  ---------

# def view8():
#     print("TEKNOLOGI GAME")
#     data = c.execute('''SELECT*FROM Teknologi_Game''')
#     for row in data:
#         print(row)
# view8()
#  ---------

# def view9():
#     print("PENULISAN ILMIAH")
#     data = c.execute('''SELECT*FROM Penulisan_Ilmiah''')
#     for row in data:
#         print(row)
# view9()
#  ---------
conn.commit()
c.close()
conn.close()
