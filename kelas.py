#GUI lib
import tkinter as tk
from tkinter import *
import recogabsen
import matkul

class kls_fp:
    def psik():
        psik = tk.Tk()
        psik.title("FR SYSTEM")
        psik.geometry("360x360")
        # Pembuatan Frame
        wrapper_psik = LabelFrame(psik, text="Psikologi")
        wrapper_psik.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gpsik = tk.Label(wrapper_psik, text="DAFTAR KELAS")
        lbl_gpsik.place(x=110,y=10)
        # create btn
        def mk_1pa():
            matkul.i_mk.mk1pa()
        btn_1pa = tk.Button(wrapper_psik, text="1-PA", width=15, height=2, command=mk_1pa)
        btn_1pa.place(x=100, y=40)
        def mk_2pa():
            matkul.i_mk.mk2pa()
        btn_2pa = tk.Button(wrapper_psik, text="2-PA", width=15, height=2, command=mk_2pa)
        btn_2pa.place(x=100, y=85)
        def mk_3pa():
            matkul.i_mk.mk3pa()
        btn_3pa = tk.Button(wrapper_psik, text="3-PA", width=15, height=2, command=mk_3pa)
        btn_3pa.place(x=100, y=130)
        def mk_4pa():
            matkul.i_mk.mk4pa()
        btn_4pa = tk.Button(wrapper_psik, text="4-PA", width=15, height=2, command=mk_4pa)
        btn_4pa.place(x=100, y=175)
        psik.mainloop()

class kls_fs:
    def sastra():
        sastra = tk.Tk()
        sastra.title("FR SYSTEM")
        sastra.geometry("360x360")
        # Pembuatan Frame
        wrapper_sastra = LabelFrame(sastra, text="Sastra Inggris")
        wrapper_sastra.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gsastra = tk.Label(wrapper_sastra, text="DAFTAR KELAS")
        lbl_gsastra.place(x=110,y=10)
        # create btn
        def mk_1sa():
            matkul.i_mk.mk1sa()
        btn_1sa = tk.Button(wrapper_sastra, text="1-SA", width=15, height=2, command=mk_1sa)
        btn_1sa.place(x=100, y=40)
        def mk_2sa():
            matkul.i_mk.mk2sa()
        btn_2sa = tk.Button(wrapper_sastra, text="2-SA", width=15, height=2, command=mk_2sa)
        btn_2sa.place(x=100, y=85)
        def mk_3sa():
            matkul.i_mk.mk3sa()
        btn_3sa = tk.Button(wrapper_sastra, text="3-SA", width=15, height=2, command=mk_3sa)
        btn_3sa.place(x=100, y=130)
        def mk_4sa():
            matkul.i_mk.mk4sa()
        btn_4sa = tk.Button(wrapper_sastra, text="4-SA", width=15, height=2, command=mk_4sa)
        btn_4sa.place(x=100, y=175)
        sastra.mainloop()

class kls_fikti:
    def si():
        si = tk.Tk()
        si.title("FR SYSTEM")
        si.geometry("360x360")
        # Pembuatan Frame
        wrapper_si = LabelFrame(si, text="Sistem Informasi")
        wrapper_si.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gsi = tk.Label(wrapper_si, text="DAFTAR KELAS")
        lbl_gsi.place(x=110,y=10)
        # create btn
        def mk_1ka():
            matkul.i_mk.mk1ka()
        btn_1ka = tk.Button(wrapper_si, text="1-KA", width=15, height=2, command=mk_1ka)
        btn_1ka.place(x=100, y=40)
        def mk_2ka():
            matkul.i_mk.mk2ka()
        btn_2ka = tk.Button(wrapper_si, text="2-KA", width=15, height=2, command=mk_2ka)
        btn_2ka.place(x=100, y=85)
        def mk_3ka():
            matkul.i_mk.mk3ka()
        btn_3ka = tk.Button(wrapper_si, text="3-KA", width=15, height=2, command=mk_3ka)
        btn_3ka.place(x=100, y=130)
        def mk_4ka():
            matkul.i_mk.mk4ka()
        btn_4ka = tk.Button(wrapper_si, text="4-KA", width=15, height=2, command=mk_4ka)
        btn_4ka.place(x=100, y=175)
        si.mainloop()

    def sk():
        sk = tk.Tk()
        sk.title("FR SYSTEM")
        sk.geometry("360x360")
        # Pembuatan Frame
        wrapper_sk = LabelFrame(sk, text="Sistem Komputer")
        wrapper_sk.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gsi = tk.Label(wrapper_sk, text="DAFTAR KELAS")
        lbl_gsi.place(x=110,y=10)
        # create btn
        def mk_1kb():
            matkul.i_mk.mk1kb()
        btn_1kb = tk.Button(wrapper_sk, text="1-KB", width=15, height=2, command=mk_1kb)
        btn_1kb.place(x=100, y=40)
        def mk_2kb():
            matkul.i_mk.mk2kb()
        btn_2kb = tk.Button(wrapper_sk, text="2-KB", width=15, height=2, command=mk_2kb)
        btn_2kb.place(x=100, y=85)
        def mk_3kb():
            matkul.i_mk.mk3kb()
        btn_3kb = tk.Button(wrapper_sk, text="3-KB", width=15, height=2, command=mk_3kb)
        btn_3kb.place(x=100, y=130)
        def mk_4kb():
            matkul.i_mk.mk4kb()
        btn_4kb = tk.Button(wrapper_sk, text="4-KB", width=15, height=2, command=mk_4kb)
        btn_4kb.place(x=100, y=175)
        sk.mainloop()

