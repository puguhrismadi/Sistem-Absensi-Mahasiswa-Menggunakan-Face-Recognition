import cv2
import numpy as np
import os
import sqlite3
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

conn = sqlite3.connect("ABSENSI_4TA.db")
c = conn.cursor()
name = input('Masukkan Nama Anda : ')
npm = input('Masukkan NPM Anda : ')
kelas = input('Masukan Kelas Anda: ')
c.execute('INSERT INTO Robotika_Cerdas(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
c.execute('INSERT INTO Rekayasa_Perbaikan_Tanah(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
c.execute('INSERT INTO Material_Beton_Berkelanjutan(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
c.execute('INSERT INTO Utilitas_Bangunan(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Hidrolika_R(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Rekayasa_Lalu_Lintas(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Hidrolika(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Mekanika_Tanah(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Analisis_Struk_Statis_Tak_Tentu(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Manajemen_Konstruksi(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
# c.execute('INSERT INTO Rekayasa_Hidrologi(NPM,NAME,KELAS)VALUES(?,?,?)', (npm, name, kelas))
print("Records Created Successfully")

conn.commit()
conn.close()

        #
        # pic_no = 0
        # os.makedirs(name)
        # fa = cv2.CascadeClassifier('faces.xml')
        # cap = cv2.VideoCapture(0)
        #
        # ret = True
        # while ret:
        #     ret, frame = cap.read()
        #     frame = cv2.flip(frame, 1)
        #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #     faces = fa.detectMultiScale(gray, 1.3, 5)
        #     for(x,y,w,h) in faces:
        #         cropped = frame[y:y+h, x:x+w]
        #         cv2.rectangle(frame,(x,y), (x+w, y+h), (800, 0,0), 2, cv2.LINE_AA)
        #         pic_no = pic_no+1
        #         cv2.imwrite(name+ "/" + (name)+"%d.jpg" % pic_no, cropped)
        #     cv2.imshow('frame', frame)
        #     cv2.waitKey(49)
        #
        #     listener = sr.Recognizer()
        #     engine = pyttsx3.init()
        #     voices = engine.getProperty('voices')
        #     engine.setProperty('voice', voices[1].id)
        #
        #     if(pic_no>49):
        #         engine.say("CREATE DATASET IS FINISH")
        #         engine.runAndWait()
        #         break
        #
        # cap.release()
        # cv2.destroyAllWindows()