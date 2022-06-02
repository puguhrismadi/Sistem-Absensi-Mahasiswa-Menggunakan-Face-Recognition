#GUI lib
import tkinter as tk
from tkinter import *
import kelas

class i_jrs:
    def f_p():
        f_p = tk.Tk()
        f_p.title("FR SYSTEM")
        f_p.geometry("360x360")
        # pembutaan Frame
        wrapper_f_p = LabelFrame(f_p, text="Fakultas Psikologi")
        wrapper_f_p.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gp = tk.Label(wrapper_f_p, text="DAFTAR JURUSAN")
        lbl_gp.place(x=100, y=10)
        # create btn
        def f_psi():
            kelas.kls_fp.psik()
        btn_p = tk.Button(wrapper_f_p, text="PSIKOLOGI", width=25, height=2, command=f_psi)
        btn_p.place(x=60, y=50)
        f_p.mainloop()

    def f_s():
        f_s = tk.Tk()
        f_s.title("FR SYSTEM")
        f_s.geometry("360x360")
        # pembutaan Frame
        wrapper_f_s = LabelFrame(f_s, text="Fakultas Sastra")
        wrapper_f_s.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gs= tk.Label(wrapper_f_s, text="DAFTAR JURUSAN")
        lbl_gs.place(x=100, y=10)
        # create btn
        def sast():
            kelas.kls_fs.sastra()
        btn_sasi = tk.Button(wrapper_f_s, text="SASTRA INGGRIS", width=25, height=2, command=sast)
        btn_sasi.place(x=60, y=50)
        f_s.mainloop()

    def f_ikti():
        f_ikti = tk.Tk()
        f_ikti.title("FR SYSTEM")
        f_ikti.geometry("360x360")
        # pembutaan Frame
        wrapper_f_ikti = LabelFrame(f_ikti, text="Fakultas Ilmu Komputer dan Teknologi Informasi")
        wrapper_f_ikti.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gikti = tk.Label(wrapper_f_ikti, text="DAFTAR JURUSAN")
        lbl_gikti.place(x=100, y=10)
        # create btn
        def siin():
            kelas.kls_fikti.si()
        btn_si = tk.Button(wrapper_f_ikti, text="SISTEM INFORMASI", width=25, height=2, command=siin)
        btn_si.place(x=60, y=50)

        def siko():
            kelas.kls_fikti.sk()
        btn_ik = tk.Button(wrapper_f_ikti, text="SISTEM KOMPUTER", width=25, height=2, command=siko)
        btn_ik.place(x=60, y=100)
        f_ikti.mainloop()

    def f_ti():
        f_ti = tk.Tk()
        f_ti.title("FR SYSTEM")
        f_ti.geometry("360x360")
        # pembutaan Frame
        wrapper_f_ti = LabelFrame(f_ti, text="Fakultas Teknologi Industri")
        wrapper_f_ti.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gfti = tk.Label(wrapper_f_ti,text="DAFTAR JURUSAN")
        lbl_gfti.place(x=100,y=10)
        # create btn
        def industri():
            kelas.kls_fti.indus()
        btn_fp = tk.Button(wrapper_f_ti,text="TEKNIK INDUSTRI", width=25, height=2, command=industri)
        btn_fp.place(x=60, y=50)
        def informatika():
            kelas.kls_fti.kls_inf()
        btn_fs = tk.Button(wrapper_f_ti,text="TEKNIK INFORMATIKA", width=25, height=2, command=informatika)
        btn_fs.place(x=60, y=100)
        def mesin():
            kelas.kls_fti.tekmes()
        btn_tm = tk.Button(wrapper_f_ti,text="TEKNIK MESIN", width=25, height=2, command=mesin)
        btn_tm.place(x=60, y=150)
        def elektro():
            kelas.kls_fti.tekel()
        btn_te = tk.Button(wrapper_f_ti,text="TEKNIK ELEKTRO", width=25, height=2, command=elektro)
        btn_te.place(x=60, y=200)
        f_ti.mainloop()

    def f_e():
        f_e = tk.Tk()
        f_e.title("FR SYSTEM")
        f_e.geometry("360x360")
        # pembutaan Frame
        wrapper_f_e = LabelFrame(f_e, text="Fakultas Ekonomi")
        wrapper_f_e.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gfe = tk.Label(wrapper_f_e, text="DAFTAR JURUSAN")
        lbl_gfe.place(x=100, y=10)
        # create btn
        def manajemen():
            kelas.kls_fe.manaj()
        btn_man = tk.Button(wrapper_f_e, text="MANAJEMEN", width=25, height=2, command=manajemen)
        btn_man.place(x=60, y=50)
        def akuntansi():
            kelas.kls_fe.akun()
        btn_akn = tk.Button(wrapper_f_e, text="AKUNTANSI", width=25, height=2, command=akuntansi)
        btn_akn.place(x=60, y=100)
        f_e.mainloop()

    def f_tsp():
        f_tsp = tk.Tk()
        f_tsp.title("FR SYSTEM")
        f_tsp.geometry("360x360")
        # pembutaan Frame
        wrapper_f_tsp = LabelFrame(f_tsp, text="Fakultas Teknik Sipil dan Perencanaan")
        wrapper_f_tsp.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gtsp = tk.Label(wrapper_f_tsp, text="DAFTAR JURUSAN")
        lbl_gtsp.place(x=100, y=10)
        # create btn
        def arsitek():
            kelas.kls_ftsp.arsi()
        btn_a = tk.Button(wrapper_f_tsp, text="ARSITEKTUR", width=25, height=2, command=arsitek)
        btn_a.place(x=60, y=50)
        def sipil():
            kelas.kls_ftsp.tesil()
        btn_ts = tk.Button(wrapper_f_tsp, text="TEKNIK SIPIL", width=25, height=2, command=sipil)
        btn_ts.place(x=60, y=100)
        f_tsp.mainloop()

    def f_kom():
        f_kom = tk.Tk()
        f_kom.title("FR SYSTEM")
        f_kom.geometry("360x360")
        # pembutaan Frame
        wrapper_f_kom = LabelFrame(f_kom, text="Fakultas Komunikasi")
        wrapper_f_kom.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gkom = tk.Label(wrapper_f_kom, text="DAFTAR JURUSAN")
        lbl_gkom.place(x=100, y=10)
        # create btn
        def komunikasi():
            kelas.kls_fikom.komu()
        btn_a = tk.Button(wrapper_f_kom, text="KOMUNIKASI", width=25, height=2, command=komunikasi)
        btn_a.place(x=60, y=50)