class kls_fti:
    def indus():
        indus = tk.Tk()
        indus.title("FR SYSTEM")
        indus.geometry("360x360")
        # Pembuatan Frame
        wrapper_indus= LabelFrame(indus, text="Teknik Industri")
        wrapper_indus.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gindus= tk.Label(wrapper_indus,text="DAFTAR KELAS")
        lbl_gindus.place(x=100,y=10)
        # create btn
        def mk_1id():
            matkul.i_mk.mk1id()
        btn_1id = tk.Button(wrapper_indus,text="1-ID", width=15, height=2, command=mk_1id)
        btn_1id.place(x=100, y=40)
        def mk_2id():
            matkul.i_mk.mk2id()
        btn_2id = tk.Button(wrapper_indus,text="2-ID", width=15, height=2, command=mk_2id)
        btn_2id.place(x=100, y=85)
        def mk_3id():
            matkul.i_mk.mk3id()
        btn_3id = tk.Button(wrapper_indus,text="3-ID", width=15, height=2, command=mk_3id)
        btn_3id.place(x=100, y=130)
        def mk_4id():
            matkul.i_mk.mk4id()
        btn_4id = tk.Button(wrapper_indus,text="4-ID", width=15, height=2, command=mk_4id)
        btn_4id.place(x=100, y=175)
        indus.mainloop()

    def kls_inf():
        kls_inf = tk.Tk()
        kls_inf.title("FR SYSTEM")
        kls_inf.geometry("360x360")
        # Pembuatan Frame
        wrapper_klsinf= LabelFrame(kls_inf, text="Teknik Informatika")
        wrapper_klsinf.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gklsinf = tk.Label(wrapper_klsinf,text="DAFTAR KELAS")
        lbl_gklsinf.place(x=110,y=10)
        # create btn
        def mk_1ia():
            matkul.i_mk.mk1ia()
        btn_1ia = tk.Button(wrapper_klsinf,text="1-IA", width=15, height=2, command=mk_1ia)
        btn_1ia.place(x=100, y=40)
        def mk_2ia():
            matkul.i_mk.mk2ia()
        btn_2ia = tk.Button(wrapper_klsinf,text="2-IA", width=15, height=2, command=mk_2ia)
        btn_2ia.place(x=100, y=85)
        def mk_3ia():
            matkul.i_mk.mk3ia()
        btn_3ia = tk.Button(wrapper_klsinf,text="3-IA", width=15, height=2, command=mk_3ia)
        btn_3ia.place(x=100, y=130)
        def mk_4ia():
            matkul.i_mk.mk4ia()
        btn_4ia = tk.Button(wrapper_klsinf,text="4-IA", width=15, height=2, command=mk_4ia)
        btn_4ia.place(x=100, y=175)
        kls_inf.mainloop()

    def tekmes():
        tekmes = tk.Tk()
        tekmes.title("FR SYSTEM")
        tekmes.geometry("360x360")
        # Pembuatan Frame
        wrapper_tekmes= LabelFrame(tekmes, text="Teknik Mesin")
        wrapper_tekmes.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gklsinf = tk.Label(wrapper_tekmes,text="DAFTAR KELAS")
        lbl_gklsinf.place(x=110,y=10)
        # create btn
        def mk_1ic():
            matkul.i_mk.mk1ic()
        btn_1ic = tk.Button(wrapper_tekmes,text="1-IC", width=15, height=2, command=mk_1ic)
        btn_1ic.place(x=100, y=40)
        def mk_2ic():
            matkul.i_mk.mk2ic()
        btn_2ic = tk.Button(wrapper_tekmes,text="2-IC", width=15, height=2, command=mk_2ic)
        btn_2ic.place(x=100, y=85)
        def mk_3ic():
            matkul.i_mk.mk3ic()
        btn_3ic = tk.Button(wrapper_tekmes,text="3-IC", width=15, height=2, command=mk_3ic)
        btn_3ic.place(x=100, y=130)
        def mk_4ic():
            matkul.i_mk.mk4ic()
        btn_4ic = tk.Button(wrapper_tekmes,text="4-IC", width=15, height=2, command=mk_4ic)
        btn_4ic.place(x=100, y=175)
        tekmes.mainloop()

    def tekel():
        tekel = tk.Tk()
        tekel.title("FR SYSTEM")
        tekel.geometry("360x360")
        # Pembuatan Frame
        wrapper_tekel= LabelFrame(tekel, text="Teknik Elektro")
        wrapper_tekel.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gtekel = tk.Label(wrapper_tekel,text="DAFTAR KELAS")
        lbl_gtekel.place(x=110,y=10)
        # create btn
        def mk_1ib():
            matkul.i_mk.mk1ib()
        btn_1ib = tk.Button(wrapper_tekel,text="1-IB", width=15, height=2, command=mk_1ib)
        btn_1ib.place(x=100, y=40)
        def mk_2ib():
            matkul.i_mk.mk2ib()
        btn_2ib = tk.Button(wrapper_tekel,text="2-IB", width=15, height=2, command=mk_2ib)
        btn_2ib.place(x=100, y=85)
        def mk_3ib():
            matkul.i_mk.mk3ib()
        btn_3ib = tk.Button(wrapper_tekel,text="3-IB", width=15, height=2, command=mk_3ib)
        btn_3ib.place(x=100, y=130)
        def mk_4ib():
            matkul.i_mk.mk4ib()
        btn_4ib = tk.Button(wrapper_tekel,text="4-IB", width=15, height=2, command=mk_4ib)
        btn_4ib.place(x=100, y=175)
        tekel.mainloop()

