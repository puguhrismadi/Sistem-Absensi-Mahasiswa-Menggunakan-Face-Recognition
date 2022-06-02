#GUI lib
import tkinter as tk
from tkinter import *
import jurusan

class i_fks:
    def fks():
        window = tk.Tk()
        window.title("FR SYSTEM")
        window.geometry("360x450")

        wrapper_fks = LabelFrame(window, text="Fakultas")
        wrapper_fks.pack(fill="both", expand="yes", padx=20, pady=10)

        # create label Greeting
        lbl_Greeting = tk.Label(wrapper_fks,text="PILIH FAKULTAS")
        lbl_Greeting.place(x=110,y=10)

        # create btn
        def psi():
            jurusan.i_jrs.f_p()
        btn_fp = tk.Button(wrapper_fks,text="FP", width=15, height=2, command=psi)
        btn_fp.place(x=100, y=40)

        def sas():
            jurusan.i_jrs.f_s()
        btn_fs = tk.Button(wrapper_fks,text="FS", width=15, height=2, command=sas)
        btn_fs.place(x=100, y=85)

        def inf():
            jurusan.i_jrs.f_ti()
        btn_fti = tk.Button(wrapper_fks,text="FTI", width=15, height=2, command=inf)
        btn_fti.place(x=100, y=130)

        def fik():
            jurusan.i_jrs.f_ikti()
        btn_fikti = tk.Button(wrapper_fks,text="FIKTI", width=15, height=2, command=fik)
        btn_fikti.place(x=100, y=175)

        def fek():
            jurusan.i_jrs.f_e()
        btn_fe = tk.Button(wrapper_fks,text="FE", width=15, height=2,command=fek)
        btn_fe.place(x=100, y=220)

        def fetek():
            jurusan.i_jrs.f_tsp()
        btn_ftsp = tk.Button(wrapper_fks,text="FTSP", width=15, height=2, command=fetek)
        btn_ftsp.place(x=100, y=265)

        def fik_om():
            jurusan.i_jrs.f_kom()
        btn_ftsp = tk.Button(wrapper_fks,text="FIKOM", width=15, height=2, command=fik_om)
        btn_ftsp.place(x=100, y=310)

        window.mainloop()