class kls_fe:
    def akun():
        Akunt = tk.Tk()
        Akunt.title("FR SYSTEM")
        Akunt.geometry("360x360")
        # Pembuatan Frame
        wrapper_Akunt = LabelFrame(Akunt, text="Akuntansi")
        wrapper_Akunt.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gilekono = tk.Label(wrapper_Akunt, text="DAFTAR KELAS")
        lbl_gilekono.place(x=110, y=10)
        # create btn
        def mk_1eb():
            matkul.i_mk.mk1eb()
        btn_1eb = tk.Button(wrapper_Akunt, text="1-EB", width=15, height=2, command=mk_1eb)
        btn_1eb.place(x=100, y=40)
        def mk_2eb():
            matkul.i_mk.mk2eb()
        btn_2eb = tk.Button(wrapper_Akunt, text="2-EB", width=15, height=2, command=mk_2eb)
        btn_2eb.place(x=100, y=85)
        def mk_3eb():
            matkul.i_mk.mk3eb()
        btn_3eb = tk.Button(wrapper_Akunt, text="3-EB", width=15, height=2, command=mk_3eb)
        btn_3eb.place(x=100, y=130)
        def mk_4eb():
            matkul.i_mk.mk4eb()
        btn_4eb = tk.Button(wrapper_Akunt, text="4-EB", width=15, height=2, command=mk_4eb)
        btn_4eb.place(x=100, y=175)
        Akunt.mainloop()
    def manaj():
        manaj = tk.Tk()
        manaj.title("FR SYSTEM")
        manaj.geometry("360x360")
        # Pembuatan Frame
        wrapper_manaj = LabelFrame(manaj, text="Manajemen")
        wrapper_manaj.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmanaj = tk.Label(wrapper_manaj, text="DAFTAR KELAS")
        lbl_gmanaj.place(x=110, y=10)
        # create btn
        def mk_1ea():
            matkul.i_mk.mk1ea()
        btn_1ea = tk.Button(wrapper_manaj, text="1-EA", width=15, height=2, command=mk_1ea)
        btn_1ea.place(x=100, y=40)
        def mk_2ea():
            matkul.i_mk.mk2ea()
        btn_2ea = tk.Button(wrapper_manaj, text="2-EA", width=15, height=2, command=mk_2ea)
        btn_2ea.place(x=100, y=85)
        def mk_3ea():
            matkul.i_mk.mk3ea()
        btn_3ea = tk.Button(wrapper_manaj, text="3-EA", width=15, height=2, command=mk_3ea)
        btn_3ea.place(x=100, y=130)
        def mk_4ea():
            matkul.i_mk.mk4ea()
        btn_4ea = tk.Button(wrapper_manaj, text="4-EA", width=15, height=2, command=mk_4ea)
        btn_4ea.place(x=100, y=175)
        manaj.mainloop()

class kls_ftsp:
    def arsi():
        arsi = tk.Tk()
        arsi.title("FR SYSTEM")
        arsi.geometry("360x360")
        # Pembuatan Frame
        wrapper_arsi = LabelFrame(arsi, text="Arsitektur")
        wrapper_arsi.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_garsi = tk.Label(wrapper_arsi, text="DAFTAR KELAS")
        lbl_garsi.place(x=110, y=10)
        # create btn
        def mk_1tb():
            matkul.i_mk.mk1tb()
        btn_1tb = tk.Button(wrapper_arsi, text="1-TB", width=15, height=2, command=mk_1tb)
        btn_1tb.place(x=100, y=40)
        def mk_2tb():
            matkul.i_mk.mk2tb()
        btn_2tb = tk.Button(wrapper_arsi, text="2-TB", width=15, height=2, command=mk_2tb)
        btn_2tb.place(x=100, y=85)
        def mk_3tb():
            matkul.i_mk.mk3tb()
        btn_3tb = tk.Button(wrapper_arsi, text="3-TB", width=15, height=2, command=mk_3tb)
        btn_3tb.place(x=100, y=130)
        def mk_4tb():
            matkul.i_mk.mk4tb()
        btn_4tb = tk.Button(wrapper_arsi, text="4-TB", width=15, height=2, command=mk_4tb)
        btn_4tb.place(x=100, y=175)
        arsi.mainloop()
    def tesil():
        tesil = tk.Tk()
        tesil.title("FR SYSTEM")
        tesil.geometry("360x360")
        # Pembuatan Frame
        wrapper_tesil = LabelFrame(tesil, text="Teknik Sipil")
        wrapper_tesil.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gtesil = tk.Label(wrapper_tesil, text="DAFTAR KELAS")
        lbl_gtesil.place(x=110, y=10)
        # create btn
        def mk_1ta():
            matkul.i_mk.mk1ta()
        btn_1ta = tk.Button(wrapper_tesil, text="1-TA", width=15, height=2, command=mk_1ta)
        btn_1ta.place(x=100, y=40)
        def mk_2ta():
            matkul.i_mk.mk2ta()
        btn_2ta = tk.Button(wrapper_tesil, text="2-TA", width=15, height=2, command=mk_2ta)
        btn_2ta.place(x=100, y=85)
        def mk_3ta():
            matkul.i_mk.mk3ta()
        btn_3ta = tk.Button(wrapper_tesil, text="3-TA", width=15, height=2, command=mk_3ta)
        btn_3ta.place(x=100, y=130)
        def mk_4ta():
            matkul.i_mk.mk4ta()
        btn_4ta = tk.Button(wrapper_tesil, text="4-TA", width=15, height=2, command=mk_4ta)
        btn_4ta.place(x=100, y=175)
        tesil.mainloop()

class kls_fikom:
    def komu():
        komu = tk.Tk()
        komu.title("FR SYSTEM")
        komu.geometry("360x360")
        # Pembuatan Frame
        wrapper_komu = LabelFrame(komu, text="Komunikasi")
        wrapper_komu.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gkomu = tk.Label(wrapper_komu, text="DAFTAR KELAS")
        lbl_gkomu.place(x=110, y=10)
        # create btn
        def mk_1ma():
            matkul.i_mk.mk1ma()
        btn_1ma = tk.Button(wrapper_komu, text="1-MA", width=15, height=2, command=mk_1ma)
        btn_1ma.place(x=100, y=40)
        def mk_2ma():
            matkul.i_mk.mk2ma()
        btn_2ma = tk.Button(wrapper_komu, text="2-MA", width=15, height=2, command=mk_2ma)
        btn_2ma.place(x=100, y=85)
        def mk_3ma():
            matkul.i_mk.mk3ma()
        btn_3ma = tk.Button(wrapper_komu, text="3-MA", width=15, height=2, command=mk_3ma)
        btn_3ma.place(x=100, y=130)
        def mk_4ma():
            matkul.i_mk.mk4ma()
        btn_4ma = tk.Button(wrapper_komu, text="4-MA", width=15, height=2, command=mk_4ma)
        btn_4ma.place(x=100, y=175)
        komu.mainloop()