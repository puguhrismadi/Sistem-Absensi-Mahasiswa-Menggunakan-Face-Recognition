#GUI lib
import tkinter as tk
from tkinter import *
import recogabsen

class i_mk:
# PSIKOLOGI
    def mk1pa():
        mk1pa = tk.Tk()
        mk1pa.title("FR SYSTEM")
        mk1pa.geometry("360x540")
        wrapper_mk1pa = LabelFrame(mk1pa, text="mata kuliah")
        wrapper_mk1pa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1pa = tk.Label(wrapper_mk1pa,text="PILIH MATA KULIAH")
        lbl_gmk1pa.place(x=100,y=10)
        # create btn
        def psifaal_1pa():
            recogabsen.recabsen.PsikologiFaal_1pa()
        btn_mk1_1pa = tk.Button(wrapper_mk1pa,text="Psikologi Faal **", width=30, height=2, command=psifaal_1pa)
        btn_mk1_1pa.place(x=50, y=40)
        def psium_1pa():
            recogabsen.recabsen.DigiCiti_1pa()
        btn_mk2_1pa = tk.Button(wrapper_mk1pa,text="Psikologi Umum 2 *", width=30, height=2, command=psium_1pa)
        btn_mk2_1pa.place(x=50, y=85)
        def digiciti_1pa():
            recogabsen.recabsen.PsiUmum_1pa()
        btn_mk3_1pa = tk.Button(wrapper_mk1pa,text="Digital Citizenship", width=30, height=2, command=digiciti_1pa)
        btn_mk3_1pa.place(x=50, y=130)
        def psian_1pa():
            recogabsen.recabsen.psipeng_1pa()
        btn_mk4_1pa = tk.Button(wrapper_mk1pa,text="Psikologi Pengembangan 1", width=30, height=2, command=psian_1pa)
        btn_mk4_1pa.place(x=50, y=175)
        def bingpsik_1pa():
            recogabsen.recabsen.bingpsi_1pa()
        btn_mk5_1pa = tk.Button(wrapper_mk1pa,text="Bahasa Inggris Psikologi 2", width=30, height=2, command=bingpsik_1pa)
        btn_mk5_1pa.place(x=50, y=220)
        def mataldas_1pa():
            recogabsen.recabsen.matalda_1pa()
        btn_mk6_1pa = tk.Button(wrapper_mk1pa,text="Matematika & Ilmu Alamiah Dasar #", width=30, height=2, command=mataldas_1pa)
        btn_mk6_1pa.place(x=50, y=265)
        def bhsindo_1pa():
            recogabsen.recabsen.bindo_1pa()
        btn_mk7_1pa = tk.Button(wrapper_mk1pa,text="Bahasa Indonesia 2", width=30, height=2, command=bhsindo_1pa)
        btn_mk7_1pa.place(x=50, y=310)
        def penpancas_1pa():
            recogabsen.recabsen.penpanc_1pa()
        btn_mk8_1pa = tk.Button(wrapper_mk1pa,text="Pendidikan Pancasila *", width=30, height=2, command=penpancas_1pa)
        btn_mk8_1pa.place(x=50, y=355)
        def psikinf2A_1pa():
            recogabsen.recabsen.psiinf2A_1pa()
        btn_mk9_1pa = tk.Button(wrapper_mk1pa,text="Peng.Apl.Komp.Psi.Informatika 2A **", width=30, height=2, command=psikinf2A_1pa)
        btn_mk9_1pa.place(x=50, y=400)
        def psikinf2B_1pa():
            recogabsen.recabsen.psiinf2B_1pa()
        btn_mk10_1pa = tk.Button(wrapper_mk1pa,text="Peng.Apl.Komp.Psi.Informatika 2B **", width=30, height=2, command=psikinf2B_1pa)
        btn_mk10_1pa.place(x=50, y=445)
        mk1pa.mainloop()

    def mk2pa():
        mk2pa = tk.Tk()
        mk2pa.title("FR SYSTEM")
        mk2pa.geometry("360x540")
        wrapper_mk2pa = LabelFrame(mk2pa, text="mata kuliah")
        wrapper_mk2pa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2pa = tk.Label(wrapper_mk2pa,text="PILIH MATA KULIAH")
        lbl_gmk2pa.place(x=100,y=10)
        # create btn
        def socnetw_2pa():
            recogabsen.recabsen.socnet_2pa()
        btn_mk1_2pa = tk.Button(wrapper_mk2pa,text="Social Networking & Creative Cont", width=30, height=2, command=socnetw_2pa)
        btn_mk1_2pa.place(x=50, y=40)
        def metodol_2pa():
            recogabsen.recabsen.metodo_2pa()
        btn_mk2_2pa = tk.Button(wrapper_mk2pa,text="Metodologi Penelitian Kuantitatif", width=30, height=2, command=metodol_2pa)
        btn_mk2_2pa.place(x=50, y=85)
        def psiklinis_2pa():
            recogabsen.recabsen.psiklin_2pa()
        btn_mk3_2pa = tk.Button(wrapper_mk2pa,text="Psikologi Klinis", width=30, height=2, command=psiklinis_2pa)
        btn_mk3_2pa.place(x=50, y=130)
        def psikeprib_2pa():
            recogabsen.recabsen.psikep_2pa()
        btn_mk4_2pa = tk.Button(wrapper_mk2pa,text="Psikologi Kepribadian 2 *", width=30, height=2, command=psikeprib_2pa)
        btn_mk4_2pa.place(x=50, y=175)
        def psisosial_2pa():
            recogabsen.recabsen.psisos_2pa()
        btn_mk5_2pa = tk.Button(wrapper_mk2pa,text="Psikologi Sosial 2 *", width=30, height=2, command=psisosial_2pa)
        btn_mk5_2pa.place(x=50, y=220)
        def psikodiagnos_2pa():
            recogabsen.recabsen.psikodiag_2pa()
        btn_mk6_2pa = tk.Button(wrapper_mk2pa,text="Psikodiagnostika 2: Observasi **", width=30, height=2, command=psikodiagnos_2pa)
        btn_mk6_2pa.place(x=50, y=265)
        def kodetikpsi_2pa():
            recogabsen.recabsen.kodetik_2pa()
        btn_mk7_2pa = tk.Button(wrapper_mk2pa,text="Kode Etik Psikologi", width=30, height=2, command=kodetikpsi_2pa)
        btn_mk7_2pa.place(x=50, y=310)
        def statlanjut_2pa():
            recogabsen.recabsen.statlnj_2pa()
        btn_mk8_2pa = tk.Button(wrapper_mk2pa,text="Statistika Lanjut", width=30, height=2, command=statlanjut_2pa)
        btn_mk8_2pa.place(x=50, y=355)
        def filsmanus_2pa():
            recogabsen.recabsen.filsman_2pa()
        btn_mk9_2pa = tk.Button(wrapper_mk2pa,text="Filsafat Manusia *", width=30, height=2, command=filsmanus_2pa)
        btn_mk9_2pa.place(x=50, y=400)
        mk2pa.mainloop()

    def mk3pa():
        mk3pa = tk.Tk()
        mk3pa.title("FR SYSTEM")
        mk3pa.geometry("360x540")
        wrapper_mk3pa = LabelFrame(mk3pa, text="mata kuliah")
        wrapper_mk3pa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3pa = tk.Label(wrapper_mk3pa,text="PILIH MATA KULIAH")
        lbl_gmk3pa.place(x=100,y=10)
        # create btn
        def psikognit_3pa():
            recogabsen.recabsen.psikog_3pa()
        btn_mk1_3pa = tk.Button(wrapper_mk3pa,text="Psikologi Kognitif */**", width=30, height=2, command=psikognit_3pa)
        btn_mk1_3pa.place(x=50, y=40)
        def psikometri_3pa():
            recogabsen.recabsen.psikom_3pa()
        btn_mk2_3pa = tk.Button(wrapper_mk3pa,text="Psikometri *", width=30, height=2, command=psikometri_3pa)
        btn_mk2_3pa.place(x=50, y=85)
        def ergonomi_3pa():
            recogabsen.recabsen.ergo_3pa()
        btn_mk3_3pa = tk.Button(wrapper_mk3pa,text="Ergonomi", width=30, height=2, command=ergonomi_3pa)
        btn_mk3_3pa.place(x=50, y=130)
        def kreativ_3pa():
            recogabsen.recabsen.krea_3pa()
        btn_mk4_3pa = tk.Button(wrapper_mk3pa,text="Pengembangan Kreativitas & Kebe", width=30, height=2, command=kreativ_3pa)
        btn_mk4_3pa.place(x=50, y=175)
        def proyektif_3pa():
            recogabsen.recabsen.proyek_3pa()
        btn_mk5_3pa = tk.Button(wrapper_mk3pa,text="Test Proyektif **", width=30, height=2, command=proyektif_3pa)
        btn_mk5_3pa.place(x=50, y=220)
        def psikonseling_3pa():
            recogabsen.recabsen.psikonsel_3pa()
        btn_mk6_3pa = tk.Button(wrapper_mk3pa,text="Psikologi Konseling", width=30, height=2, command=psikonseling_3pa)
        btn_mk6_3pa.place(x=50, y=265)
        def penmiah_3pa():
            recogabsen.recabsen.pi_3pa()
        btn_mk7_3pa = tk.Button(wrapper_mk3pa,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=penmiah_3pa)
        btn_mk7_3pa.place(x=50, y=310)
        def psianakhusus_3pa():
            recogabsen.recabsen.psianak_3pa()
        btn_mk8_3pa = tk.Button(wrapper_mk3pa,text="Psikologi Anak Khusus", width=30, height=2, command=psianakhusus_3pa)
        btn_mk8_3pa.place(x=50, y=355)
        def psilintasbud_3pa():
            recogabsen.recabsen.psilinbud_3pa()
        btn_mk9_3pa = tk.Button(wrapper_mk3pa,text="Psikologi Lintas Budaya", width=30, height=2, command=psilintasbud_3pa)
        btn_mk9_3pa.place(x=50, y=400)
        def sainsbigdata_3pa():
            recogabsen.recabsen.sainbig_3pa()
        btn_mk10_3pa = tk.Button(wrapper_mk3pa, text="Sains Data & Analisis Big Data", width=30, height=2, command=sainsbigdata_3pa)
        btn_mk10_3pa.place(x=50, y=445)
        mk3pa.mainloop()

    def mk4pa():
        mk4pa = tk.Tk()
        mk4pa.title("FR SYSTEM")
        mk4pa.geometry("360x360")
        wrapper_mk4pa = LabelFrame(mk4pa, text="mata kuliah")
        wrapper_mk4pa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4pa = tk.Label(wrapper_mk4pa,text="PILIH MATA KULIAH")
        lbl_gmk4pa.place(x=100,y=10)
        # create btn
        def aplpsikognitif_4pa():
            recogabsen.recabsen.aplpsikog_4pa()
        btn_mk1_4pa = tk.Button(wrapper_mk4pa,text="Apl.Psi.Kognitif Sain dlm TIK", width=30, height=2, command=aplpsikognitif_4pa)
        btn_mk1_4pa.place(x=50, y=40)
        def konsalatukur_4pa():
            recogabsen.recabsen.alatukur_4pa()
        btn_mk2_4pa = tk.Button(wrapper_mk4pa,text="Konstruksi Alat Ukur", width=30, height=2, command=konsalatukur_4pa)
        btn_mk2_4pa.place(x=50, y=85)
        def artmasy_4pa():
            recogabsen.recabsen.masy_4pa()
        btn_mk3_4pa = tk.Button(wrapper_mk4pa,text="Kecerdasan Artifisial & Masy", width=30, height=2, command=artmasy_4pa)
        btn_mk3_4pa.place(x=50, y=130)
        mk4pa.mainloop()

#SASTRA
    def mk1sa():
        mk1sa = tk.Tk()
        mk1sa.title("FR SYSTEM")
        mk1sa.geometry("360x670")
        wrapper_mk1sa = LabelFrame(mk1sa, text="mata kuliah")
        wrapper_mk1sa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1sa = tk.Label(wrapper_mk1sa,text="PILIH MATA KULIAH")
        lbl_gmk1sa.place(x=100,y=10)
        # create btn
        def digicitiz_1sa():
            recogabsen.recabsen.digiciti_1sa()
        btn_mk1_1sa = tk.Button(wrapper_mk1sa,text="Digital Citizenship", width=30, height=2, command=digicitiz_1sa)
        btn_mk1_1sa.place(x=50, y=40)
        def penagis_1sa():
            recogabsen.recabsen.pai_1sa()
        btn_mk2_1sa = tk.Button(wrapper_mk1sa,text="Pendidikan Agama Islam", width=30, height=2, command=penagis_1sa)
        btn_mk2_1sa.place(x=50, y=85)
        def kosakata_1sa():
            recogabsen.recabsen.kokat_1sa()
        btn_mk3_1sa = tk.Button(wrapper_mk1sa,text="Kosa Kata **", width=30, height=2, command=kosakata_1sa)
        btn_mk3_1sa.place(x=50, y=130)
        def nyimak2A_1sa():
            recogabsen.recabsen.simak2A_1sa()
        btn_mk4_1sa = tk.Button(wrapper_mk1sa,text="Menyimak 2A", width=30, height=2, command=nyimak2A_1sa)
        btn_mk4_1sa.place(x=50, y=175)
        def nyimak2B_1sa():
            recogabsen.recabsen.simak2B_1sa()
        btn_mk5_1sa = tk.Button(wrapper_mk1sa,text="Menyimak 2B", width=30, height=2, command=nyimak2B_1sa)
        btn_mk5_1sa.place(x=50, y=220)
        def nyimak2C_1sa():
            recogabsen.recabsen.simak2C_1sa()
        btn_mk6_1sa = tk.Button(wrapper_mk1sa,text="Menyimak 2C", width=30, height=2, command=nyimak2C_1sa)
        btn_mk6_1sa.place(x=50, y=265)
        def bhsindo_1sa():
            recogabsen.recabsen.bindo_1sa()
        btn_mk7_1sa = tk.Button(wrapper_mk1sa,text="Bahasa Indonesia 2 *", width=30, height=2, command=bhsindo_1sa)
        btn_mk7_1sa.place(x=50, y=310)
        def berbicara2A_1sa():
            recogabsen.recabsen.bicara2A_1sa()
        btn_mk8_1sa = tk.Button(wrapper_mk1sa,text="Berbicara 2A **", width=30, height=2, command=berbicara2A_1sa)
        btn_mk8_1sa.place(x=50, y=355)
        def berbicara2B_1sa():
            recogabsen.recabsen.bicara2B_1sa()
        btn_mk9_1sa = tk.Button(wrapper_mk1sa,text="Berbicara 2B **", width=30, height=2, command=berbicara2B_1sa)
        btn_mk9_1sa.place(x=50, y=400)
        def membaca_1sa():
            recogabsen.recabsen.baca_1sa()
        btn_mk10_1sa = tk.Button(wrapper_mk1sa,text="Membaca 2", width=30, height=2, command=membaca_1sa)
        btn_mk10_1sa.place(x=50, y=445)
        def penpancas_1sa():
            recogabsen.recabsen.penpanc_1sa()
        btn_mk11_1sa = tk.Button(wrapper_mk1sa, text="Pendidikan Pancasila *", width=30, height=2, command=penpancas_1sa)
        btn_mk11_1sa.place(x=50, y=490)
        def tatabhs_1sa():
            recogabsen.recabsen.tabas_1sa()
        btn_mk12_1sa = tk.Button(wrapper_mk1sa, text="Tata Bahasa 2 **", width=30, height=2, command=tatabhs_1sa)
        btn_mk12_1sa.place(x=50, y=535)
        mk1sa.mainloop()

    def mk2sa():
        mk2sa = tk.Tk()
        mk2sa.title("FR SYSTEM")
        mk2sa.geometry("360x730")
        wrapper_mk2sa = LabelFrame(mk2sa, text="mata kuliah")
        wrapper_mk2sa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2sa = tk.Label(wrapper_mk2sa,text="PILIH MATA KULIAH")
        lbl_gmk2sa.place(x=100,y=10)
        # create btn
        def socnetw_2sa():
            recogabsen.recabsen.socnet_2sa()
        btn_mk1_2sa = tk.Button(wrapper_mk2sa,text="Social Networking & Creative Cont", width=30, height=2, command=socnetw_2sa)
        btn_mk1_2sa.place(x=50, y=40)
        def filmodern_2sa():
            recogabsen.recabsen.filmod_2sa()
        btn_mk2_2sa = tk.Button(wrapper_mk2sa,text="Peng.Filsafat & Pemikiran Modern", width=30, height=2, command=filmodern_2sa)
        btn_mk2_2sa.place(x=50, y=85)
        def basicact_2sa():
            recogabsen.recabsen.acting_2sa()
        btn_mk3_2sa = tk.Button(wrapper_mk2sa,text="BasicActing & StageProduction **", width=30, height=2, command=basicact_2sa)
        btn_mk3_2sa.place(x=50, y=130)
        def kosakata_2sa():
            recogabsen.recabsen.kokat_2sa()
        btn_mk4_2sa = tk.Button(wrapper_mk2sa,text="Kosa Kata 3", width=30, height=2, command=kosakata_2sa)
        btn_mk4_2sa.place(x=50, y=175)
        def berbicara4A_2sa():
            recogabsen.recabsen.bicara4A_2sa()
        btn_mk5_2sa = tk.Button(wrapper_mk2sa,text="Berbicara 4/A **", width=30, height=2, command=berbicara4A_2sa)
        btn_mk5_2sa.place(x=50, y=220)
        def berbicara4B_2sa():
            recogabsen.recabsen.bicara4B_2sa()
        btn_mk6_2sa = tk.Button(wrapper_mk2sa,text="Berbicara 4/B **", width=30, height=2, command=berbicara4B_2sa)
        btn_mk6_2sa.place(x=50, y=265)
        def fonbinggris_2sa():
            recogabsen.recabsen.fonbing_2sa()
        btn_mk7_2sa = tk.Button(wrapper_mk2sa,text="Fonologi Bahasa Inggris *", width=30, height=2, command=fonbinggris_2sa)
        btn_mk7_2sa.place(x=50, y=310)
        def humasy_2sa():
            recogabsen.recabsen.humas_2sa()
        btn_mk8_2sa = tk.Button(wrapper_mk2sa,text="Hubungan Masyarakat 2", width=30, height=2, command=humasy_2sa)
        btn_mk8_2sa.place(x=50, y=355)
        def penerjemahan_2sa():
            recogabsen.recabsen.terjemah_2sa()
        btn_mk9_2sa = tk.Button(wrapper_mk2sa,text="Penerjemahan 2", width=30, height=2, command=penerjemahan_2sa)
        btn_mk9_2sa.place(x=50, y=400)
        def readimg_2sa():
            recogabsen.recabsen.semiotika_2sa()
        btn_mk10_2sa = tk.Button(wrapper_mk2sa,text="Reading Images(Semiotika)", width=30, height=2, command=readimg_2sa)
        btn_mk10_2sa.place(x=50, y=445)
        def tatabhs_2sa():
            recogabsen.recabsen.tabas_2sa()
        btn_mk11_2sa = tk.Button(wrapper_mk2sa, text="Tata Bahasa 4 **", width=30, height=2, command=tatabhs_2sa)
        btn_mk11_2sa.place(x=50, y=490)
        def nyimak4A_2sa():
            recogabsen.recabsen.simak4A_2sa()
        btn_mk12_2sa = tk.Button(wrapper_mk2sa, text="Menyimak 4A", width=30, height=2, command=nyimak4A_2sa)
        btn_mk12_2sa.place(x=50, y=535)
        def nyimak4B_2sa():
            recogabsen.recabsen.simak4B_2sa()
        btn_mk13_2sa = tk.Button(wrapper_mk2sa, text="Menyimak 4B", width=30, height=2, command=nyimak4B_2sa)
        btn_mk13_2sa.place(x=50, y=580)
        def nyimak4C_2sa():
            recogabsen.recabsen.simak4C_2sa()
        btn_mk14_2sa = tk.Button(wrapper_mk2sa, text="Menyimak 4C", width=30, height=2, command=nyimak4C_2sa)
        btn_mk14_2sa.place(x=50, y=625)
        mk2sa.mainloop()

    def mk3sa():
        mk3sa = tk.Tk()
        mk3sa.title("FR SYSTEM")
        mk3sa.geometry("360x540")
        wrapper_mk3sa = LabelFrame(mk3sa, text="mata kuliah")
        wrapper_mk3sa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3sa = tk.Label(wrapper_mk3sa,text="PILIH MATA KULIAH")
        lbl_gmk3sa.place(x=100,y=10)
        # create btn
        def penah_3sa():
            recogabsen.recabsen.pi_3sa()
        btn_mk1_3sa = tk.Button(wrapper_mk3sa,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=penah_3sa)
        btn_mk1_3sa.place(x=50, y=40)
        def penerjemahankom_3sa():
            recogabsen.recabsen.terjemahankom_3sa()
        btn_mk2_3sa = tk.Button(wrapper_mk3sa,text="Penerjemahan Berbantuan Komp.", width=30, height=2, command=penerjemahankom_3sa)
        btn_mk2_3sa.place(x=50, y=85)
        def jurnalistik_3sa():
            recogabsen.recabsen.jurnal_3sa()
        btn_mk3_3sa = tk.Button(wrapper_mk3sa,text="Jurnalistik 2", width=30, height=2, command=jurnalistik_3sa)
        btn_mk3_3sa.place(x=50, y=130)
        def kajiprosa_3sa():
            recogabsen.recabsen.prosa_3sa()
        btn_mk4_3sa = tk.Button(wrapper_mk3sa,text="Pengkajian Prosa *", width=30, height=2, command=kajiprosa_3sa)
        btn_mk4_3sa.place(x=50, y=175)
        def sintaksbing_3sa():
            recogabsen.recabsen.sinbing_3sa()
        btn_mk5_3sa = tk.Button(wrapper_mk3sa,text="Sintaksis Bahasa Inggris *", width=30, height=2, command=sintaksbing_3sa)
        btn_mk5_3sa.place(x=50, y=220)
        def speaking_3sa():
            recogabsen.recabsen.speak_3sa()
        btn_mk6_3sa = tk.Button(wrapper_mk3sa,text="Public Speaking #", width=30, height=2, command=speaking_3sa)
        btn_mk6_3sa.place(x=50, y=265)
        def aud_3sa():
            recogabsen.recabsen.terjemahaud_3sa()
        btn_mk7_3sa = tk.Button(wrapper_mk3sa,text="Penerjemahan Audiovisual", width=30, height=2, command=aud_3sa)
        btn_mk7_3sa.place(x=50, y=310)
        def langass_3sa():
            recogabsen.recabsen.lang_3sa()
        btn_mk8_3sa = tk.Button(wrapper_mk3sa,text="Language Assessment", width=30, height=2, command=langass_3sa)
        btn_mk8_3sa.place(x=50, y=355)
        def jurubhs_3sa():
            recogabsen.recabsen.juruining_3sa()
        btn_mk9_3sa = tk.Button(wrapper_mk3sa,text="Kejurubahasaan Indonesia-Inggris", width=30, height=2, command=jurubhs_3sa)
        btn_mk9_3sa.place(x=50, y=400)
        def sainbigdat_3sa():
            recogabsen.recabsen.saindat_3sa()
        btn_mk10_3sa = tk.Button(wrapper_mk3sa, text="Sains Data & Analisis Big Data", width=30, height=2, command=sainbigdat_3sa)
        btn_mk10_3sa.place(x=50, y=445)
        mk3sa.mainloop()

    def mk4sa():
        mk4sa = tk.Tk()
        mk4sa.title("FR SYSTEM")
        mk4sa.geometry("360x360")
        wrapper_mk4sa = LabelFrame(mk4sa, text="mata kuliah")
        wrapper_mk4sa.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4sa = tk.Label(wrapper_mk4sa,text="PILIH MATA KULIAH")
        lbl_gmk4sa.place(x=100,y=10)
        # create btn
        def wacana_4sa():
            recogabsen.recabsen.wac_4sa()
        btn_mk1_4sa = tk.Button(wrapper_mk4sa,text="Analisis Wacana", width=30, height=2, command=wacana_4sa)
        btn_mk1_4sa.place(x=50, y=40)
        def mikro_4sa():
            recogabsen.recabsen.mik_4sa()
        btn_mk2_4sa = tk.Button(wrapper_mk4sa,text="Pengajaran Mikro", width=30, height=2, command=mikro_4sa)
        btn_mk2_4sa.place(x=50, y=85)
        def puising_4sa():
            recogabsen.recabsen.puisi_4sa()
        btn_mk3_4sa = tk.Button(wrapper_mk4sa,text="Pengkajian Puisi Inggris *", width=30, height=2, command=puising_4sa)
        btn_mk3_4sa.place(x=50, y=130)
        def artmasy_4sa():
            recogabsen.recabsen.masy_4sa()
        btn_mk4_4sa = tk.Button(wrapper_mk4sa, text="Kecerdasan Artifisial & Masy", width=30, height=2, command=artmasy_4sa)
        btn_mk4_4sa.place(x=50, y=130)
        mk4sa.mainloop()

# SISTEM INFORMASI
    def mk1ka():
        mk1ka = tk.Tk()
        mk1ka.title("FR SYSTEM")
        mk1ka.geometry("360x750")
        wrapper_mk1ka = LabelFrame(mk1ka, text="mata kuliah")
        wrapper_mk1ka.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ka = tk.Label(wrapper_mk1ka,text="PILIH MATA KULIAH")
        lbl_gmk1ka.place(x=100,y=10)
        # create btn
        def fskim2A_1ka():
            recogabsen.recabsen.fikim2A_1ka()
        btn_mk1_1ka = tk.Button(wrapper_mk1ka,text="Fisika & Kimia Dasar 2A", width=30, height=2, command=fskim2A_1ka)
        btn_mk1_1ka.place(x=50, y=40)
        def fskim2B_1ka():
            recogabsen.recabsen.fikim2B_1ka()
        btn_mk2_1ka = tk.Button(wrapper_mk1ka,text="Fisika & Kimia Dasar 2B", width=30, height=2, command=fskim2B_1ka)
        btn_mk2_1ka.place(x=50, y=85)
        def kecart_1ka():
            recogabsen.recabsen.art_1ka()
        btn_mk3_1ka = tk.Button(wrapper_mk1ka,text="Teknologi Kecerdasan Artifisial", width=30, height=2,command=kecart_1ka)
        btn_mk3_1ka.place(x=50, y=130)
        def algoan2A_1ka():
            recogabsen.recabsen.algan2A_1ka()
        btn_mk4_1ka = tk.Button(wrapper_mk1ka,text="Algoritma & Pemrograman 2A", width=30, height=2, command=algoan2A_1ka)
        btn_mk4_1ka.place(x=50, y=175)
        def algoan2B_1ka():
            recogabsen.recabsen.algan2B_1ka()
        btn_mk5_1ka = tk.Button(wrapper_mk1ka,text="Algoritma & Pemrograman 2B", width=30, height=2, command=algoan2B_1ka)
        btn_mk5_1ka.place(x=50, y=220)
        def algoan2C_1ka():
            recogabsen.recabsen.algan2C_1ka()
        btn_mk6_1ka = tk.Button(wrapper_mk1ka,text="Algoritma & Pemrograman 2C", width=30, height=2, command=algoan2C_1ka)
        btn_mk6_1ka.place(x=50, y=265)
        def teknoifA_1ka():
            recogabsen.recabsen.tenifA_1ka()
        btn_mk7_1ka = tk.Button(wrapper_mk1ka,text="Konsep Sistem Informasi A*/**", width=30, height=2, command=teknoifA_1ka)
        btn_mk7_1ka.place(x=50, y=310)
        def teknoifB_1ka():
            recogabsen.recabsen.tenifB_1ka()
        btn_mk8_1ka = tk.Button(wrapper_mk1ka,text="Konsep Sistem Informasi B*/**", width=30, height=2, command=teknoifB_1ka)
        btn_mk8_1ka.place(x=50, y=355)
        def teknoifC_1ka():
            recogabsen.recabsen.tenifC_1ka()
        btn_mk9_1ka = tk.Button(wrapper_mk1ka,text="Konsep Sistem Informasi C*/**", width=30, height=2, command=teknoifC_1ka)
        btn_mk9_1ka.place(x=50, y=400)
        def budaya_1ka():
            recogabsen.recabsen.bud_1ka()
        btn_mk10_1ka = tk.Button(wrapper_mk1ka,text="Ilmu Budaya Dasar #", width=30, height=2, command=budaya_1ka)
        btn_mk10_1ka.place(x=50, y=445)
        def binggris_1ka():
            recogabsen.recabsen.bing_1ka()
        btn_mk11_1ka = tk.Button(wrapper_mk1ka, text="Bahasa Inggris 2", width=30, height=2, command=binggris_1ka)
        btn_mk11_1ka.place(x=50, y=490)
        def penpancas_1ka():
            recogabsen.recabsen.penpanc_1ka()
        btn_mk12_1ka = tk.Button(wrapper_mk1ka, text="Pendidikan Pancasila *", width=30, height=2, command=penpancas_1ka)
        btn_mk12_1ka.place(x=50, y=535)
        def matdasar2A_1ka():
            recogabsen.recabsen.matdas2A_1ka()
        btn_mk13_1ka = tk.Button(wrapper_mk1ka, text="Matematika Dasar 2A", width=30, height=2, command=matdasar2A_1ka)
        btn_mk13_1ka.place(x=50, y=580)
        def matdasar2B_1ka():
            recogabsen.recabsen.matdas2B_1ka()
        btn_mk14_1ka = tk.Button(wrapper_mk1ka, text="Matematika Dasar 2B", width=30, height=2, command=matdasar2B_1ka)
        btn_mk14_1ka.place(x=50, y=625)
        def umum_1ka():
            recogabsen.recabsen.orgum_1ka()
        btn_mk15_1ka = tk.Button(wrapper_mk1ka, text="Teknologi Organisasi Umum 1", width=30, height=2, command=umum_1ka)
        btn_mk15_1ka.place(x=50, y=625)
        mk1ka.mainloop()

    def mk2ka():
        mk2ka = tk.Tk()
        mk2ka.title("FR SYSTEM")
        mk2ka.geometry("360x700")
        wrapper_mk2ka = LabelFrame(mk2ka, text="mata kuliah")
        wrapper_mk2ka.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ka = tk.Label(wrapper_mk2ka,text="PILIH MATA KULIAH")
        lbl_gmk2ka.place(x=100,y=10)
        # create btn
        def kombigdat_2ka():
            recogabsen.recabsen.kombig_2ka()
        btn_mk1_2ka = tk.Button(wrapper_mk2ka,text="Komputasi Big Data", width=30, height=2, command=kombigdat_2ka)
        btn_mk1_2ka.place(x=50, y=40)
        def matlanjut_2ka():
            recogabsen.recabsen.matlan_2ka()
        btn_mk2_2ka = tk.Button(wrapper_mk2ka,text="Matematika Lanjut 2 **", width=30, height=2, command=matlanjut_2ka)
        btn_mk2_2ka.place(x=50, y=85)
        def matsin_2ka():
            recogabsen.recabsen.matsi_2ka()
        btn_mk3_2ka = tk.Button(wrapper_mk2ka,text="Matematika Sistem Informasi 2", width=30, height=2, command=matsin_2ka)
        btn_mk3_2ka.place(x=50, y=130)
        def ordata_2ka():
            recogabsen.recabsen.ordat_2ka()
        btn_mk4_2ka = tk.Button(wrapper_mk2ka,text="Struktur & Organisasi Data 2 *", width=30, height=2, command=ordata_2ka)
        btn_mk4_2ka.place(x=50, y=175)
        def akuntan_2ka():
            recogabsen.recabsen.akun_2ka()
        btn_mk5_2ka = tk.Button(wrapper_mk2ka,text="Pengantar Akuntansi Keuangan 2", width=30, height=2, command=akuntan_2ka)
        btn_mk5_2ka.place(x=50, y=220)
        def manajsin_2ka():
            recogabsen.recabsen.manajsi_2ka()
        btn_mk6_2ka = tk.Button(wrapper_mk2ka,text="Manaj.Layanan Sistem Informasi #", width=30, height=2, command=manajsin_2ka)
        btn_mk6_2ka.place(x=50, y=265)
        def sioper_2ka():
            recogabsen.recabsen.siop_2ka()
        btn_mk7_2ka = tk.Button(wrapper_mk2ka,text="Sistem Operasi **", width=30, height=2, command=sioper_2ka)
        btn_mk7_2ka.place(x=50, y=310)
        def mansim_2ka():
            recogabsen.recabsen.sim_2ka()
        btn_mk8_2ka = tk.Button(wrapper_mk2ka,text="Manajemen & SIM 2 *", width=30, height=2, command=mansim_2ka)
        btn_mk8_2ka.place(x=50, y=355)
        def statistika_2ka():
            recogabsen.recabsen.stat_2ka()
        btn_mk9_2ka = tk.Button(wrapper_mk2ka,text="Statistika 2", width=30, height=2, command=statistika_2ka)
        btn_mk9_2ka.place(x=50, y=400)
        def bindon_2ka():
            recogabsen.recabsen.bindo_2ka()
        btn_mk10_2ka = tk.Button(wrapper_mk2ka,text="Bahasa Indonesia 1", width=30, height=2, command=bindon_2ka)
        btn_mk10_2ka.place(x=50, y=445)
        def tekrog_2ka():
            recogabsen.recabsen.pemrog_2ka()
        btn_mk11_2ka = tk.Button(wrapper_mk2ka, text="Teknik Pemrog.Terstruktur 2 **", width=30, height=2, command=tekrog_2ka)
        btn_mk11_2ka.place(x=50, y=490)
        mk2ka.mainloop()

    def mk3ka():
        mk3ka = tk.Tk()
        mk3ka.title("FR SYSTEM")
        mk3ka.geometry("360x650")
        wrapper_mk3ka = LabelFrame(mk3ka, text="mata kuliah")
        wrapper_mk3ka.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ka = tk.Label(wrapper_mk3ka,text="PILIH MATA KULIAH")
        lbl_gmk3ka.place(x=100,y=10)
        # create btn
        def datamin_3ka():
            recogabsen.recabsen.datmin_3ka()
        btn_mk1_3ka = tk.Button(wrapper_mk3ka,text="Konsep Data Mining", width=30, height=2, command=datamin_3ka)
        btn_mk1_3ka.place(x=50, y=40)
        def desmanaj_3ka():
            recogabsen.recabsen.desman_3ka()
        btn_mk2_3ka = tk.Button(wrapper_mk3ka,text="Desain & Manaj.Jaringan Komp.*", width=30, height=2, command=desmanaj_3ka)
        btn_mk2_3ka.place(x=50, y=85)
        def perancangan_3ka():
            recogabsen.recabsen.peranc_3ka()
        btn_mk3_3ka = tk.Button(wrapper_mk3ka,text="Anali.& Peranc.Sistem Inf.*/**", width=30, height=2, command=perancangan_3ka)
        btn_mk3_3ka.place(x=50, y=130)
        def siskeputusan_3ka():
            recogabsen.recabsen.siskep_3ka()
        btn_mk4_3ka = tk.Button(wrapper_mk3ka,text="Sistem Penunjang Keputusan *", width=30, height=2, command=siskeputusan_3ka)
        btn_mk4_3ka.place(x=50, y=175)
        def animasi_3ka():
            recogabsen.recabsen.anim_3ka()
        btn_mk5_3ka = tk.Button(wrapper_mk3ka,text="Pengantar Animasi & Desain Graf #", width=30, height=2, command=animasi_3ka)
        btn_mk5_3ka.place(x=50, y=220)
        def basdat_3ka():
            recogabsen.recabsen.basis_3ka()
        btn_mk6_3ka = tk.Button(wrapper_mk3ka,text="Sistem Basis Data 2 */**", width=30, height=2, command=basdat_3ka)
        btn_mk6_3ka.place(x=50, y=265)
        def kompilasi_3ka():
            recogabsen.recabsen.kompil_3ka()
        btn_mk7_3ka = tk.Button(wrapper_mk3ka,text="Pengantar Teknik Kompilasi", width=30, height=2, command=kompilasi_3ka)
        btn_mk7_3ka.place(x=50, y=310)
        def tegraf_3ka():
            recogabsen.recabsen.graf_3ka()
        btn_mk8_3ka = tk.Button(wrapper_mk3ka,text="Terapan Teori Graf", width=30, height=2, command=tegraf_3ka)
        btn_mk8_3ka.place(x=50, y=355)
        def penah_3ka():
            recogabsen.recabsen.pi_3ka()
        btn_mk9_3ka = tk.Button(wrapper_mk3ka,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=penah_3ka)
        btn_mk9_3ka.place(x=50, y=400)
        mk3ka.mainloop()

    def mk4ka():
        mk4ka = tk.Tk()
        mk4ka.title("FR SYSTEM")
        mk4ka.geometry("360x600")
        wrapper_mk4ka = LabelFrame(mk4ka, text="mata kuliah")
        wrapper_mk4ka.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ka = tk.Label(wrapper_mk4ka,text="PILIH MATA KULIAH")
        lbl_gmk4ka.place(x=100,y=10)
        # create btn
        def bingbisnis_4ka():
            recogabsen.recabsen.bingbis_4ka()
        btn_mk1_4ka = tk.Button(wrapper_mk4ka,text="Bahasa Inggris Bisnis 2 #", width=30, height=2, command=bingbisnis_4ka)
        btn_mk1_4ka.place(x=50, y=40)
        def bistekno_4ka():
            recogabsen.recabsen.bistek_4ka()
        btn_mk2_4ka = tk.Button(wrapper_mk4ka,text="Pengantar Bisnis Teknologi Inf.", width=30, height=2, command=bistekno_4ka)
        btn_mk2_4ka.place(x=50, y=85)
        def sinbank_4ka():
            recogabsen.recabsen.sibank_4ka()
        btn_mk3_4ka = tk.Button(wrapper_mk4ka,text="Sistem Informasi Perbankan", width=30, height=2, command=sinbank_4ka)
        btn_mk3_4ka.place(x=50, y=130)
        def etika_4ka():
            recogabsen.recabsen.etik_4ka()
        btn_mk4_4ka = tk.Button(wrapper_mk4ka,text="Etika & Profesionalisme TSI", width=30, height=2, command=etika_4ka)
        btn_mk4_4ka.place(x=50, y=175)
        def sisdm_4ka():
            recogabsen.recabsen.sdm_4ka()
        btn_mk5_4ka = tk.Button(wrapper_mk4ka,text="Sistem Informasi SDM", width=30, height=2, command=sisdm_4ka)
        btn_mk5_4ka.place(x=50, y=220)
        def sigeo_4ka():
            recogabsen.recabsen.geo_4ka()
        btn_mk6_4ka = tk.Button(wrapper_mk4ka,text="Sistem Informasi Geografis", width=30, height=2, command=sigeo_4ka)
        btn_mk6_4ka.place(x=50, y=265)
        def robotika_4ka():
            recogabsen.recabsen.robot_4ka()
        btn_mk7_4ka = tk.Button(wrapper_mk4ka,text="Robotika Cerdas", width=30, height=2, command=robotika_4ka)
        btn_mk7_4ka.place(x=50, y=310)
        mk4ka.mainloop()

# SISTEM KOMPUTER
    def mk1kb():
        mk1kb = tk.Tk()
        mk1kb.title("FR SYSTEM")
        mk1kb.geometry("360x650")
        wrapper_mk1kb = LabelFrame(mk1kb, text="mata kuliah")
        wrapper_mk1kb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1kb = tk.Label(wrapper_mk1kb,text="PILIH MATA KULIAH")
        lbl_gmk1kb.place(x=100,y=10)
        # create btn
        def kbpai_1kb():
            recogabsen.recabsen.pai_1kb()
        btn_mk1_1kb = tk.Button(wrapper_mk1kb,text="Pendidikan Agama Islam", width=30, height=2, command=kbpai_1kb)
        btn_mk1_1kb.place(x=50, y=40)
        def kbmatdas2A_1kb():
            recogabsen.recabsen.matdas2A_1kb()
        btn_mk2_1kb = tk.Button(wrapper_mk1kb,text="Matematika Dasar 2A", width=30, height=2, command=kbmatdas2A_1kb)
        btn_mk2_1kb.place(x=50, y=85)
        def kbmatdas2B_1kb():
            recogabsen.recabsen.matdas2B_1kb()
        btn_mk3_1kb = tk.Button(wrapper_mk1kb,text="Matematika Dasar 2B", width=30, height=2, command=kbmatdas2B_1kb)
        btn_mk3_1kb.place(x=50, y=130)
        def kbart_1kb():
            recogabsen.recabsen.art_1kb()
        btn_mk4_1kb = tk.Button(wrapper_mk1kb,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=kbart_1kb)
        btn_mk4_1kb.place(x=50, y=175)
        def kbindo_1kb():
            recogabsen.recabsen.bindo_1kb()
        btn_mk5_1kb = tk.Button(wrapper_mk1kb,text="Bahasa Indonesia", width=30, height=2, command=kbindo_1kb)
        btn_mk5_1kb.place(x=50, y=220)
        def kbalgo2A_1kb():
            recogabsen.recabsen.algo2A_1kb()
        btn_mk6_1kb = tk.Button(wrapper_mk1kb,text="Algoritma & Pemrograman 2A", width=30, height=2, command=kbalgo2A_1kb)
        btn_mk6_1kb.place(x=50, y=265)
        def kbalgo2B_1kb():
            recogabsen.recabsen.algo2B_1kb()
        btn_mk7_1kb = tk.Button(wrapper_mk1kb,text="Algoritma & Pemrograman 2B", width=30, height=2, command=kbalgo2B_1kb)
        btn_mk7_1kb.place(x=50, y=310)
        def kbalgo2C_1kb():
            recogabsen.recabsen.algo2C_1kb()
        btn_mk8_1kb = tk.Button(wrapper_mk1kb,text="Algoritma & Pemrograman 2C", width=30, height=2, command=kbalgo2C_1kb)
        btn_mk8_1kb.place(x=50, y=355)
        def kbtele_1kb():
            recogabsen.recabsen.tele_1kb()
        btn_mk9_1kb = tk.Button(wrapper_mk1kb,text="Dasar-dasar Telekomunikasi", width=30, height=2, command=kbtele_1kb)
        btn_mk9_1kb.place(x=50, y=400)
        def kbpanc_1kb():
            recogabsen.recabsen.panc_1kb()
        btn_mk10_1kb = tk.Button(wrapper_mk1kb,text="Pendidikan Pancasila", width=30, height=2, command=kbpanc_1kb)
        btn_mk10_1kb.place(x=50, y=445)
        def kbelek_1kb():
            recogabsen.recabsen.elek_1kb()
        btn_mk11_1kb = tk.Button(wrapper_mk1kb, text="Elektronika Dasar", width=30, height=2, command=kbelek_1kb)
        btn_mk11_1kb.place(x=50, y=490)
        mk1kb.mainloop()
    def mk2kb():
        mk2kb = tk.Tk()
        mk2kb.title("FR SYSTEM")
        mk2kb.geometry("360x650")
        wrapper_mk2kb = LabelFrame(mk2kb, text="mata kuliah")
        wrapper_mk2kb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2kb = tk.Label(wrapper_mk2kb,text="PILIH MATA KULIAH")
        lbl_gmk2kb.place(x=100,y=10)
        # create btn
        def kbomdat_2kb():
            recogabsen.recabsen.komdat_2kb()
        btn_mk1_2kb = tk.Button(wrapper_mk2kb,text="Komputasi Big Data", width=30, height=2, command=kbomdat_2kb)
        btn_mk1_2kb.place(x=50, y=40)
        def kbstatpro_2kb():
            recogabsen.recabsen.statpro_2kb()
        btn_mk2_2kb = tk.Button(wrapper_mk2kb,text="Statistika & Probabilitas Terapan", width=30, height=2, command=kbstatpro_2kb)
        btn_mk2_2kb.place(x=50, y=85)
        def kbdist_2kb():
            recogabsen.recabsen.dist_2kb()
        btn_mk3_2kb = tk.Button(wrapper_mk2kb,text="Sistem Terdistribusi *", width=30, height=2, command=kbdist_2kb)
        btn_mk3_2kb.place(x=50, y=130)
        def kbsinyal_2kb():
            recogabsen.recabsen.sinyal_2kb()
        btn_mk4_2kb = tk.Button(wrapper_mk2kb,text="Pengolahan Sinyal Digital", width=30, height=2, command=kbsinyal_2kb)
        btn_mk4_2kb.place(x=50, y=175)
        def kbjaringan_2kb():
            recogabsen.recabsen.jaringan_2kb()
        btn_mk5_2kb = tk.Button(wrapper_mk2kb,text="Jaringan Komputer Dasar *", width=30, height=2, command=kbjaringan_2kb)
        btn_mk5_2kb.place(x=50, y=220)
        def kbdigital_2kb():
            recogabsen.recabsen.digital_2kb()
        btn_mk6_2kb = tk.Button(wrapper_mk2kb,text="Sistem Digital", width=30, height=2, command=kbdigital_2kb)
        btn_mk6_2kb.place(x=50, y=265)
        def kbingbis_2kb():
            recogabsen.recabsen.bingbis_2kb()
        btn_mk7_2kb = tk.Button(wrapper_mk2kb,text="Bahasa Inggris Bisnis #", width=30, height=2, command=kbingbis_2kb)
        btn_mk7_2kb.place(x=50, y=310)
        def kbmatdisk_2kb():
            recogabsen.recabsen.matdisk_2kb()
        btn_mk8_2kb = tk.Button(wrapper_mk2kb,text="Matematika Diskrit 2", width=30, height=2, command=kbmatdisk_2kb)
        btn_mk8_2kb.place(x=50, y=355)
        def kbmatlan_2kb():
            recogabsen.recabsen.matlan_2kb()
        btn_mk9_2kb = tk.Button(wrapper_mk2kb,text="Matematika Lanjut 2 *", width=30, height=2, command=kbmatlan_2kb)
        btn_mk9_2kb.place(x=50, y=400)
        mk2kb.mainloop()
    def mk3kb():
        mk3kb = tk.Tk()
        mk3kb.title("FR SYSTEM")
        mk3kb.geometry("360x650")
        wrapper_mk3kb = LabelFrame(mk3kb, text="mata kuliah")
        wrapper_mk3kb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3kb = tk.Label(wrapper_mk3kb,text="PILIH MATA KULIAH")
        lbl_gmk3kb.place(x=100,y=10)
        # create btn
        def kbproyek_3kb():
            recogabsen.recabsen.proyek_3kb()
        btn_mk1_3kb = tk.Button(wrapper_mk3kb,text="Proyek Sistem Komputer", width=30, height=2, command=kbproyek_3kb)
        btn_mk1_3kb.place(x=50, y=40)
        def kbiot_3kb():
            recogabsen.recabsen.iot_3kb()
        btn_mk2_3kb = tk.Button(wrapper_mk3kb,text="Internet of Things(IoT)", width=30, height=2, command=kbiot_3kb)
        btn_mk2_3kb.place(x=50, y=85)
        def kbpi_3kb():
            recogabsen.recabsen.pi_3kb()
        btn_mk3_3kb = tk.Button(wrapper_mk3kb,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=kbpi_3kb)
        btn_mk3_3kb.place(x=50, y=130)
        def kbtanam_3kb():
            recogabsen.recabsen.tanam_3kb()
        btn_mk4_3kb = tk.Button(wrapper_mk3kb,text="Sistem Tertanam(Embedded)*", width=30, height=2, command=kbtanam_3kb)
        btn_mk4_3kb.place(x=50, y=175)
        def kbcerdas_3kb():
            recogabsen.recabsen.cerdas_3kb()
        btn_mk5_3kb = tk.Button(wrapper_mk3kb,text="Sistem Cerdas Lanjut", width=30, height=2, command=kbcerdas_3kb)
        btn_mk5_3kb.place(x=50, y=220)
        def kbrobot_3kb():
            recogabsen.recabsen.robot_3kb()
        btn_mk6_3kb = tk.Button(wrapper_mk3kb,text="Robotika Dasar *", width=30, height=2, command=kbrobot_3kb)
        btn_mk6_3kb.place(x=50, y=265)
        def kbperi_3kb():
            recogabsen.recabsen.peri_3kb()
        btn_mk7_3kb = tk.Button(wrapper_mk3kb,text="Pengantarmukaan Periferal Komp.*", width=30, height=2, command=kbperi_3kb)
        btn_mk7_3kb.place(x=50, y=310)
        def kbgraf_3kb():
            recogabsen.recabsen.graf_3kb()
        btn_mk8_3kb = tk.Button(wrapper_mk3kb,text="Terapan Teori Graf", width=30, height=2, command=kbgraf_3kb)
        btn_mk8_3kb.place(x=50, y=355)
        mk3kb.mainloop()
    def mk4kb():
        mk4kb = tk.Tk()
        mk4kb.title("FR SYSTEM")
        mk4kb.geometry("360x650")
        wrapper_mk4kb = LabelFrame(mk4kb, text="mata kuliah")
        wrapper_mk4kb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4kb = tk.Label(wrapper_mk4kb,text="PILIH MATA KULIAH")
        lbl_gmk4kb.place(x=100,y=10)
        # create btn
        def kbsimulasi_4kb():
            recogabsen.recabsen.simulasi_4kb()
        btn_mk1_4kb = tk.Button(wrapper_mk4kb,text="Simulasi & Pemodelan", width=30, height=2, command=kbsimulasi_4kb)
        btn_mk1_4kb.place(x=50, y=40)
        def kbigdat_4kb():
            recogabsen.recabsen.bigdat_4kb()
        btn_mk2_4kb = tk.Button(wrapper_mk4kb,text="Analisis Big Data", width=30, height=2, command=kbigdat_4kb)
        btn_mk2_4kb.place(x=50, y=85)
        def kbdist_4kb():
            recogabsen.recabsen.dist_4kb()
        btn_mk3_4kb = tk.Button(wrapper_mk4kb,text="Sistem Terdistribusi *", width=30, height=2, command=kbdist_4kb)
        btn_mk3_4kb.place(x=50, y=130)
        def kbwira_4kb():
            recogabsen.recabsen.wira_4kb()
        btn_mk4_4kb = tk.Button(wrapper_mk4kb,text="Kewirausahaan Teknologi Informasi", width=30, height=2, command=kbwira_4kb)
        btn_mk4_4kb.place(x=50, y=175)
        def kbcv_4kb():
            recogabsen.recabsen.cv_4kb()
        btn_mk5_4kb = tk.Button(wrapper_mk4kb,text="Computer Vision", width=30, height=2, command=kbcv_4kb)
        btn_mk5_4kb.place(x=50, y=220)
        def kbrobot_4kb():
            recogabsen.recabsen.robot_4kb()
        btn_mk6_4kb = tk.Button(wrapper_mk4kb,text="Robotika Cerdas", width=30, height=2, command=kbrobot_4kb)
        btn_mk6_4kb.place(x=50, y=265)
        def kbubikom_4kb():
            recogabsen.recabsen.ubikom_4kb()
        btn_mk7_4kb = tk.Button(wrapper_mk4kb,text="Pengantar Ubiquitas Computing", width=30, height=2, command=kbubikom_4kb)
        btn_mk7_4kb.place(x=50, y=310)
        def kbwaktu_4kb():
            recogabsen.recabsen.waktu_4kb()
        btn_mk8_4kb = tk.Button(wrapper_mk4kb,text="Sistem Waktu Nyata", width=30, height=2, command=kbwaktu_4kb)
        btn_mk8_4kb.place(x=50, y=355)
        mk4kb.mainloop()

# TEKNIK INDUSTRI
    def mk1id():
        mk1id = tk.Tk()
        mk1id.title("FR SYSTEM")
        mk1id.geometry("360x650")
        wrapper_mk1id = LabelFrame(mk1id, text="mata kuliah")
        wrapper_mk1id.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1id = tk.Label(wrapper_mk1id,text="PILIH MATA KULIAH")
        lbl_gmk1id.place(x=100,y=10)
        # create btn
        def idart_1id():
            recogabsen.recabsen.art_1id()
        btn_mk1_1id = tk.Button(wrapper_mk1id,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=idart_1id)
        btn_mk1_1id.place(x=50, y=40)
        def idmekanik_1id():
            recogabsen.recabsen.mekanik_1id()
        btn_mk2_1id = tk.Button(wrapper_mk1id,text="Mekanika Teknik", width=30, height=2, command=idmekanik_1id)
        btn_mk2_1id.place(x=50, y=85)
        def idbing_1id():
            recogabsen.recabsen.bing_1id()
        btn_mk3_1id = tk.Button(wrapper_mk1id,text="Bahasa Inggris", width=30, height=2, command=idbing_1id)
        btn_mk3_1id.place(x=50, y=130)
        def idprob_1id():
            recogabsen.recabsen.prob_1id()
        btn_mk4_1id = tk.Button(wrapper_mk1id,text="Teori Probabilitas *", width=30, height=2, command=idprob_1id)
        btn_mk4_1id.place(x=50, y=175)
        def idaskom2A_1id():
            recogabsen.recabsen.daskom2A_1id()
        btn_mk5_1id = tk.Button(wrapper_mk1id,text="Dasar Komp.& Pemrograman 2A **", width=30, height=2, command=idaskom2A_1id)
        btn_mk5_1id.place(x=50, y=220)
        def idaskom2B_1id():
            recogabsen.recabsen.daskom2B_1id()
        btn_mk6_1id = tk.Button(wrapper_mk1id,text="Dasar Komp.& Pemrograman 2B **", width=30, height=2, command=idaskom2B_1id)
        btn_mk6_1id.place(x=50, y=265)
        def idpai_1id():
            recogabsen.recabsen.pai_1id()
        btn_mk7_1id = tk.Button(wrapper_mk1id,text="Pendidikan Agama Islam", width=30, height=2, command=idpai_1id)
        btn_mk7_1id.place(x=50, y=310)
        def idfisdas_1id():
            recogabsen.recabsen.fisdas_1id()
        btn_mk8_1id = tk.Button(wrapper_mk1id,text="Fisika Dasar 2 **", width=30, height=2, command=idfisdas_1id)
        btn_mk8_1id.place(x=50, y=355)
        def idkalku2A_1id():
            recogabsen.recabsen.kalku2A_1id()
        btn_mk9_1id = tk.Button(wrapper_mk1id,text="Kalkulus 2A", width=30, height=2, command=idkalku2A_1id)
        btn_mk9_1id.place(x=50, y=400)
        def idkalku2B_1id():
            recogabsen.recabsen.kalku2B_1id()
        btn_mk10_1id = tk.Button(wrapper_mk1id,text="Kalkulus 2B", width=30, height=2, command=idkalku2B_1id)
        btn_mk10_1id.place(x=50, y=445)
        def idsosial_1id():
            recogabsen.recabsen.sosial_1id()
        btn_mk11_1id = tk.Button(wrapper_mk1id, text="Ilmu Sosial Dasar #", width=30, height=2, command=idsosial_1id)
        btn_mk11_1id.place(x=50, y=490)
        mk1id.mainloop()
    def mk2id():
        mk2id = tk.Tk()
        mk2id.title("FR SYSTEM")
        mk2id.geometry("360x550")
        wrapper_mk2id = LabelFrame(mk2id, text="mata kuliah")
        wrapper_mk2id.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2id = tk.Label(wrapper_mk2id,text="PILIH MATA KULIAH")
        lbl_gmk2id.place(x=100,y=10)
        # create btn
        def idkombig_2id():
            recogabsen.recabsen.kombig_2id()
        btn_mk1_2id = tk.Button(wrapper_mk2id,text="Komputasi Big Data", width=30, height=2, command=idkombig_2id)
        btn_mk1_2id.place(x=50, y=40)
        def idkomin_2id():
            recogabsen.recabsen.komin_2id()
        btn_mk2_2id = tk.Button(wrapper_mk2id,text="Komputer Industri 1", width=30, height=2, command=idkomin_2id)
        btn_mk2_2id.place(x=50, y=85)
        def idhukum_2id():
            recogabsen.recabsen.hukum_2id()
        btn_mk3_2id = tk.Button(wrapper_mk2id,text="Hukum Industri #", width=30, height=2, command=idhukum_2id)
        btn_mk3_2id.place(x=50, y=130)
        def idproduk_2id():
            recogabsen.recabsen.produk_2id()
        btn_mk4_2id = tk.Button(wrapper_mk2id,text="Perencanaan & Perancangan Produk *", width=30, height=2, command=idproduk_2id)
        btn_mk4_2id.place(x=50, y=175)
        def idergo_2id():
            recogabsen.recabsen.ergo_2id()
        btn_mk5_2id = tk.Button(wrapper_mk2id,text="Peranc.Sistem Kerja & Ergonomi", width=30, height=2, command=idergo_2id)
        btn_mk5_2id.place(x=50, y=220)
        def idstokastik_2id():
            recogabsen.recabsen.stokastik_2id()
        btn_mk6_2id = tk.Button(wrapper_mk2id,text="Metode Stokastik", width=30, height=2, command=idstokastik_2id)
        btn_mk6_2id.place(x=50, y=265)
        def idkalku_2id():
            recogabsen.recabsen.kalku_2id()
        btn_mk7_2id = tk.Button(wrapper_mk2id,text="Kalkulus 3", width=30, height=2, command=idkalku_2id)
        btn_mk7_2id.place(x=50, y=310)
        def idmanuf_2id():
            recogabsen.recabsen.manuf_2id()
        btn_mk8_2id = tk.Button(wrapper_mk2id,text="Proses Manufaktur */**", width=30, height=2, command=idmanuf_2id)
        btn_mk8_2id.place(x=50, y=355)
        mk2id.mainloop()
    def mk3id():
        mk3id = tk.Tk()
        mk3id.title("FR SYSTEM")
        mk3id.geometry("360x550")
        wrapper_mk3id = LabelFrame(mk3id, text="mata kuliah")
        wrapper_mk3id.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3id = tk.Label(wrapper_mk3id,text="PILIH MATA KULIAH")
        lbl_gmk3id.place(x=100,y=10)
        # create btn
        def idmutu_3id():
            recogabsen.recabsen.mutu_3id()
        btn_mk1_3id = tk.Button(wrapper_mk3id,text="Pengen.& Penjaminan Mutu *", width=30, height=2, command=idmutu_3id)
        btn_mk1_3id.place(x=50, y=40)
        def idekotek_3id():
            recogabsen.recabsen.ekotek_3id()
        btn_mk2_3id = tk.Button(wrapper_mk3id,text="Ekonomi Teknik *", width=30, height=2, command=idekotek_3id)
        btn_mk2_3id.place(x=50, y=85)
        def idpi_3id():
            recogabsen.recabsen.pi_3id()
        btn_mk3_3id = tk.Button(wrapper_mk3id,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=idpi_3id)
        btn_mk3_3id.place(x=50, y=130)
        def idlingkungan_3id():
            recogabsen.recabsen.lingkungan_3id()
        btn_mk4_3id = tk.Button(wrapper_mk3id,text="Pengetahuan Lingkungan #", width=30, height=2, command=idlingkungan_3id)
        btn_mk4_3id.place(x=50, y=175)
        def idsisan_3id():
            recogabsen.recabsen.sisan_3id()
        btn_mk5_3id = tk.Button(wrapper_mk3id,text="Sistem Pendukung Keputusan", width=30, height=2, command=idsisan_3id)
        btn_mk5_3id.place(x=50, y=220)
        def idgraf_3id():
            recogabsen.recabsen.graf_3id()
        btn_mk6_3id = tk.Button(wrapper_mk3id,text="Terapan Teori Graf", width=30, height=2, command=idgraf_3id)
        btn_mk6_3id.place(x=50, y=265)
        def idtataletak_3id():
            recogabsen.recabsen.tataletak_3id()
        btn_mk7_3id = tk.Button(wrapper_mk3id,text="Peranc.Tata Letak Fasilitas *", width=30, height=2, command=idtataletak_3id)
        btn_mk7_3id.place(x=50, y=310)
        def idsispro_3id():
            recogabsen.recabsen.sispro_3id()
        btn_mk8_3id = tk.Button(wrapper_mk3id,text="Sistem Produksi", width=30, height=2, command=idsispro_3id)
        btn_mk8_3id.place(x=50, y=355)
        mk3id.mainloop()
    def mk4id():
        mk4id = tk.Tk()
        mk4id.title("FR SYSTEM")
        mk4id.geometry("360x360")
        wrapper_mk4id = LabelFrame(mk4id, text="mata kuliah")
        wrapper_mk4id.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4id = tk.Label(wrapper_mk4id,text="PILIH MATA KULIAH")
        lbl_gmk4id.place(x=100,y=10)
        # create btn
        def idexperimen_4id():
            recogabsen.recabsen.experimen_4id()
        btn_mk1_4id = tk.Button(wrapper_mk4id,text="Perencanaan Eksperimen", width=30, height=2, command=idexperimen_4id)
        btn_mk1_4id.place(x=50, y=40)
        def idusaha_4id():
            recogabsen.recabsen.usaha_4id()
        btn_mk2_4id = tk.Button(wrapper_mk4id,text="Kewirausahaan #", width=30, height=2, command=idusaha_4id)
        btn_mk2_4id.place(x=50, y=85)
        def idkimia_4id():
            recogabsen.recabsen.kimia_4id()
        btn_mk3_4id = tk.Button(wrapper_mk4id,text="Kimia Lanjut", width=30, height=2, command=idkimia_4id)
        btn_mk3_4id.place(x=50, y=130)
        def idrobot_4id():
            recogabsen.recabsen.robot_4id()
        btn_mk4_4id = tk.Button(wrapper_mk4id,text="Robotika Cerdas", width=30, height=2, command=idrobot_4id)
        btn_mk4_4id.place(x=50, y=175)
        mk4id.mainloop()

# TEKNIK INFORMATIKA
    def mk1ia():
        mk1ia = tk.Tk()
        mk1ia.title("FR SYSTEM")
        mk1ia.geometry("360x750")
        wrapper_mk1ia = LabelFrame(mk1ia, text="mata kuliah")
        wrapper_mk1ia.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ia = tk.Label(wrapper_mk1ia,text="PILIH MATA KULIAH")
        lbl_gmk1ia.place(x=100,y=10)
        # create btn
        def iaktiA_1ia():
            recogabsen.recabsen.ktiA_1ia()
        btn_mk1_1ia = tk.Button(wrapper_mk1ia,text="Konsep Teknologi Informasi A **", width=30, height=2, command=iaktiA_1ia)
        btn_mk1_1ia.place(x=50, y=40)
        def iaktiB_1ia():
            recogabsen.recabsen.ktiB_1ia()
        btn_mk2_1ia = tk.Button(wrapper_mk1ia,text="Konsep Teknologi Informasi B **", width=30, height=2, command=iaktiB_1ia)
        btn_mk2_1ia.place(x=50, y=85)
        def iaktiC_1ia():
            recogabsen.recabsen.ktiC_1ia()
        btn_mk3_1ia = tk.Button(wrapper_mk1ia,text="Konsep Teknologi Informasi C **", width=30, height=2, command=iaktiC_1ia)
        btn_mk3_1ia.place(x=50, y=130)
        def ialgo2A_1ia():
            recogabsen.recabsen.algo2A_1ia()
        btn_mk4_1ia = tk.Button(wrapper_mk1ia,text="Algoritma & Pemrograman 2A *", width=30, height=2, command=ialgo2A_1ia)
        btn_mk4_1ia.place(x=50, y=175)
        def ialgo2B_1ia():
            recogabsen.recabsen.algo2B_1ia()
        btn_mk5_1ia = tk.Button(wrapper_mk1ia,text="Algoritma & Pemrograman 2B *", width=30, height=2, command=ialgo2B_1ia)
        btn_mk5_1ia.place(x=50, y=220)
        def ialgo2C_1ia():
            recogabsen.recabsen.algo2C_1ia()
        btn_mk6_1ia = tk.Button(wrapper_mk1ia,text="Algoritma & Pemrograman 2C *", width=30, height=2, command=ialgo2C_1ia)
        btn_mk6_1ia.place(x=50, y=265)
        def ialegal_1ia():
            recogabsen.recabsen.legal_1ia()
        btn_mk7_1ia = tk.Button(wrapper_mk1ia,text="Legal Aspek TIK", width=30, height=2, command=ialegal_1ia)
        btn_mk7_1ia.place(x=50, y=310)
        def iart_1ia():
            recogabsen.recabsen.art_1ia()
        btn_mk8_1ia = tk.Button(wrapper_mk1ia,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=iart_1ia)
        btn_mk8_1ia.place(x=50, y=355)
        def fiskimA_1ia():
            recogabsen.recabsen.fiskimA_1ia()
        btn_mk9_1ia = tk.Button(wrapper_mk1ia,text="Fisika & Kimia Dasar 2A", width=30, height=2, command=fiskimA_1ia)
        btn_mk9_1ia.place(x=50, y=400)
        def fiskimB_1ia():
            recogabsen.recabsen.fiskimB_1ia()
        btn_mk10_1ia = tk.Button(wrapper_mk1ia,text="Fisika & Kimia Dasar 2B", width=30, height=2, command=fiskimB_1ia)
        btn_mk10_1ia.place(x=50, y=445)
        def bing_1ia():
            recogabsen.recabsen.bing_1ia()
        btn_mk11_1ia = tk.Button(wrapper_mk1ia, text="Bahasa Inggris 2", width=30, height=2, command=bing_1ia)
        btn_mk11_1ia.place(x=50, y=490)
        def iapanc_1ia():
            recogabsen.recabsen.panc_1ia()
        btn_mk12_1ia = tk.Button(wrapper_mk1ia, text="Pendidikan Pancasila *", width=30, height=2, command=iapanc_1ia)
        btn_mk12_1ia.place(x=50, y=535)
        def iamatif_1ia():
            recogabsen.recabsen.matif_1ia()
        btn_mk13_1ia = tk.Button(wrapper_mk1ia, text="Matematika Informatika 2 **", width=30, height=2, command=iamatif_1ia)
        btn_mk13_1ia.place(x=50, y=580)
        def iamatdas_1ia():
            recogabsen.recabsen.matdas_1ia()
        btn_mk14_1ia = tk.Button(wrapper_mk1ia, text="Matematika Dasar 2 *", width=30, height=2, command=iamatdas_1ia)
        btn_mk14_1ia.place(x=50, y=625)
        mk1ia.mainloop()

    def mk2ia():
        mk2ia = tk.Tk()
        mk2ia.title("FR SYSTEM")
        mk2ia.geometry("360x750")
        wrapper_mk2ia = LabelFrame(mk2ia, text="mata kuliah")
        wrapper_mk2ia.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ia = tk.Label(wrapper_mk2ia,text="PILIH MATA KULIAH")
        lbl_gmk2ia.place(x=100,y=10)
        # create btn
        def iabigdat_2ia():
            recogabsen.recabsen.bigdat_2ia()
        btn_mk1_2ia = tk.Button(wrapper_mk2ia,text="Komputasi Big Data", width=30, height=2, command=iabigdat_2ia)
        btn_mk1_2ia.place(x=50, y=40)
        def iamatlan_2ia():
            recogabsen.recabsen.matlan_2ia()
        btn_mk2_2ia = tk.Button(wrapper_mk2ia,text="Matematika Lanjut 2", width=30, height=2, command=iamatlan_2ia)
        btn_mk2_2ia.place(x=50, y=85)
        def iamatif_2ia():
            recogabsen.recabsen.matif_2ia()
        btn_mk3_2ia = tk.Button(wrapper_mk2ia,text="Matematika Informatika 4 *", width=30, height=2, command=iamatif_2ia)
        btn_mk3_2ia.place(x=50, y=130)
        def ialegal_2ia():
            recogabsen.recabsen.legal_2ia()
        btn_mk4_2ia = tk.Button(wrapper_mk2ia,text="Legal Aspek Produk TIK", width=30, height=2, command=ialegal_2ia)
        btn_mk4_2ia.place(x=50, y=175)
        def iaweb_2ia():
            recogabsen.recabsen.web_2ia()
        btn_mk5_2ia = tk.Button(wrapper_mk2ia,text="Pengantar Web Science #", width=30, height=2, command=iaweb_2ia)
        btn_mk5_2ia.place(x=50, y=220)
        def iasim_2ia():
            recogabsen.recabsen.sim_2ia()
        btn_mk6_2ia = tk.Button(wrapper_mk2ia,text="Sistem Informasi Manajemen", width=30, height=2, command=iasim_2ia)
        btn_mk6_2ia.place(x=50, y=265)
        def ianfokes_2ia():
            recogabsen.recabsen.infokes_2ia()
        btn_mk7_2ia = tk.Button(wrapper_mk2ia,text="Informatika Kesehatan", width=30, height=2, command=ianfokes_2ia)
        btn_mk7_2ia.place(x=50, y=310)
        def iastat_2ia():
            recogabsen.recabsen.stat_2ia()
        btn_mk8_2ia = tk.Button(wrapper_mk2ia,text="Statistika 2 **", width=30, height=2, command=iastat_2ia)
        btn_mk8_2ia.place(x=50, y=355)
        def iapbo_2ia():
            recogabsen.recabsen.pbo_2ia()
        btn_mk9_2ia = tk.Button(wrapper_mk2ia,text="Pemrograman Berbasis Obyek **", width=30, height=2, command=iapbo_2ia)
        btn_mk9_2ia.place(x=50, y=400)
        def iarsikom_2ia():
            recogabsen.recabsen.arsikom_2ia()
        btn_mk10_2ia = tk.Button(wrapper_mk2ia,text="Arsitektur Komputer *", width=30, height=2, command=iarsikom_2ia)
        btn_mk10_2ia.place(x=50, y=445)
        def iaberkas_2ia():
            recogabsen.recabsen.berkas_2ia()
        btn_mk11_2ia = tk.Button(wrapper_mk2ia, text="Sistem Berkas *", width=30, height=2, command=iaberkas_2ia)
        btn_mk11_2ia.place(x=50, y=490)
        mk2ia.mainloop()

    def mk3ia():
        mk3ia = tk.Tk()
        mk3ia.title("FR SYSTEM")
        mk3ia.geometry("360x540")
        wrapper_mk3ia = LabelFrame(mk3ia, text="mata kuliah")
        wrapper_mk3ia.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ia = tk.Label(wrapper_mk3ia,text="PILIH MATA KULIAH")
        lbl_gmk3ia.place(x=100,y=10)
        # create btn
        def iatbo_3ia():
            recogabsen.recabsen.tbo_3ia()
        btn_mk1_3ia = tk.Button(wrapper_mk3ia,text="Teori Bahasa dan Otomata */**", width=30, height=2, command=iatbo_3ia)
        btn_mk1_3ia.place(x=50, y=40)
        def iarekom_3ia():
            recogabsen.recabsen.rekom_3ia()
        btn_mk2_3ia = tk.Button(wrapper_mk3ia,text="Rekayasa Komputasional **", width=30, height=2, command=iarekom_3ia)
        btn_mk2_3ia.place(x=50, y=85)
        def iadesain_3ia():
            recogabsen.recabsen.desain_3ia()
        btn_mk3_3ia = tk.Button(wrapper_mk3ia,text="Desain Pemodelan Grafik #", width=30, height=2, command=iadesain_3ia)
        btn_mk3_3ia.place(x=50, y=130)
        def iagrafkom_3ia():
            recogabsen.recabsen.grafkom_3ia()
        btn_mk4_3ia = tk.Button(wrapper_mk3ia,text="Grafik Komputer 2 **", width=30, height=2, command=iagrafkom_3ia)
        btn_mk4_3ia.place(x=50, y=175)
        def iamk_3ia():
            recogabsen.recabsen.imk_3ia()
        btn_mk5_3ia = tk.Button(wrapper_mk3ia,text="Interaksi Manusia & Komputer */**", width=30, height=2, command=iamk_3ia)
        btn_mk5_3ia.place(x=50, y=220)
        def iabasis_3ia():
            recogabsen.recabsen.basis_3ia()
        btn_mk6_3ia = tk.Button(wrapper_mk3ia,text="Sistem Basis Data 2 */**", width=30, height=2, command=iabasis_3ia)
        btn_mk6_3ia.place(x=50, y=265)
        def iagraf_3ia():
            recogabsen.recabsen.graf_3ia()
        btn_mk7_3ia = tk.Button(wrapper_mk3ia,text="Terapan Teori Graf", width=30, height=2, command=iagraf_3ia)
        btn_mk7_3ia.place(x=50, y=310)
        def iaskk_3ia():
            recogabsen.recabsen.skk_3ia()
        btn_mk8_3ia = tk.Button(wrapper_mk3ia,text="Sistem Keamanan Komputer", width=30, height=2, command=iaskk_3ia)
        btn_mk8_3ia.place(x=50, y=355)
        def iapi_3ia():
            recogabsen.recabsen.pi_3ia()
        btn_mk9_3ia = tk.Button(wrapper_mk3ia,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=iapi_3ia)
        btn_mk9_3ia.place(x=50, y=400)
        def iagame_3ia():
            recogabsen.recabsen.game_3ia()
        btn_mk10_3ia = tk.Button(wrapper_mk3ia,text="Teknologi Game #", width=30, height=2, command=iagame_3ia)
        btn_mk10_3ia.place(x=50, y=445)
        mk3ia.mainloop()

    def mk4ia():
        mk4ia = tk.Tk()
        mk4ia.title("FR SYSTEM")
        mk4ia.geometry("360x700")
        wrapper_mk4ia = LabelFrame(mk4ia, text="mata kuliah")
        wrapper_mk4ia.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ia = tk.Label(wrapper_mk4ia,text="PILIH MATA KULIAH")
        lbl_gmk4ia.place(x=100,y=10)
        # create btn
        def iadist_4ia():
            recogabsen.recabsen.dist_4ia()
        btn_mk1_4ia = tk.Button(wrapper_mk4ia,text="Sistem Terdistribusi", width=30, height=2, command=iadist_4ia)
        btn_mk1_4ia.place(x=50, y=40)
        def iamult_4ia():
            recogabsen.recabsen.mult_4ia()
        btn_mk2_4ia = tk.Button(wrapper_mk4ia,text="Sistem Multimedia **", width=30, height=2, command=iamult_4ia)
        btn_mk2_4ia.place(x=50, y=85)
        def iadamin_4ia():
            recogabsen.recabsen.damin_4ia()
        btn_mk3_4ia = tk.Button(wrapper_mk4ia,text="Konsep Data Mining", width=30, height=2, command=iadamin_4ia)
        btn_mk3_4ia.place(x=50, y=130)
        def iarpl_4ia():
            recogabsen.recabsen.rpl_4ia()
        btn_mk4_4ia = tk.Button(wrapper_mk4ia,text="Rekayasa Perangkat Lunak 2 */**", width=30, height=2, command=iarpl_4ia)
        btn_mk4_4ia.place(x=50, y=175)
        def iabingbis_4ia():
            recogabsen.recabsen.bingbis_4ia()
        btn_mk5_4ia = tk.Button(wrapper_mk4ia,text="Bahasa Inggris Bisnis 2", width=30, height=2, command=iabingbis_4ia)
        btn_mk5_4ia.place(x=50, y=220)
        def iajaringan_4ia():
            recogabsen.recabsen.jaringan_4ia()
        btn_mk6_4ia = tk.Button(wrapper_mk4ia,text="Pemrograman Jaringan **", width=30, height=2, command=iajaringan_4ia)
        btn_mk6_4ia.place(x=50, y=265)
        def iapplA_4ia():
            recogabsen.recabsen.pplA_4ia()
        btn_mk7_4ia = tk.Button(wrapper_mk4ia,text="Pengel. Proyek Perangkat Lunak A", width=30, height=2, command=iapplA_4ia)
        btn_mk7_4ia.place(x=50, y=310)
        def iapplB_4ia():
            recogabsen.recabsen.pplB_4ia()
        btn_mk8_4ia = tk.Button(wrapper_mk4ia,text="Pengel. Proyek Perangkat Lunak B", width=30, height=2, command=iapplB_4ia)
        btn_mk8_4ia.place(x=50, y=355)
        def iakomo_4ia():
            recogabsen.recabsen.komo_4ia()
        btn_mk9_4ia = tk.Button(wrapper_mk4ia,text="Komputasi Modern #", width=30, height=2, command=iakomo_4ia)
        btn_mk9_4ia.place(x=50, y=400)
        def iarobot_4ia():
            recogabsen.recabsen.robot_4ia()
        btn_mk10_4ia = tk.Button(wrapper_mk4ia,text="Robotika Cerdas", width=30, height=2, command=iarobot_4ia)
        btn_mk10_4ia.place(x=50, y=445)
        def iapemulti_4ia():
            recogabsen.recabsen.pemulti_4ia()
        btn_mk11_4ia = tk.Button(wrapper_mk4ia, text="Pemrograman Multimedia", width=30, height=2, command=iapemulti_4ia)
        btn_mk11_4ia.place(x=50, y=490)
        def iadeep_4ia():
            recogabsen.recabsen.deep_4ia()
        btn_mk12_4ia = tk.Button(wrapper_mk4ia, text="Algoritma Deep Learning", width=30, height=2, command=iadeep_4ia)
        btn_mk12_4ia.place(x=50, y=535)
        mk4ia.mainloop()

# TEKNIK MESIN
    def mk1ic():
        mk1ic = tk.Tk()
        mk1ic.title("FR SYSTEM")
        mk1ic.geometry("360x700")
        wrapper_mk1ic = LabelFrame(mk1ic, text="mata kuliah")
        wrapper_mk1ic.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ic = tk.Label(wrapper_mk1ic,text="PILIH MATA KULIAH")
        lbl_gmk1ic.place(x=100,y=10)
        # create btn
        def icart_1ic():
            recogabsen.recabsen.art_1ic()
        btn_mk1_1ic = tk.Button(wrapper_mk1ic,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=icart_1ic)
        btn_mk1_1ic.place(x=50, y=40)
        def icdaskomA_1ic():
            recogabsen.recabsen.daskomA_1ic()
        btn_mk2_1ic = tk.Button(wrapper_mk1ic,text="Dasar Komputer & Pemrog.2A", width=30, height=2, command=icdaskomA_1ic)
        btn_mk2_1ic.place(x=50, y=85)
        def icdaskomB_1ic():
            recogabsen.recabsen.daskomB_1ic()
        btn_mk3_1ic = tk.Button(wrapper_mk1ic,text="Dasar Komputer & Pemrog.2B", width=30, height=2, command=icdaskomB_1ic)
        btn_mk3_1ic.place(x=50, y=130)
        def ickalkuA_1ic():
            recogabsen.recabsen.kalkuA_1ic()
        btn_mk4_1ic = tk.Button(wrapper_mk1ic,text="Kalkulus 2A", width=30, height=2, command=ickalkuA_1ic)
        btn_mk4_1ic.place(x=50, y=175)
        def ickalkuB_1ic():
            recogabsen.recabsen.kalkuB_1ic()
        btn_mk5_1ic = tk.Button(wrapper_mk1ic,text="Kalkulus 2B", width=30, height=2, command=ickalkuB_1ic)
        btn_mk5_1ic.place(x=50, y=220)
        def icfiskimA_1ic():
            recogabsen.recabsen.fiskimA_1ic()
        btn_mk6_1ic = tk.Button(wrapper_mk1ic,text="Fisika & Kimia Dasar 2A", width=30, height=2, command=icfiskimA_1ic)
        btn_mk6_1ic.place(x=50, y=265)
        def icfiskimB_1ic():
            recogabsen.recabsen.fiskimB_1ic()
        btn_mk7_1ic = tk.Button(wrapper_mk1ic,text="Fisika & Kimia Dasar 2B", width=30, height=2, command=icfiskimB_1ic)
        btn_mk7_1ic.place(x=50, y=310)
        def icbudaya_1ic():
            recogabsen.recabsen.budaya_1ic()
        btn_mk8_1ic = tk.Button(wrapper_mk1ic,text="Ilmu Budaya Dasar #", width=30, height=2, command=icbudaya_1ic)
        btn_mk8_1ic.place(x=50, y=355)
        def icgambar_1ic():
            recogabsen.recabsen.gambar_1ic()
        btn_mk9_1ic = tk.Button(wrapper_mk1ic,text="Menggambar Mesin *", width=30, height=2, command=icgambar_1ic)
        btn_mk9_1ic.place(x=50, y=400)
        def icproduksi_1ic():
            recogabsen.recabsen.produksi_1ic()
        btn_mk10_1ic = tk.Button(wrapper_mk1ic,text="Proses Produksi 2", width=30, height=2, command=icproduksi_1ic)
        btn_mk10_1ic.place(x=50, y=445)
        def icbing_1ic():
            recogabsen.recabsen.bing_1ic()
        btn_mk11_1ic = tk.Button(wrapper_mk1ic, text="Bahasa Inggris 2", width=30, height=2, command=icbing_1ic)
        btn_mk11_1ic.place(x=50, y=490)
        def icbindo_1ic():
            recogabsen.recabsen.bindo_1ic()
        btn_mk12_1ic = tk.Button(wrapper_mk1ic, text="Bahasa Indonesia 2", width=30, height=2, command=icbindo_1ic)
        btn_mk12_1ic.place(x=50, y=535)
        def icekomanaj_1ic():
            recogabsen.recabsen.ekomanaj_1ic()
        btn_mk13_1ic = tk.Button(wrapper_mk1ic, text="Pengantar Ekonomi & Manaj. 2", width=30, height=2, command=icekomanaj_1ic)
        btn_mk13_1ic.place(x=50, y=580)
        mk1ic.mainloop()
    def mk2ic():
        mk2ic = tk.Tk()
        mk2ic.title("FR SYSTEM")
        mk2ic.geometry("360x600")
        wrapper_mk2ic = LabelFrame(mk2ic, text="mata kuliah")
        wrapper_mk2ic.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ic = tk.Label(wrapper_mk2ic,text="PILIH MATA KULIAH")
        lbl_gmk2ic.place(x=100,y=10)
        # create btn
        def ickombig_2ic():
            recogabsen.recabsen.kombig_2ic()
        btn_mk1_2ic = tk.Button(wrapper_mk2ic,text="Komputasi Big Data", width=30, height=2, command=ickombig_2ic)
        btn_mk1_2ic.place(x=50, y=40)
        def ickalku_2ic():
            recogabsen.recabsen.kalku_2ic()
        btn_mk2_2ic = tk.Button(wrapper_mk2ic,text="Kalkulus 4", width=30, height=2, command=ickalku_2ic)
        btn_mk2_2ic.place(x=50, y=85)
        def icmateknik_2ic():
            recogabsen.recabsen.mateknik_2ic()
        btn_mk3_2ic = tk.Button(wrapper_mk2ic,text="Matematika Teknik 2", width=30, height=2, command=icmateknik_2ic)
        btn_mk3_2ic.place(x=50, y=130)
        def icelmesin_2ic():
            recogabsen.recabsen.elmesin_2ic()
        btn_mk4_2ic = tk.Button(wrapper_mk2ic,text="Tugas Perencanaan Elemen Mesin 1", width=30, height=2, command=icelmesin_2ic)
        btn_mk4_2ic.place(x=50, y=175)
        def icmaterial_2ic():
            recogabsen.recabsen.material_2ic()
        btn_mk5_2ic = tk.Button(wrapper_mk2ic,text="Teknik Pembentukan Material", width=30, height=2, command=icmaterial_2ic)
        btn_mk5_2ic.place(x=50, y=220)
        def icelemen_2ic():
            recogabsen.recabsen.elemen_2ic()
        btn_mk6_2ic = tk.Button(wrapper_mk2ic,text="Elemen Mesin 1 *", width=30, height=2, command=icelemen_2ic)
        btn_mk6_2ic.place(x=50, y=265)
        def icfisdas_2ic():
            recogabsen.recabsen.fisdas_2ic()
        btn_mk7_2ic = tk.Button(wrapper_mk2ic,text="Fisika Dasar 4", width=30, height=2, command=icfisdas_2ic)
        btn_mk7_2ic.place(x=50, y=310)
        def icbahan_2ic():
            recogabsen.recabsen.bahan_2ic()
        btn_mk8_2ic = tk.Button(wrapper_mk2ic,text="Pemilihan Bahan & Proses *", width=30, height=2, command=icbahan_2ic)
        btn_mk8_2ic.place(x=50, y=355)
        def icpkn_2ic():
            recogabsen.recabsen.pkn_2ic()
        btn_mk9_2ic = tk.Button(wrapper_mk2ic,text="Pendidikan Kewarganegaraan #", width=30, height=2, command=icpkn_2ic)
        btn_mk9_2ic.place(x=50, y=400)
        def ickanima_2ic():
            recogabsen.recabsen.kanima_2ic()
        btn_mk10_2ic = tk.Button(wrapper_mk2ic,text="Mekanika Kekuatan Material", width=30, height=2, command=ickanima_2ic)
        btn_mk10_2ic.place(x=50, y=445)
        def ickamass_2ic():
            recogabsen.recabsen.kamass_2ic()
        btn_mk11_2ic = tk.Button(wrapper_mk2ic, text="Perpindahan Kalor & Massa", width=30, height=2, command=ickamass_2ic)
        btn_mk11_2ic.place(x=50, y=490)
        mk2ic.mainloop()
    def mk3ic():
        mk3ic = tk.Tk()
        mk3ic.title("FR SYSTEM")
        mk3ic.geometry("360x540")
        wrapper_mk3ic = LabelFrame(mk3ic, text="mata kuliah")
        wrapper_mk3ic.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ic = tk.Label(wrapper_mk3ic,text="PILIH MATA KULIAH")
        lbl_gmk3ic.place(x=100,y=10)
        # create btn
        def icstatek_3ic():
            recogabsen.recabsen.statek_3ic()
        btn_mk1_3ic = tk.Button(wrapper_mk3ic,text="Statistik Teknik", width=30, height=2, command=icstatek_3ic)
        btn_mk1_3ic.place(x=50, y=40)
        def icenergi_3ic():
            recogabsen.recabsen.energi_3ic()
        btn_mk2_3ic = tk.Button(wrapper_mk3ic,text="Energi Alternatif & Terbarukan", width=30, height=2, command=icenergi_3ic)
        btn_mk2_3ic.place(x=50, y=85)
        def icpi_3ic():
            recogabsen.recabsen.pi_3ic()
        btn_mk3_3ic = tk.Button(wrapper_mk3ic,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=icpi_3ic)
        btn_mk3_3ic.place(x=50, y=130)
        def icmekatronika_3ic():
            recogabsen.recabsen.mekatronika_3ic()
        btn_mk4_3ic = tk.Button(wrapper_mk3ic,text="Mekatronika", width=30, height=2, command=icmekatronika_3ic)
        btn_mk4_3ic.place(x=50, y=175)
        def icwirausaha_3ic():
            recogabsen.recabsen.wirausaha_3ic()
        btn_mk5_3ic = tk.Button(wrapper_mk3ic,text="Kewirausahaan", width=30, height=2, command=icwirausaha_3ic)
        btn_mk5_3ic.place(x=50, y=220)
        def ickonversi_3ic():
            recogabsen.recabsen.konversi_3ic()
        btn_mk6_3ic = tk.Button(wrapper_mk3ic,text="Mesin Konversi Energi *", width=30, height=2, command=ickonversi_3ic)
        btn_mk6_3ic.place(x=50, y=265)
        def icperanc_3ic():
            recogabsen.recabsen.peranc_3ic()
        btn_mk7_3ic = tk.Button(wrapper_mk3ic,text="Tugas Peranc.Elemen Mesin 3", width=30, height=2, command=icperanc_3ic)
        btn_mk7_3ic.place(x=50, y=310)
        def icelemen_3ic():
            recogabsen.recabsen.elemen_3ic()
        btn_mk8_3ic = tk.Button(wrapper_mk3ic,text="Elemen Mesin 3 *", width=30, height=2, command=icelemen_3ic)
        btn_mk8_3ic.place(x=50, y=355)
        def icnumeric_3ic():
            recogabsen.recabsen.numeric_3ic()
        btn_mk9_3ic = tk.Button(wrapper_mk3ic,text="Komputer Numerical Control(CNC)", width=30, height=2, command=icnumeric_3ic)
        btn_mk9_3ic.place(x=50, y=400)
        def icgraf_3ic():
            recogabsen.recabsen.graf_3ic()
        btn_mk10_3ic = tk.Button(wrapper_mk3ic,text="Terapan Teori Graf", width=30, height=2, command=icgraf_3ic)
        btn_mk10_3ic.place(x=50, y=445)
        mk3ic.mainloop()
    def mk4ic():
        mk4ic = tk.Tk()
        mk4ic.title("FR SYSTEM")
        mk4ic.geometry("360x360")
        wrapper_mk4ic = LabelFrame(mk4ic, text="mata kuliah")
        wrapper_mk4ic.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ic = tk.Label(wrapper_mk4ic,text="PILIH MATA KULIAH")
        lbl_gmk4ic.place(x=100,y=10)
        # create btn
        def icamdal_4ic():
            recogabsen.recabsen.amdal_4ic()
        btn_mk1_4ic = tk.Button(wrapper_mk4ic,text="Teknik Lingkungan & AMDAL", width=30, height=2, command=icamdal_4ic)
        btn_mk1_4ic.place(x=50, y=40)
        def icetika_4ic():
            recogabsen.recabsen.etika_4ic()
        btn_mk2_4ic = tk.Button(wrapper_mk4ic,text="Etika Profesi #", width=30, height=2, command=icetika_4ic)
        btn_mk2_4ic.place(x=50, y=85)
        def icaudit_4ic():
            recogabsen.recabsen.audit_4ic()
        btn_mk3_4ic = tk.Button(wrapper_mk4ic,text="Audit Energi", width=30, height=2, command=icaudit_4ic)
        btn_mk3_4ic.place(x=50, y=130)
        def icrawat_4ic():
            recogabsen.recabsen.rawat_4ic()
        btn_mk4_4ic = tk.Button(wrapper_mk4ic,text="Teknik Perawatan Mesin", width=30, height=2, command=icrawat_4ic)
        btn_mk4_4ic.place(x=50, y=175)
        def icaero_4ic():
            recogabsen.recabsen.aero_4ic()
        btn_mk5_4ic = tk.Button(wrapper_mk4ic,text="Aerodinamika", width=30, height=2, command=icaero_4ic)
        btn_mk5_4ic.place(x=50, y=220)
        def icrobot_4ic():
            recogabsen.recabsen.robot_4ic()
        btn_mk6_4ic = tk.Button(wrapper_mk4ic,text="Robotika Cerdas", width=30, height=2, command=icrobot_4ic)
        btn_mk6_4ic.place(x=50, y=265)
        mk4ic.mainloop()

# TEKNIK ELEKTRO
    def mk1ib():
        mk1ib = tk.Tk()
        mk1ib.title("FR SYSTEM")
        mk1ib.geometry("360x700")
        wrapper_mk1ib = LabelFrame(mk1ib, text="mata kuliah")
        wrapper_mk1ib.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ib = tk.Label(wrapper_mk1ib,text="PILIH MATA KULIAH")
        lbl_gmk1ib.place(x=100,y=10)
        # create btn
        def ibralo_1ib():
            recogabsen.recabsen.ralo_1ib()
        btn_mk1_1ib = tk.Button(wrapper_mk1ib,text="Rangkaian Logika *", width=30, height=2, command=ibralo_1ib)
        btn_mk1_1ib.place(x=50, y=40)
        def ibelektrik_1ib():
            recogabsen.recabsen.elektrik_1ib()
        btn_mk2_1ib = tk.Button(wrapper_mk1ib,text="Rangkaian Elektrik 2", width=30, height=2, command=ibelektrik_1ib)
        btn_mk2_1ib.place(x=50, y=85)
        def ibart_1ib():
            recogabsen.recabsen.art_1ib()
        btn_mk3_1ib = tk.Button(wrapper_mk1ib,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=ibart_1ib)
        btn_mk3_1ib.place(x=50, y=130)
        def ibkompA_1ib():
            recogabsen.recabsen.kompA_1ib()
        btn_mk4_1ib = tk.Button(wrapper_mk1ib,text="Dasar Komputer & Pemrog.2A", width=30, height=2, command=ibkompA_1ib)
        btn_mk4_1ib.place(x=50, y=175)
        def ibkompB_1ib():
            recogabsen.recabsen.kompB_1ib()
        btn_mk5_1ib = tk.Button(wrapper_mk1ib,text="Dasar Komputer & Pemrog.2B", width=30, height=2, command=ibkompB_1ib)
        btn_mk5_1ib.place(x=50, y=220)
        def ibfiskimA_1ib():
            recogabsen.recabsen.fiskimA_1ib()
        btn_mk6_1ib = tk.Button(wrapper_mk1ib,text="Fisika & Kimia 2A", width=30, height=2, command=ibfiskimA_1ib)
        btn_mk6_1ib.place(x=50, y=265)
        def ibfiskimB_1ib():
            recogabsen.recabsen.fiskimB_1ib()
        btn_mk7_1ib = tk.Button(wrapper_mk1ib,text="Fisika & Kimia 2B", width=30, height=2, command=ibfiskimB_1ib)
        btn_mk7_1ib.place(x=50, y=310)
        def ibkalkuA_1ib():
            recogabsen.recabsen.kalkuA_1ib()
        btn_mk8_1ib = tk.Button(wrapper_mk1ib,text="Kalkulus 2A", width=30, height=2, command=ibkalkuA_1ib)
        btn_mk8_1ib.place(x=50, y=355)
        def ibkalkuB_1ib():
            recogabsen.recabsen.kalkuB_1ib()
        btn_mk9_1ib = tk.Button(wrapper_mk1ib,text="Kalkulus 2B", width=30, height=2, command=ibkalkuB_1ib)
        btn_mk9_1ib.place(x=50, y=400)
        def iblogR_1ib():
            recogabsen.recabsen.logR_1ib()
        btn_mk10_1ib = tk.Button(wrapper_mk1ib,text="Rangkaian Logika */R", width=30, height=2, command=iblogR_1ib)
        btn_mk10_1ib.place(x=50, y=445)
        def ibelek2R_1ib():
            recogabsen.recabsen.elek2R_1ib()
        btn_mk11_1ib = tk.Button(wrapper_mk1ib, text="Rangkaian Elektrik 2/R", width=30, height=2, command=ibelek2R_1ib)
        btn_mk11_1ib.place(x=50, y=490)
        def ibmateknik_1ib():
            recogabsen.recabsen.mateknik_1ib()
        btn_mk12_1ib = tk.Button(wrapper_mk1ib, text="Matemaika Teknik 2", width=30, height=2, command=ibmateknik_1ib)
        btn_mk12_1ib.place(x=50, y=535)
        def ibtele_1ib():
            recogabsen.recabsen.tele_1ib()
        btn_mk13_1ib = tk.Button(wrapper_mk1ib, text="Dasar Telekomunikasi", width=30, height=2, command=ibtele_1ib)
        btn_mk13_1ib.place(x=50, y=580)
        mk1ib.mainloop()
    def mk2ib():
        mk2ib = tk.Tk()
        mk2ib.title("FR SYSTEM")
        mk2ib.geometry("360x540")
        wrapper_mk2ib = LabelFrame(mk2ib, text="mata kuliah")
        wrapper_mk2ib.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ib = tk.Label(wrapper_mk2ib,text="PILIH MATA KULIAH")
        lbl_gmk2ib.place(x=100,y=10)
        # create btn
        def ibkombig_2ib():
            recogabsen.recabsen.kombig_2ib()
        btn_mk1_2ib = tk.Button(wrapper_mk2ib,text="Komputasi Big Data", width=30, height=2, command=ibkombig_2ib)
        btn_mk1_2ib.place(x=50, y=40)
        def ibfisika_2ib():
            recogabsen.recabsen.fisika_2ib()
        btn_mk2_2ib = tk.Button(wrapper_mk2ib,text="Fisika 4 *", width=30, height=2, command=ibfisika_2ib)
        btn_mk2_2ib.place(x=50, y=85)
        def ibelek_2ib():
            recogabsen.recabsen.elek_2ib()
        btn_mk3_2ib = tk.Button(wrapper_mk2ib,text="Dasar Tenaga Elektrik **", width=30, height=2, command=ibelek_2ib)
        btn_mk3_2ib.place(x=50, y=130)
        def ibmikro_2ib():
            recogabsen.recabsen.mikro_2ib()
        btn_mk4_2ib = tk.Button(wrapper_mk2ib,text="Teknik Mikroprosesor *", width=30, height=2, command=ibmikro_2ib)
        btn_mk4_2ib.place(x=50, y=175)
        def ibstatpro_2ib():
            recogabsen.recabsen.statpro_2ib()
        btn_mk5_2ib = tk.Button(wrapper_mk2ib,text="Statistika & Probabilitas", width=30, height=2, command=ibstatpro_2ib)
        btn_mk5_2ib.place(x=50, y=220)
        def ibkalku_2ib():
            recogabsen.recabsen.kalku_2ib()
        btn_mk6_2ib = tk.Button(wrapper_mk2ib,text="Kalkulus 4 *", width=30, height=2, command=ibkalku_2ib)
        btn_mk6_2ib.place(x=50, y=265)
        def ibpkn_2ib():
            recogabsen.recabsen.pkn_2ib()
        btn_mk7_2ib = tk.Button(wrapper_mk2ib,text="Pendidikan Kewarganegaraan #", width=30, height=2, command=ibpkn_2ib)
        btn_mk7_2ib.place(x=50, y=310)
        def ibesel_2ib():
            recogabsen.recabsen.besel_2ib()
        btn_mk8_2ib = tk.Button(wrapper_mk2ib,text="Pengukuran Besaran Elektrik", width=30, height=2, command=ibesel_2ib)
        btn_mk8_2ib.place(x=50, y=355)
        def ibmedan_2ib():
            recogabsen.recabsen.medan_2ib()
        btn_mk9_2ib = tk.Button(wrapper_mk2ib,text="Teori Medan", width=30, height=2, command=ibmedan_2ib)
        btn_mk9_2ib.place(x=50, y=400)
        def ibkonversi_2ib():
            recogabsen.recabsen.konversi_2ib()
        btn_mk10_2ib = tk.Button(wrapper_mk2ib,text="Dasar Konversi Energi Elektrik *", width=30, height=2, command=ibkonversi_2ib)
        btn_mk10_2ib.place(x=50, y=445)
        mk2ib.mainloop()
    def mk3ib():
        mk3ib = tk.Tk()
        mk3ib.title("FR SYSTEM")
        mk3ib.geometry("360x750")
        wrapper_mk3ib = LabelFrame(mk3ib, text="mata kuliah")
        wrapper_mk3ib.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ib = tk.Label(wrapper_mk3ib,text="PILIH MATA KULIAH")
        lbl_gmk3ib.place(x=100,y=10)
        # create btn
        def ibpi_3ib():
            recogabsen.recabsen.pi_3ib()
        btn_mk1_3ib = tk.Button(wrapper_mk3ib,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=ibpi_3ib)
        btn_mk1_3ib.place(x=50, y=40)
        def ibanalog_3ib():
            recogabsen.recabsen.analog_3ib()
        btn_mk2_3ib = tk.Button(wrapper_mk3ib,text="Elektronika Analog *", width=30, height=2, command=ibanalog_3ib)
        btn_mk2_3ib.place(x=50, y=85)
        def ibtekelek_3ib():
            recogabsen.recabsen.tekelek_3ib()
        btn_mk3_3ib = tk.Button(wrapper_mk3ib,text="Alg & Pemrog Kasus Tek.Elek #", width=30, height=2, command=ibtekelek_3ib)
        btn_mk3_3ib.place(x=50, y=130)
        def ibradio_3ib():
            recogabsen.recabsen.radio_3ib()
        btn_mk4_3ib = tk.Button(wrapper_mk3ib,text="Teknik Radio & Televisi", width=30, height=2, command=ibradio_3ib)
        btn_mk4_3ib.place(x=50, y=175)
        def ibsinyal_3ib():
            recogabsen.recabsen.sinyal_3ib()
        btn_mk5_3ib = tk.Button(wrapper_mk3ib,text="Sistem Pemrosesan Sinyal", width=30, height=2, command=ibsinyal_3ib)
        btn_mk5_3ib.place(x=50, y=220)
        def ibtele_3ib():
            recogabsen.recabsen.tele_3ib()
        btn_mk6_3ib = tk.Button(wrapper_mk3ib,text="Elektronika Telekomunikasi *", width=30, height=2, command=ibtele_3ib)
        btn_mk6_3ib.place(x=50, y=265)
        def ibdayaR_3ib():
            recogabsen.recabsen.dayaR_3ib()
        btn_mk7_3ib = tk.Button(wrapper_mk3ib,text="Elektronika Daya /R", width=30, height=2, command=ibdayaR_3ib)
        btn_mk7_3ib.place(x=50, y=310)
        def ibpembangkit_3ib():
            recogabsen.recabsen.pembangkit_3ib()
        btn_mk8_3ib = tk.Button(wrapper_mk3ib,text="Sist.Pembangkit Tenaga Elektrik *", width=30, height=2, command=ibpembangkit_3ib)
        btn_mk8_3ib.place(x=50, y=355)
        def ibnstrumen_3ib():
            recogabsen.recabsen.instrumen_3ib()
        btn_mk9_3ib = tk.Button(wrapper_mk3ib,text="Instrumentasi Elektronika *", width=30, height=2, command=ibnstrumen_3ib)
        btn_mk9_3ib.place(x=50, y=400)
        def ibarus_3ib():
            recogabsen.recabsen.arus_3ib()
        btn_mk10_3ib = tk.Button(wrapper_mk3ib,text="Teknik Tegangan & Arus Tinggi *", width=30, height=2, command=ibarus_3ib)
        btn_mk10_3ib.place(x=50, y=445)
        def ibtransmisi_3ib():
            recogabsen.recabsen.transmisi_3ib()
        btn_mk11_3ib = tk.Button(wrapper_mk3ib, text="Saluran Transmisi *", width=30, height=2, command=ibtransmisi_3ib)
        btn_mk11_3ib.place(x=50, y=490)
        def ibgraf_3ib():
            recogabsen.recabsen.graf_3ib()
        btn_mk12_3ib = tk.Button(wrapper_mk3ib, text="Terapan Teori Graf", width=30, height=2, command=ibgraf_3ib)
        btn_mk12_3ib.place(x=50, y=535)
        def ibdaya_3ib():
            recogabsen.recabsen.daya_3ib()
        btn_mk13_3ib = tk.Button(wrapper_mk3ib, text="Elektronika Daya", width=30, height=2, command=ibdaya_3ib)
        btn_mk13_3ib.place(x=50, y=580)
        def ibmelek_3ib():
            recogabsen.recabsen.melek_3ib()
        btn_mk14_3ib = tk.Button(wrapper_mk3ib, text="Mesin Elektrik 2 */**", width=30, height=2, command=ibmelek_3ib)
        btn_mk14_3ib.place(x=50, y=625)
        mk3ib.mainloop()
    def mk4ib():
        mk4ib = tk.Tk()
        mk4ib.title("FR SYSTEM")
        mk4ib.geometry("360x600")
        wrapper_mk4ib = LabelFrame(mk4ib, text="mata kuliah")
        wrapper_mk4ib.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ib = tk.Label(wrapper_mk4ib,text="PILIH MATA KULIAH")
        lbl_gmk4ib.place(x=100,y=10)
        # create btn
        def ibndus_4ib():
            recogabsen.recabsen.indus_4ib()
        btn_mk1_4ib = tk.Button(wrapper_mk4ib,text="Komponen Elektronika Industri", width=30, height=2, command=ibndus_4ib)
        btn_mk1_4ib.place(x=50, y=40)
        def ibmedis_4ib():
            recogabsen.recabsen.medis_4ib()
        btn_mk2_4ib = tk.Button(wrapper_mk4ib,text="Elektronika Medis", width=30, height=2, command=ibmedis_4ib)
        btn_mk2_4ib.place(x=50, y=85)
        def iboptik_4ib():
            recogabsen.recabsen.optik_4ib()
        btn_mk3_4ib = tk.Button(wrapper_mk4ib,text="Elektronika Optik", width=30, height=2, command=iboptik_4ib)
        btn_mk3_4ib.place(x=50, y=130)
        def ibproteksi_4ib():
            recogabsen.recabsen.proteksi_4ib()
        btn_mk4_4ib = tk.Button(wrapper_mk4ib,text="Proteksi Tenaga Elektrik", width=30, height=2, command=ibproteksi_4ib)
        btn_mk4_4ib.place(x=50, y=175)
        def ibrobot_4ib():
            recogabsen.recabsen.robot_4ib()
        btn_mk5_4ib = tk.Button(wrapper_mk4ib,text="Robotika Cerdas", width=30, height=2, command=ibrobot_4ib)
        btn_mk5_4ib.place(x=50, y=220)
        def ibmikro_4ib():
            recogabsen.recabsen.mikro_4ib()
        btn_mk6_4ib = tk.Button(wrapper_mk4ib,text="Teknik Gelombang Mikro", width=30, height=2, command=ibmikro_4ib)
        btn_mk6_4ib.place(x=50, y=265)
        def ibtele_4ib():
            recogabsen.recabsen.tele_4ib()
        btn_mk7_4ib = tk.Button(wrapper_mk4ib,text="Sist. Jaringan Telekomunikasi Ljt", width=30, height=2, command=ibtele_4ib)
        btn_mk7_4ib.place(x=50, y=310)
        def ibselular_4ib():
            recogabsen.recabsen.selular_4ib()
        btn_mk8_4ib = tk.Button(wrapper_mk4ib,text="Teknologi Selular", width=30, height=2, command=ibselular_4ib)
        btn_mk8_4ib.place(x=50, y=355)
        def ibtrans_4ib():
            recogabsen.recabsen.trans_4ib()
        btn_mk9_4ib = tk.Button(wrapper_mk4ib,text="Transformator Tenaga Elektrik", width=30, height=2, command=ibtrans_4ib)
        btn_mk9_4ib.place(x=50, y=400)
        def ibotomatisasi_4ib():
            recogabsen.recabsen.otomatisasi_4ib()
        btn_mk10_4ib = tk.Button(wrapper_mk4ib,text="Teknik Otomatisasi Sist.Elekt", width=30, height=2, command=ibotomatisasi_4ib)
        btn_mk10_4ib.place(x=50, y=445)
        mk4ib.mainloop()
    
# AKUNTANSI
    def mk1eb():
        mk1eb = tk.Tk()
        mk1eb.title("FR SYSTEM")
        mk1eb.geometry("360x650")
        wrapper_mk1eb = LabelFrame(mk1eb, text="mata kuliah")
        wrapper_mk1eb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1eb = tk.Label(wrapper_mk1eb,text="PILIH MATA KULIAH")
        lbl_gmk1eb.place(x=100,y=10)
        # create btn
        def ebkomtiA_1eb():
            recogabsen.recabsen.komtiA_1eb()
        btn_mk1_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Komputer & TI 2A", width=30, height=2, command=ebkomtiA_1eb)
        btn_mk1_1eb.place(x=50, y=40)
        def ebkomtiB_1eb():
            recogabsen.recabsen.komtiB_1eb()
        btn_mk2_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Komputer & TI 2B", width=30, height=2, command=ebkomtiB_1eb)
        btn_mk2_1eb.place(x=50, y=85)
        def ebkomtiC_1eb():
            recogabsen.recabsen.komtiC_1eb()
        btn_mk3_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Komputer & TI 2C", width=30, height=2, command=ebkomtiC_1eb)
        btn_mk3_1eb.place(x=50, y=130)
        def ebdigiciti_1eb():
            recogabsen.recabsen.digiciti_1eb()
        btn_mk4_1eb = tk.Button(wrapper_mk1eb,text="Digital Citizenship", width=30, height=2, command=ebdigiciti_1eb)
        btn_mk4_1eb.place(x=50, y=175)
        def ebmatekonomi_1eb():
            recogabsen.recabsen.matekonomi_1eb()
        btn_mk5_1eb = tk.Button(wrapper_mk1eb,text="Matematika Ekonomi 2 **", width=30, height=2, command=ebmatekonomi_1eb)
        btn_mk5_1eb.place(x=50, y=220)
        def ebpanc_1eb():
            recogabsen.recabsen.panc_1eb()
        btn_mk6_1eb = tk.Button(wrapper_mk1eb,text="Pendidikan Pancasila *", width=30, height=2, command=ebpanc_1eb)
        btn_mk6_1eb.place(x=50, y=265)
        def ebsosio_1eb():
            recogabsen.recabsen.sosio_1eb()
        btn_mk7_1eb = tk.Button(wrapper_mk1eb,text="Sosiologi & Politik", width=30, height=2, command=ebsosio_1eb)
        btn_mk7_1eb.place(x=50, y=310)
        def ebing_1eb():
            recogabsen.recabsen.bing_1eb()
        btn_mk8_1eb = tk.Button(wrapper_mk1eb,text="Bahasa Inggris 2", width=30, height=2, command=ebing_1eb)
        btn_mk8_1eb.place(x=50, y=355)
        def ebpakunA_1eb():
            recogabsen.recabsen.pakunA_1eb()
        btn_mk9_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Akuntansi 2A", width=30, height=2, command=ebpakunA_1eb)
        btn_mk9_1eb.place(x=50, y=400)
        def ebpakunB_1eb():
            recogabsen.recabsen.pakunB_1eb()
        btn_mk10_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Akuntansi 2B", width=30, height=2, command=ebpakunB_1eb)
        btn_mk10_1eb.place(x=50, y=445)
        def ebkoindo_1eb():
            recogabsen.recabsen.ekoindo_1eb()
        btn_mk11_1eb = tk.Button(wrapper_mk1eb,text="Perekonomian Indonesia #", width=30, height=2, command=ebkoindo_1eb)
        btn_mk11_1eb.place(x=50, y=490)
        def ebpeko_1eb():
            recogabsen.recabsen.peko_1eb()
        btn_mk12_1eb = tk.Button(wrapper_mk1eb,text="Pengantar Ekonomi 2 *", width=30, height=2, command=ebpeko_1eb)
        btn_mk12_1eb.place(x=50, y=535)
        mk1eb.mainloop()
    def mk2eb():
        mk2eb = tk.Tk()
        mk2eb.title("FR SYSTEM")
        mk2eb.geometry("360x600")
        wrapper_mk2eb = LabelFrame(mk2eb, text="mata kuliah")
        wrapper_mk2eb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2eb = tk.Label(wrapper_mk2eb,text="PILIH MATA KULIAH")
        lbl_gmk2eb.place(x=100,y=10)
        # create btn
        def ebsocnet_2eb():
            recogabsen.recabsen.socnet_2eb()
        btn_mk1_2eb = tk.Button(wrapper_mk2eb,text="Social Networking & Creative Cont", width=30, height=2, command=ebsocnet_2eb)
        btn_mk1_2eb.place(x=50, y=40)
        def ebstat_2eb():
            recogabsen.recabsen.stat_2eb()
        btn_mk2_2eb = tk.Button(wrapper_mk2eb,text="Statistika 2 **", width=30, height=2, command=ebstat_2eb)
        btn_mk2_2eb.place(x=50, y=85)
        def ebakunmanaj_2eb():
            recogabsen.recabsen.akunmanaj_2eb()
        btn_mk3_2eb = tk.Button(wrapper_mk2eb,text="Akuntansi Manajemen */**", width=30, height=2, command=ebakunmanaj_2eb)
        btn_mk3_2eb.place(x=50, y=130)
        def ebplakun_2eb():
            recogabsen.recabsen.plakun_2eb()
        btn_mk4_2eb = tk.Button(wrapper_mk2eb,text="Perangkat Lunak Akuntansi 2", width=30, height=2, command=ebplakun_2eb)
        btn_mk4_2eb.place(x=50, y=175)
        def ebteko_2eb():
            recogabsen.recabsen.teko_2eb()
        btn_mk5_2eb = tk.Button(wrapper_mk2eb,text="Teori Ekonomi 2", width=30, height=2, command=ebteko_2eb)
        btn_mk5_2eb.place(x=50, y=220)
        def ebhukum_2eb():
            recogabsen.recabsen.hukum_2eb()
        btn_mk6_2eb = tk.Button(wrapper_mk2eb,text="Aspek Hukum Dalam Ekonomi #", width=30, height=2, command=ebhukum_2eb)
        btn_mk6_2eb.place(x=50, y=265)
        def ebank_2eb():
            recogabsen.recabsen.bank_2eb()
        btn_mk7_2eb = tk.Button(wrapper_mk2eb,text="Bank & Lembaga Keuangan 2 *", width=30, height=2, command=ebank_2eb)
        btn_mk7_2eb.place(x=50, y=310)
        def ebkeu_2eb():
            recogabsen.recabsen.keu_2eb()
        btn_mk8_2eb = tk.Button(wrapper_mk2eb,text="Akuntansi Keu.Menengah 2 **", width=30, height=2, command=ebkeu_2eb)
        btn_mk8_2eb.place(x=50, y=355)
        def ebmanajkeu_2eb():
            recogabsen.recabsen.manajkeu_2eb()
        btn_mk9_2eb = tk.Button(wrapper_mk2eb,text="Manajemen Keuangan 2 */**", width=30, height=2, command=ebmanajkeu_2eb)
        btn_mk9_2eb.place(x=50, y=400)
        def ebsiak_2eb():
            recogabsen.recabsen.siak_2eb()
        btn_mk10_2eb = tk.Button(wrapper_mk2eb,text="Sistem Informasi Akuntansi */**", width=30, height=2, command=ebsiak_2eb)
        btn_mk10_2eb.place(x=50, y=445)
        mk2eb.mainloop()
    def mk3eb():
        mk3eb = tk.Tk()
        mk3eb.title("FR SYSTEM")
        mk3eb.geometry("360x600")
        wrapper_mk3eb = LabelFrame(mk3eb, text="mata kuliah")
        wrapper_mk3eb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3eb = tk.Label(wrapper_mk3eb,text="PILIH MATA KULIAH")
        lbl_gmk3eb.place(x=100,y=10)
        # create btn
        def ebpajak_3eb():
            recogabsen.recabsen.pajak_3eb()
        btn_mk1_3eb = tk.Button(wrapper_mk3eb,text="Akuntansi Pajak **", width=30, height=2, command=ebpajak_3eb)
        btn_mk1_3eb.place(x=50, y=40)
        def ebinter_3eb():
            recogabsen.recabsen.inter_3eb()
        btn_mk2_3eb = tk.Button(wrapper_mk3eb,text="Akuntansi Internasional", width=30, height=2, command=ebinter_3eb)
        btn_mk2_3eb.place(x=50, y=85)
        def ebingbis_3eb():
            recogabsen.recabsen.bingbis_3eb()
        btn_mk3_3eb = tk.Button(wrapper_mk3eb,text="Bahasa Inggris Bisnis 2 #", width=30, height=2, command=ebingbis_3eb)
        btn_mk3_3eb.place(x=50, y=130)
        def ebmanop_3eb():
            recogabsen.recabsen.manop_3eb()
        btn_mk4_3eb = tk.Button(wrapper_mk3eb,text="Manajemen Operasional", width=30, height=2, command=ebmanop_3eb)
        btn_mk4_3eb.place(x=50, y=175)
        def ebsia_3eb():
            recogabsen.recabsen.sia_3eb()
        btn_mk5_3eb = tk.Button(wrapper_mk3eb,text="Analisis & Perancangan SIA **", width=30, height=2, command=ebsia_3eb)
        btn_mk5_3eb.place(x=50, y=220)
        def ebtekun_3eb():
            recogabsen.recabsen.tekun_3eb()
        btn_mk6_3eb = tk.Button(wrapper_mk3eb,text="Teori Akuntansi *", width=30, height=2, command=ebtekun_3eb)
        btn_mk6_3eb.place(x=50, y=265)
        def ebperiksa_3eb():
            recogabsen.recabsen.periksa_3eb()
        btn_mk7_3eb = tk.Button(wrapper_mk3eb,text="Pemeriksaan Akuntansi 2 **", width=30, height=2, command=ebperiksa_3eb)
        btn_mk7_3eb.place(x=50, y=310)
        def ebkeulnjt_3eb():
            recogabsen.recabsen.keulnjt_3eb()
        btn_mk8_3eb = tk.Button(wrapper_mk3eb,text="Akuntansi Keuangan Lanjut 2", width=30, height=2, command=ebkeulnjt_3eb)
        btn_mk8_3eb.place(x=50, y=355)
        def ebindo_3eb():
            recogabsen.recabsen.bindo_3eb()
        btn_mk9_3eb = tk.Button(wrapper_mk3eb,text="Bahasa Indonesia 2", width=30, height=2, command=ebindo_3eb)
        btn_mk9_3eb.place(x=50, y=400)
        def ebsabigdat_3eb():
            recogabsen.recabsen.sabigdat_3eb()
        btn_mk10_3eb = tk.Button(wrapper_mk3eb,text="Sains Data & Analisis Big Data", width=30, height=2, command=ebsabigdat_3eb)
        btn_mk10_3eb.place(x=50, y=445)
        mk3eb.mainloop()
    def mk4eb():
        mk4eb = tk.Tk()
        mk4eb.title("FR SYSTEM")
        mk4eb.geometry("360x500")
        wrapper_mk4eb = LabelFrame(mk4eb, text="mata kuliah")
        wrapper_mk4eb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4eb = tk.Label(wrapper_mk4eb,text="PILIH MATA KULIAH")
        lbl_gmk4eb.place(x=100,y=10)
        # create btn
        def ebusaha_4eb():
            recogabsen.recabsen.usaha_4eb()
        btn_mk1_4eb = tk.Button(wrapper_mk4eb,text="Kewirausahaan", width=30, height=2, command=ebusaha_4eb)
        btn_mk1_4eb.place(x=50, y=40)
        def ebisnis_4eb():
            recogabsen.recabsen.bisnis_4eb()
        btn_mk2_4eb = tk.Button(wrapper_mk4eb,text="Studi Kelayakan Bisnis", width=30, height=2, command=ebisnis_4eb)
        btn_mk2_4eb.place(x=50, y=85)
        def ebseminar_4eb():
            recogabsen.recabsen.seminar_4eb()
        btn_mk3_4eb = tk.Button(wrapper_mk4eb,text="Seminar Kajian Bidang Akuntansi", width=30, height=2, command=ebseminar_4eb)
        btn_mk3_4eb.place(x=50, y=130)
        def ebforen_4eb():
            recogabsen.recabsen.foren_4eb()
        btn_mk4_4eb = tk.Button(wrapper_mk4eb,text="Akun.Forensik & AuditInvestigatif", width=30, height=2, command=ebforen_4eb)
        btn_mk4_4eb.place(x=50, y=175)
        def ebsyariah_4eb():
            recogabsen.recabsen.syariah_4eb()
        btn_mk5_4eb = tk.Button(wrapper_mk4eb,text="Akuntansi Syariah", width=30, height=2, command=ebsyariah_4eb)
        btn_mk5_4eb.place(x=50, y=220)
        def ebmanpajak_4eb():
            recogabsen.recabsen.manpajak_4eb()
        btn_mk6_4eb = tk.Button(wrapper_mk4eb,text="Manajemen Perpajakan", width=30, height=2, command=ebmanpajak_4eb)
        btn_mk6_4eb.place(x=50, y=265)
        def ebmasy_4eb():
            recogabsen.recabsen.masy_4eb()
        btn_mk7_4eb = tk.Button(wrapper_mk4eb,text="Kecerdasan Artifisial & Masy.", width=30, height=2, command=ebmasy_4eb)
        btn_mk7_4eb.place(x=50, y=310)
        mk4eb.mainloop()

# MANAJEMEN
    def mk1ea():
        mk1ea = tk.Tk()
        mk1ea.title("FR SYSTEM")
        mk1ea.geometry("360x670")
        wrapper_mk1ea = LabelFrame(mk1ea, text="mata kuliah")
        wrapper_mk1ea.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ea = tk.Label(wrapper_mk1ea,text="PILIH MATA KULIAH")
        lbl_gmk1ea.place(x=100,y=10)
        # create btn
        def eakomtiA_1ea():
            recogabsen.recabsen.komtiA_1ea()
        btn_mk1_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Komputer & TI 2A", width=30, height=2, command=eakomtiA_1ea)
        btn_mk1_1ea.place(x=50, y=40)
        def eakomtiB_1ea():
            recogabsen.recabsen.komtiB_1ea()
        btn_mk2_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Komputer & TI 2B", width=30, height=2, command=eakomtiB_1ea)
        btn_mk2_1ea.place(x=50, y=85)
        def eakomtiC_1ea():
            recogabsen.recabsen.komtiC_1ea()
        btn_mk3_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Komputer & TI 2C", width=30, height=2, command=eakomtiC_1ea)
        btn_mk3_1ea.place(x=50, y=130)
        def eadigiciti_1ea():
            recogabsen.recabsen.digiciti_1ea()
        btn_mk4_1ea = tk.Button(wrapper_mk1ea,text="Digital Citizenship", width=30, height=2, command=eadigiciti_1ea)
        btn_mk4_1ea.place(x=50, y=175)
        def eamateko_1ea():
            recogabsen.recabsen.mateko_1ea()
        btn_mk5_1ea = tk.Button(wrapper_mk1ea,text="Matematika Ekonomi 2 **", width=30, height=2, command=eamateko_1ea)
        btn_mk5_1ea.place(x=50, y=220)
        def eapanc_1ea():
            recogabsen.recabsen.panc_1ea()
        btn_mk6_1ea = tk.Button(wrapper_mk1ea,text="Pendidikan Pancasila *", width=30, height=2, command=eapanc_1ea)
        btn_mk6_1ea.place(x=50, y=265)
        def eabindo_1ea():
            recogabsen.recabsen.bindo_1ea()
        btn_mk7_1ea = tk.Button(wrapper_mk1ea,text="Bahasa Indonesia 2", width=30, height=2, command=eabindo_1ea)
        btn_mk7_1ea.place(x=50, y=310)
        def eabing_1ea():
            recogabsen.recabsen.bing_1ea()
        btn_mk8_1ea = tk.Button(wrapper_mk1ea,text="Bahasa Inggris 2 #", width=30, height=2, command=eabing_1ea)
        btn_mk8_1ea.place(x=50, y=355)
        def eapakun_1ea():
            recogabsen.recabsen.pakun_1ea()
        btn_mk9_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Akuntansi 2 **", width=30, height=2, command=eapakun_1ea)
        btn_mk9_1ea.place(x=50, y=400)
        def eapasar_1ea():
            recogabsen.recabsen.pasar_1ea()
        btn_mk10_1ea = tk.Button(wrapper_mk1ea,text="Manajemen Pemasaran *", width=30, height=2, command=eapasar_1ea)
        btn_mk10_1ea.place(x=50, y=445)
        def eamanaj_1ea():
            recogabsen.recabsen.manaj_1ea()
        btn_mk11_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Manajemen *", width=30, height=2, command=eamanaj_1ea)
        btn_mk11_1ea.place(x=50, y=490)
        def eapekon_1ea():
            recogabsen.recabsen.pekon_1ea()
        btn_mk12_1ea = tk.Button(wrapper_mk1ea,text="Pengantar Ekonomi 2", width=30, height=2, command=eapekon_1ea)
        btn_mk12_1ea.place(x=50, y=535)
        mk1ea.mainloop()
    def mk2ea():
        mk2ea = tk.Tk()
        mk2ea.title("FR SYSTEM")
        mk2ea.geometry("360x540")
        wrapper_mk2ea = LabelFrame(mk2ea, text="mata kuliah")
        wrapper_mk2ea.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ea = tk.Label(wrapper_mk2ea,text="PILIH MATA KULIAH")
        lbl_gmk2ea.place(x=100,y=10)
        # create btn
        def easocnet_2ea():
            recogabsen.recabsen.socnet_2ea()
        btn_mk1_2ea = tk.Button(wrapper_mk2ea,text="Social Networking & Creative Cont", width=30, height=2, command=easocnet_2ea)
        btn_mk1_2ea.place(x=50, y=40)
        def eastat_2ea():
            recogabsen.recabsen.stat_2ea()
        btn_mk2_2ea = tk.Button(wrapper_mk2ea,text="Statistika 2 **", width=30, height=2, command=eastat_2ea)
        btn_mk2_2ea.place(x=50, y=85)
        def eakunmanaj_2ea():
            recogabsen.recabsen.akunmanaj_2ea()
        btn_mk3_2ea = tk.Button(wrapper_mk2ea,text="Akuntansi Manajemen", width=30, height=2, command=eakunmanaj_2ea)
        btn_mk3_2ea.place(x=50, y=130)
        def eamanajerial_2ea():
            recogabsen.recabsen.manajerial_2ea()
        btn_mk4_2ea = tk.Button(wrapper_mk2ea,text="Ekonomi Manajerial", width=30, height=2, command=eamanajerial_2ea)
        btn_mk4_2ea.place(x=50, y=175)
        def eariset_2ea():
            recogabsen.recabsen.riset_2ea()
        btn_mk5_2ea = tk.Button(wrapper_mk2ea,text="Riset Operasional 2 **", width=30, height=2, command=eariset_2ea)
        btn_mk5_2ea.place(x=50, y=220)
        def eako_2ea():
            recogabsen.recabsen.eko_2ea()
        btn_mk6_2ea = tk.Button(wrapper_mk2ea,text="Teori Ekonomi 2 *", width=30, height=2, command=eako_2ea)
        btn_mk6_2ea.place(x=50, y=265)
        def easim_2ea():
            recogabsen.recabsen.sim_2ea()
        btn_mk7_2ea = tk.Button(wrapper_mk2ea,text="Pengantar Teknologi SIM 2 **", width=30, height=2, command=easim_2ea)
        btn_mk7_2ea.place(x=50, y=310)
        def earev_2ea():
            recogabsen.recabsen.rev_2ea()
        btn_mk8_2ea = tk.Button(wrapper_mk2ea,text="Mnj Keu.Era Rev.Industri 4.0 */**", width=30, height=2, command=earev_2ea)
        btn_mk8_2ea.place(x=50, y=355)
        def eabank_2ea():
            recogabsen.recabsen.bank_2ea()
        btn_mk9_2ea = tk.Button(wrapper_mk2ea,text="Komp.Lembaga Keu.Perbankan **", width=30, height=2, command=eabank_2ea)
        btn_mk9_2ea.place(x=50, y=400)
        mk2ea.mainloop()
    def mk3ea():
        mk3ea = tk.Tk()
        mk3ea.title("FR SYSTEM")
        mk3ea.geometry("360x540")
        wrapper_mk3ea = LabelFrame(mk3ea, text="mata kuliah")
        wrapper_mk3ea.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ea = tk.Label(wrapper_mk3ea,text="PILIH MATA KULIAH")
        lbl_gmk3ea.place(x=100,y=10)
        # create btn
        def eapajak_3ea():
            recogabsen.recabsen.pajak_3ea()
        btn_mk1_3ea = tk.Button(wrapper_mk3ea,text="Komp.Perpajakan Untuk Manaj **", width=30, height=2, command=eapajak_3ea)
        btn_mk1_3ea.place(x=50, y=40)
        def eaproyek_3ea():
            recogabsen.recabsen.proyek_3ea()
        btn_mk2_3ea = tk.Button(wrapper_mk3ea,text="Teknik Proyeksi Bisnis", width=30, height=2, command=eaproyek_3ea)
        btn_mk2_3ea.place(x=50, y=85)
        def eakonsumen_3ea():
            recogabsen.recabsen.konsumen_3ea()
        btn_mk3_3ea = tk.Button(wrapper_mk3ea,text="Perilaku Konsumen", width=30, height=2, command=eakonsumen_3ea)
        btn_mk3_3ea.place(x=50, y=130)
        def eakoindo_3ea():
            recogabsen.recabsen.ekoindo_3ea()
        btn_mk4_3ea = tk.Button(wrapper_mk3ea,text="Perekonomian Indonesia", width=30, height=2, command=eakoindo_3ea)
        btn_mk4_3ea.place(x=50, y=175)
        def eabingbis_3ea():
            recogabsen.recabsen.bingbis_3ea()
        btn_mk5_3ea = tk.Button(wrapper_mk3ea,text="Bahasa Inggris Bisnis 2", width=30, height=2, command=eabingbis_3ea)
        btn_mk5_3ea.place(x=50, y=220)
        def easdm_3ea():
            recogabsen.recabsen.sdm_3ea()
        btn_mk6_3ea = tk.Button(wrapper_mk3ea,text="Manajemen Sumber Daya Manusia *", width=30, height=2, command=easdm_3ea)
        btn_mk6_3ea.place(x=50, y=265)
        def eatika_3ea():
            recogabsen.recabsen.etika_3ea()
        btn_mk7_3ea = tk.Button(wrapper_mk3ea,text="Etika Bisnis #", width=30, height=2, command=eatika_3ea)
        btn_mk7_3ea.place(x=50, y=310)
        def easabigdat_3ea():
            recogabsen.recabsen.sabigdat_3ea()
        btn_mk8_3ea = tk.Button(wrapper_mk3ea,text="Sains Data & Analisis Big Data", width=30, height=2, command=easabigdat_3ea)
        btn_mk8_3ea.place(x=50, y=355)
        def ealayak_3ea():
            recogabsen.recabsen.layak_3ea()
        btn_mk9_3ea = tk.Button(wrapper_mk3ea,text="Studi Kelayakan Bisnis *", width=30, height=2, command=ealayak_3ea)
        btn_mk9_3ea.place(x=50, y=400)
        mk3ea.mainloop()
    def mk4ea():
        mk4ea = tk.Tk()
        mk4ea.title("FR SYSTEM")
        mk4ea.geometry("360x500")
        wrapper_mk4ea = LabelFrame(mk4ea, text="mata kuliah")
        wrapper_mk4ea.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ea = tk.Label(wrapper_mk4ea,text="PILIH MATA KULIAH")
        lbl_gmk4ea.place(x=100,y=10)
        # create btn
        def eamanajljt_4ea():
            recogabsen.recabsen.manajljt_4ea()
        btn_mk1_4ea = tk.Button(wrapper_mk4ea,text="Akuntansi Manajemen Lanjut", width=30, height=2, command=eamanajljt_4ea)
        btn_mk1_4ea.place(x=50, y=40)
        def eakapita_4ea():
            recogabsen.recabsen.kapita_4ea()
        btn_mk2_4ea = tk.Button(wrapper_mk4ea,text="Kapita Selekta Pasar Modal", width=30, height=2, command=eakapita_4ea)
        btn_mk2_4ea.place(x=50, y=85)
        def eakinerja_4ea():
            recogabsen.recabsen.kinerja_4ea()
        btn_mk3_4ea = tk.Button(wrapper_mk4ea,text="Manajemen Kinerja", width=30, height=2, command=eakinerja_4ea)
        btn_mk3_4ea.place(x=50, y=130)
        def eapasarindus_4ea():
            recogabsen.recabsen.pasarindus_4ea()
        btn_mk4_4ea = tk.Button(wrapper_mk4ea,text="Manajemen Pemasaran Industri", width=30, height=2, command=eapasarindus_4ea)
        btn_mk4_4ea.place(x=50, y=175)
        def easeminar_4ea():
            recogabsen.recabsen.seminar_4ea()
        btn_mk5_4ea = tk.Button(wrapper_mk4ea,text="Seminar Kajian Bidang Manajemen", width=30, height=2, command=easeminar_4ea)
        btn_mk5_4ea.place(x=50, y=220)
        def earesiko_4ea():
            recogabsen.recabsen.resiko_4ea()
        btn_mk6_4ea = tk.Button(wrapper_mk4ea,text="Manajemen Risiko", width=30, height=2, command=earesiko_4ea)
        btn_mk6_4ea.place(x=50, y=265)
        def eamasy_4ea():
            recogabsen.recabsen.masy_4ea()
        btn_mk7_4ea = tk.Button(wrapper_mk4ea,text="Kecerdasan Artifisial & Masy.", width=30, height=2, command=eamasy_4ea)
        btn_mk7_4ea.place(x=50, y=310)
        mk4ea.mainloop()

# ARSITEKTUR
    def mk1tb():
        mk1tb = tk.Tk()
        mk1tb.title("FR SYSTEM")
        mk1tb.geometry("360x540")
        wrapper_mk1tb = LabelFrame(mk1tb, text="mata kuliah")
        wrapper_mk1tb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1tb = tk.Label(wrapper_mk1tb,text="PILIH MATA KULIAH")
        lbl_gmk1tb.place(x=100,y=10)
        # create btn
        def tbestetika_1tb():
            recogabsen.recabsen.estetika_1tb()
        btn_mk1_1tb = tk.Button(wrapper_mk1tb,text="Estetika Bentuk 2", width=30, height=2, command=tbestetika_1tb)
        btn_mk1_1tb.place(x=50, y=40)
        def tbcadJ_1tb():
            recogabsen.recabsen.cadJ_1tb()
        btn_mk2_1tb = tk.Button(wrapper_mk1tb,text="Auto CAD J", width=30, height=2, command=tbcadJ_1tb)
        btn_mk2_1tb.place(x=50, y=85)
        def tbcadI_1tb():
            recogabsen.recabsen.cadI_1tb()
        btn_mk3_1tb = tk.Button(wrapper_mk1tb,text="Auto CAD I", width=30, height=2, command=tbcadI_1tb)
        btn_mk3_1tb.place(x=50, y=130)
        def tbmat_1tb():
            recogabsen.recabsen.mat_1tb()
        btn_mk4_1tb = tk.Button(wrapper_mk1tb,text="Matematika 2 *", width=30, height=2, command=tbmat_1tb)
        btn_mk4_1tb.place(x=50, y=175)
        def tbart_1tb():
            recogabsen.recabsen.art_1tb()
        btn_mk5_1tb = tk.Button(wrapper_mk1tb,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=tbart_1tb)
        btn_mk5_1tb.place(x=50, y=220)
        def tbstruk_1tb():
            recogabsen.recabsen.struk_1tb()
        btn_mk6_1tb = tk.Button(wrapper_mk1tb,text="Struktur dan Konstruksi 1 *", width=30, height=2, command=tbstruk_1tb)
        btn_mk6_1tb.place(x=50, y=265)
        def tbstudio_1tb():
            recogabsen.recabsen.studio_1tb()
        btn_mk7_1tb = tk.Button(wrapper_mk1tb,text="Studio Peranc. Arsitektur 1 *", width=30, height=2, command=tbstudio_1tb)
        btn_mk7_1tb.place(x=50, y=310)
        def tbmetode_1tb():
            recogabsen.recabsen.metode_1tb()
        btn_mk8_1tb = tk.Button(wrapper_mk1tb,text="Metode Perancangan Arsitektur", width=30, height=2, command=tbmetode_1tb)
        btn_mk8_1tb.place(x=50, y=355)
        def tbarsi_1tb():
            recogabsen.recabsen.arsi_1tb()
        btn_mk9_1tb = tk.Button(wrapper_mk1tb,text="Teori Arsitektur 1", width=30, height=2, command=tbarsi_1tb)
        btn_mk9_1tb.place(x=50, y=400)
        mk1tb.mainloop()
    def mk2tb():
        mk2tb = tk.Tk()
        mk2tb.title("FR SYSTEM")
        mk2tb.geometry("360x540")
        wrapper_mk2tb = LabelFrame(mk2tb, text="mata kuliah")
        wrapper_mk2tb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2tb = tk.Label(wrapper_mk2tb,text="PILIH MATA KULIAH")
        lbl_gmk2tb.place(x=100,y=10)
        # create btn
        def tbstudio_2tb():
            recogabsen.recabsen.studio_2tb()
        btn_mk1_2tb = tk.Button(wrapper_mk2tb,text="Studio Peranc. Arsitektur 3 *", width=30, height=2, command=tbstudio_2tb)
        btn_mk1_2tb.place(x=50, y=40)
        def tbkomunikasi_2tb():
            recogabsen.recabsen.komunikasi_2tb()
        btn_mk2_2tb = tk.Button(wrapper_mk2tb,text="Teknik Komunikasi Arsitektural", width=30, height=2, command=tbkomunikasi_2tb)
        btn_mk2_2tb.place(x=50, y=85)
        def tbfilsafat_2tb():
            recogabsen.recabsen.filsafat_2tb()
        btn_mk3_2tb = tk.Button(wrapper_mk2tb,text="Filsafat Arsitektur", width=30, height=2, command=tbfilsafat_2tb)
        btn_mk3_2tb.place(x=50, y=130)
        def tbstruk_2tb():
            recogabsen.recabsen.struk_2tb()
        btn_mk4_2tb = tk.Button(wrapper_mk2tb,text="Struktur dan Konstruksi 3 *", width=30, height=2, command=tbstruk_2tb)
        btn_mk4_2tb.place(x=50, y=175)
        def tbutil_2tb():
            recogabsen.recabsen.util_2tb()
        btn_mk5_2tb = tk.Button(wrapper_mk2tb,text="Utilitas 2", width=30, height=2, command=tbutil_2tb)
        btn_mk5_2tb.place(x=50, y=220)
        def tbpkn_2tb():
            recogabsen.recabsen.pkn_2tb()
        btn_mk6_2tb = tk.Button(wrapper_mk2tb,text="Pendidikan Kewarganegaraan #", width=30, height=2, command=tbpkn_2tb)
        btn_mk6_2tb.place(x=50, y=265)
        def tbkembang_2tb():
            recogabsen.recabsen.kembang_2tb()
        btn_mk7_2tb = tk.Button(wrapper_mk2tb,text="Perkembangan Arsitektur 2", width=30, height=2, command=tbkembang_2tb)
        btn_mk7_2tb.place(x=50, y=310)
        def tbahan_2tb():
            recogabsen.recabsen.bahan_2tb()
        btn_mk8_2tb = tk.Button(wrapper_mk2tb,text="Teknologi Bahan", width=30, height=2, command=tbahan_2tb)
        btn_mk8_2tb.place(x=50, y=355)
        def tbapak_2tb():
            recogabsen.recabsen.tapak_2tb()
        btn_mk9_2tb = tk.Button(wrapper_mk2tb,text="Perancangan Tapak *", width=30, height=2, command=tbapak_2tb)
        btn_mk9_2tb.place(x=50, y=400)
        def tbigdat_2tb():
            recogabsen.recabsen.bigdat_2tb()
        btn_mk10_2tb = tk.Button(wrapper_mk2tb, text="Komputasi Big Data", width=30, height=2, command=tbigdat_2tb)
        btn_mk10_2tb.place(x=50, y=445)
        mk2tb.mainloop()
    def mk3tb():
        mk3tb = tk.Tk()
        mk3tb.title("FR SYSTEM")
        mk3tb.geometry("360x500")
        wrapper_mk3tb = LabelFrame(mk3tb, text="mata kuliah")
        wrapper_mk3tb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3tb = tk.Label(wrapper_mk3tb,text="PILIH MATA KULIAH")
        lbl_gmk3tb.place(x=100,y=10)
        # create btn
        def tbpraktek_3tb():
            recogabsen.recabsen.praktek_3tb()
        btn_mk1_3tb = tk.Button(wrapper_mk3tb,text="Kerja Praktek", width=30, height=2, command=tbpraktek_3tb)
        btn_mk1_3tb.place(x=50, y=40)
        def tblapangan_3tb():
            recogabsen.recabsen.lapangan_3tb()
        btn_mk2_3tb = tk.Button(wrapper_mk3tb,text="Kuliah Lapangan/Studi Ekskursi #", width=30, height=2, command=tblapangan_3tb)
        btn_mk2_3tb.place(x=50, y=85)
        def tbfoto_3tb():
            recogabsen.recabsen.foto_3tb()
        btn_mk3_3tb = tk.Button(wrapper_mk3tb,text="Fotografi Arsitektur", width=30, height=2, command=tbfoto_3tb)
        btn_mk3_3tb.place(x=50, y=130)
        def tbstudio_3tb():
            recogabsen.recabsen.studio_3tb()
        btn_mk4_3tb = tk.Button(wrapper_mk3tb,text="Studio Perancangan Arsitektur 5*", width=30, height=2, command=tbstudio_3tb)
        btn_mk4_3tb.place(x=50, y=175)
        def tbdalam_3tb():
            recogabsen.recabsen.dalam_3tb()
        btn_mk5_3tb = tk.Button(wrapper_mk3tb,text="Tata Ruang Dalam", width=30, height=2, command=tbdalam_3tb)
        btn_mk5_3tb.place(x=50, y=220)
        def tbluar_3tb():
            recogabsen.recabsen.luar_3tb()
        btn_mk6_3tb = tk.Button(wrapper_mk3tb,text="Tata Ruang Luar", width=30, height=2, command=tbluar_3tb)
        btn_mk6_3tb.place(x=50, y=265)
        def tbgraf_3tb():
            recogabsen.recabsen.graf_3tb()
        btn_mk7_3tb = tk.Button(wrapper_mk3tb,text="Terapan Teori Graf", width=30, height=2, command=tbgraf_3tb)
        btn_mk7_3tb.place(x=50, y=310)
        def tbsinema_3tb():
            recogabsen.recabsen.sinema_3tb()
        btn_mk8_3tb = tk.Button(wrapper_mk3tb,text="Sinematografi Arsitektur", width=30, height=2, command=tbsinema_3tb)
        btn_mk8_3tb.place(x=50, y=355)
        mk3tb.mainloop()
    def mk4tb():
        mk4tb = tk.Tk()
        mk4tb.title("FR SYSTEM")
        mk4tb.geometry("360x360")
        wrapper_mk4tb = LabelFrame(mk4tb, text="mata kuliah")
        wrapper_mk4tb.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4tb = tk.Label(wrapper_mk4tb,text="PILIH MATA KULIAH")
        lbl_gmk4tb.place(x=100,y=10)
        # create btn
        def tbrobot_4tb():
            recogabsen.recabsen.robot_4tb()
        btn_mk1_4tb = tk.Button(wrapper_mk4tb,text="Robotika Cerdas", width=30, height=2, command=tbrobot_4tb)
        btn_mk1_4tb.place(x=50, y=40)
        mk4tb.mainloop()

# TEKNIK SIPIL
    def mk1ta():
        mk1ta = tk.Tk()
        mk1ta.title("FR SYSTEM")
        mk1ta.geometry("360x540")
        wrapper_mk1ta = LabelFrame(mk1ta, text="mata kuliah")
        wrapper_mk1ta.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ta = tk.Label(wrapper_mk1ta,text="PILIH MATA KULIAH")
        lbl_gmk1ta.place(x=100,y=10)
        # create btn
        def tamat_1ta():
            recogabsen.recabsen.mat_1ta()
        btn_mk1_1ta = tk.Button(wrapper_mk1ta,text="Matematika 2", width=30, height=2, command=tamat_1ta)
        btn_mk1_1ta.place(x=50, y=40)
        def taetika_1ta():
            recogabsen.recabsen.etika_1ta()
        btn_mk2_1ta = tk.Button(wrapper_mk1ta,text="Etika Profesi & Komunikasi #", width=30, height=2, command=taetika_1ta)
        btn_mk2_1ta.place(x=50, y=85)
        def tabindo_1ta():
            recogabsen.recabsen.bindo_1ta()
        btn_mk3_1ta = tk.Button(wrapper_mk1ta,text="Bahasa Indonesia", width=30, height=2, command=tabindo_1ta)
        btn_mk3_1ta.place(x=50, y=130)
        def tart_1ta():
            recogabsen.recabsen.art_1ta()
        btn_mk4_1ta = tk.Button(wrapper_mk1ta,text="Teknologi Kecerdasan Artifisial", width=30, height=2, command=tart_1ta)
        btn_mk4_1ta.place(x=50, y=175)
        def tabahan_1ta():
            recogabsen.recabsen.bahan_1ta()
        btn_mk5_1ta = tk.Button(wrapper_mk1ta,text="Mekanika Bahan*", width=30, height=2, command=tabahan_1ta)
        btn_mk5_1ta.place(x=50, y=220)
        def tafisika_1ta():
            recogabsen.recabsen.fisika_1ta()
        btn_mk6_1ta = tk.Button(wrapper_mk1ta,text="Fisika 2", width=30, height=2, command=tafisika_1ta)
        btn_mk6_1ta.place(x=50, y=265)
        def tabahanR_1ta():
            recogabsen.recabsen.bahanR_1ta()
        btn_mk7_1ta = tk.Button(wrapper_mk1ta,text="Mekanika Bahan/R *", width=30, height=2, command=tabahanR_1ta)
        btn_mk7_1ta.place(x=50, y=310)
        def takontru_1ta():
            recogabsen.recabsen.kontru_1ta()
        btn_mk8_1ta = tk.Button(wrapper_mk1ta,text="Kewirausahaan Bisnis Jasa&Konstru", width=30, height=2, command=takontru_1ta)
        btn_mk8_1ta.place(x=50, y=355)
        def tapanc_1ta():
            recogabsen.recabsen.panc_1ta()
        btn_mk9_1ta = tk.Button(wrapper_mk1ta,text="Pendidikan Pancasila *", width=30, height=2, command=tapanc_1ta)
        btn_mk9_1ta.place(x=50, y=400)
        mk1ta.mainloop()
    def mk2ta():
        mk2ta = tk.Tk()
        mk2ta.title("FR SYSTEM")
        mk2ta.geometry("360x600")
        wrapper_mk2ta = LabelFrame(mk2ta, text="mata kuliah")
        wrapper_mk2ta.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ta = tk.Label(wrapper_mk2ta,text="PILIH MATA KULIAH")
        lbl_gmk2ta.place(x=100,y=10)
        # create btn
        def takombig_2ta():
            recogabsen.recabsen.kombig_2ta()
        btn_mk1_2ta = tk.Button(wrapper_mk2ta,text="Komputasi Big Data", width=30, height=2, command=takombig_2ta)
        btn_mk1_2ta.place(x=50, y=40)
        def tapai_2ta():
            recogabsen.recabsen.pai_2ta()
        btn_mk2_2ta = tk.Button(wrapper_mk2ta,text="Pendidikan Agama Islam", width=30, height=2, command=tapai_2ta)
        btn_mk2_2ta.place(x=50, y=85)
        def tahidroR_2ta():
            recogabsen.recabsen.hidroR_2ta()
        btn_mk3_2ta = tk.Button(wrapper_mk2ta,text="Rekayasa Hidrologi/R", width=30, height=2, command=tahidroR_2ta)
        btn_mk3_2ta.place(x=50, y=130)
        def tataktentuR_2ta():
            recogabsen.recabsen.taktentuR_2ta()
        btn_mk4_2ta = tk.Button(wrapper_mk2ta,text="Analisis Struk.Statis Tak Tentu/R", width=30, height=2, command=tataktentuR_2ta)
        btn_mk4_2ta.place(x=50, y=175)
        def tahidrolikaR_2ta():
            recogabsen.recabsen.hidrolikaR_2ta()
        btn_mk5_2ta = tk.Button(wrapper_mk2ta,text="Hidrolika/R *", width=30, height=2, command=tahidrolikaR_2ta)
        btn_mk5_2ta.place(x=50, y=220)
        def talalulintas_2ta():
            recogabsen.recabsen.lalulintas_2ta()
        btn_mk6_2ta = tk.Button(wrapper_mk2ta,text="Rekayasa Lalu Lintas", width=30, height=2, command=talalulintas_2ta)
        btn_mk6_2ta.place(x=50, y=265)
        def tahidrolika_2ta():
            recogabsen.recabsen.hidrolika_2ta()
        btn_mk7_2ta = tk.Button(wrapper_mk2ta,text="Hidrolika *", width=30, height=2, command=tahidrolika_2ta)
        btn_mk7_2ta.place(x=50, y=310)
        def tatanah_2ta():
            recogabsen.recabsen.tanah_2ta()
        btn_mk8_2ta = tk.Button(wrapper_mk2ta,text="Mekanika Tanah *", width=30, height=2, command=tatanah_2ta)
        btn_mk8_2ta.place(x=50, y=355)
        def tataktentu_2ta():
            recogabsen.recabsen.taktentu_2ta()
        btn_mk9_2ta = tk.Button(wrapper_mk2ta,text="Analisis Struk. Statis Tak Tentu", width=30, height=2, command=tataktentu_2ta)
        btn_mk9_2ta.place(x=50, y=400)
        def takonstruksi_2ta():
            recogabsen.recabsen.konstruksi_2ta()
        btn_mk10_2ta = tk.Button(wrapper_mk2ta, text="Manajemen Konstruksi", width=30, height=2, command=takonstruksi_2ta)
        btn_mk10_2ta.place(x=50, y=445)
        def tarekayasa_2ta():
            recogabsen.recabsen.rekayasa_2ta()
        btn_mk11_2ta = tk.Button(wrapper_mk2ta, text="Rekayasa Hidrologi", width=30, height=2, command=tarekayasa_2ta)
        btn_mk11_2ta.place(x=50, y=490)
        mk2ta.mainloop()
    def mk3ta():
        mk3ta = tk.Tk()
        mk3ta.title("FR SYSTEM")
        mk3ta.geometry("360x750")
        wrapper_mk3ta = LabelFrame(mk3ta, text="mata kuliah")
        wrapper_mk3ta.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ta = tk.Label(wrapper_mk3ta,text="PILIH MATA KULIAH")
        lbl_gmk3ta.place(x=100,y=10)
        # create btn
        def tajembatanR_3ta():
            recogabsen.recabsen.jembatanR_3ta()
        btn_mk1_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Struktur Jembatan /R", width=30, height=2, command=tajembatanR_3ta)
        btn_mk1_3ta.place(x=50, y=40)
        def tabaja2R_3ta():
            recogabsen.recabsen.baja2R_3ta()
        btn_mk2_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Struktur Baja 2/R", width=30, height=2, command=tabaja2R_3ta)
        btn_mk2_3ta.place(x=50, y=85)
        def tajalanR_3ta():
            recogabsen.recabsen.jalanR_3ta()
        btn_mk3_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Perkerasan Jalan/R *", width=30, height=2, command=tajalanR_3ta)
        btn_mk3_3ta.place(x=50, y=130)
        def tanumerik_3ta():
            recogabsen.recabsen.numerik_3ta()
        btn_mk4_3ta = tk.Button(wrapper_mk3ta,text="Metode Numerik", width=30, height=2, command=tanumerik_3ta)
        btn_mk4_3ta.place(x=50, y=175)
        def taulang2R_3ta():
            recogabsen.recabsen.tulang2R_3ta()
        btn_mk5_3ta = tk.Button(wrapper_mk3ta,text="Peranc.Stru.Beton Bertulang 2/R", width=30, height=2, command=taulang2R_3ta)
        btn_mk5_3ta.place(x=50, y=220)
        def tapondasi_3ta():
            recogabsen.recabsen.pondasi_3ta()
        btn_mk6_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Pondasi Dalam", width=30, height=2, command=tapondasi_3ta)
        btn_mk6_3ta.place(x=50, y=265)
        def tapraktek_3ta():
            recogabsen.recabsen.praktek_3ta()
        btn_mk7_3ta = tk.Button(wrapper_mk3ta,text="Kerja Praktek", width=30, height=2, command=tapraktek_3ta)
        btn_mk7_3ta.place(x=50, y=310)
        def tajembatan_3ta():
            recogabsen.recabsen.jembatan_3ta()
        btn_mk8_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Struktur Jembatan", width=30, height=2, command=tajembatan_3ta)
        btn_mk8_3ta.place(x=50, y=355)
        def tajalan_3ta():
            recogabsen.recabsen.jalan_3ta()
        btn_mk9_3ta = tk.Button(wrapper_mk3ta,text="Perancangan Perkerasan Jalan *", width=30, height=2, command=tajalan_3ta)
        btn_mk9_3ta.place(x=50, y=400)
        def tabaja_3ta():
            recogabsen.recabsen.baja_3ta()
        btn_mk10_3ta = tk.Button(wrapper_mk3ta, text="Perancangan Struktur Baja 2", width=30, height=2, command=tabaja_3ta)
        btn_mk10_3ta.place(x=50, y=445)
        def tagraf_3ta():
            recogabsen.recabsen.graf_3ta()
        btn_mk11_3ta = tk.Button(wrapper_mk3ta, text="Terapan Teori Graf", width=30, height=2, command=tagraf_3ta)
        btn_mk11_3ta.place(x=50, y=490)
        def tadalamR_3ta():
            recogabsen.recabsen.dalamR_3ta()
        btn_mk12_3ta = tk.Button(wrapper_mk3ta, text="Perancangan Pondasi Dalam/R", width=30, height=2, command=tadalamR_3ta)
        btn_mk12_3ta.place(x=50, y=535)
        def taulang_3ta():
            recogabsen.recabsen.tulang_3ta()
        btn_mk13_3ta = tk.Button(wrapper_mk3ta, text="Peranc. Struk.Beton Bertulang 2", width=30, height=2, command=taulang_3ta)
        btn_mk13_3ta.place(x=50, y=580)
        def taudara_3ta():
            recogabsen.recabsen.udara_3ta()
        btn_mk14_3ta = tk.Button(wrapper_mk3ta, text="Perancangan Pelabuhan Udara", width=30, height=2, command=taudara_3ta)
        btn_mk14_3ta.place(x=50, y=625)
        mk3ta.mainloop()
    def mk4ta():
        mk4ta = tk.Tk()
        mk4ta.title("FR SYSTEM")
        mk4ta.geometry("360x360")
        wrapper_mk4ta = LabelFrame(mk4ta, text="mata kuliah")
        wrapper_mk4ta.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ta = tk.Label(wrapper_mk4ta,text="PILIH MATA KULIAH")
        lbl_gmk4ta.place(x=100,y=10)
        # create btn
        def tarobot_4ta():
            recogabsen.recabsen.robot_4ta()
        btn_mk1_4ta = tk.Button(wrapper_mk4ta,text="Robotika Cerdas", width=30, height=2, command=tarobot_4ta)
        btn_mk1_4ta.place(x=50, y=40)
        def tatanah_4ta():
            recogabsen.recabsen.tanah_4ta()
        btn_mk2_4ta = tk.Button(wrapper_mk4ta,text="Rekayasa Perbaikan Tanah", width=30, height=2, command=tatanah_4ta)
        btn_mk2_4ta.place(x=50, y=85)
        def tabeton_4ta():
            recogabsen.recabsen.beton_4ta()
        btn_mk3_4ta = tk.Button(wrapper_mk4ta,text="Material Beton Berkelanjutan", width=30, height=2, command=tabeton_4ta)
        btn_mk3_4ta.place(x=50, y=130)
        def tautilitas_4ta():
            recogabsen.recabsen.utilitas_4ta()
        btn_mk4_4ta = tk.Button(wrapper_mk4ta,text="Utilitas Bangunan", width=30, height=2, command=tautilitas_4ta)
        btn_mk4_4ta.place(x=50, y=175)
        mk4ta.mainloop()

# KOMUNIKASI
    def mk1ma():
        mk1ma = tk.Tk()
        mk1ma.title("FR SYSTEM")
        mk1ma.geometry("360x540")
        wrapper_mk1ma = LabelFrame(mk1ma, text="mata kuliah")
        wrapper_mk1ma.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk1ma = tk.Label(wrapper_mk1ma,text="PILIH MATA KULIAH")
        lbl_gmk1ma.place(x=100,y=10)
        # create btn
        def makomunikasi_1ma():
            recogabsen.recabsen.komunikasi_1ma()
        btn_mk1_1ma = tk.Button(wrapper_mk1ma,text="Teori Komunikasi *", width=30, height=2, command=makomunikasi_1ma)
        btn_mk1_1ma.place(x=50, y=40)
        def maprocess_1ma():
            recogabsen.recabsen.process_1ma()
        btn_mk2_1ma = tk.Button(wrapper_mk1ma,text="Algoritma Pemrog. 2(Processing)**", width=30, height=2, command=maprocess_1ma)
        btn_mk2_1ma.place(x=50, y=85)
        def mapai_1ma():
            recogabsen.recabsen.pai_1ma()
        btn_mk3_1ma = tk.Button(wrapper_mk1ma,text="Pendidikan Agama Islam", width=30, height=2, command=mapai_1ma)
        btn_mk3_1ma.place(x=50, y=130)
        def madigiciti_1ma():
            recogabsen.recabsen.digiciti_1ma()
        btn_mk4_1ma = tk.Button(wrapper_mk1ma,text="Digital Citizenship", width=30, height=2, command=madigiciti_1ma)
        btn_mk4_1ma.place(x=50, y=175)
        def mabing_1ma():
            recogabsen.recabsen.bing_1ma()
        btn_mk5_1ma = tk.Button(wrapper_mk1ma,text="Bahasa Inggris 2", width=30, height=2, command=mabing_1ma)
        btn_mk5_1ma.place(x=50, y=220)
        def mapkn_1ma():
            recogabsen.recabsen.pkn_1ma()
        btn_mk6_1ma = tk.Button(wrapper_mk1ma,text="Pendidikan Kewarganegaraan", width=30, height=2, command=mapkn_1ma)
        btn_mk6_1ma.place(x=50, y=265)
        def mabindo_1ma():
            recogabsen.recabsen.bindo_1ma()
        btn_mk7_1ma = tk.Button(wrapper_mk1ma,text="Bahasa Indonesia", width=30, height=2, command=mabindo_1ma)
        btn_mk7_1ma.place(x=50, y=310)
        def masosio_1ma():
            recogabsen.recabsen.sosio_1ma()
        btn_mk8_1ma = tk.Button(wrapper_mk1ma,text="Sosiologi Komunikasi & Informasi", width=30, height=2, command=masosio_1ma)
        btn_mk8_1ma.place(x=50, y=355)
        def majurnalis_1ma():
            recogabsen.recabsen.jurnalis_1ma()
        btn_mk9_1ma = tk.Button(wrapper_mk1ma,text="Dasar-Dasar Jurnalistik */**", width=30, height=2, command=majurnalis_1ma)
        btn_mk9_1ma.place(x=50, y=400)
        mk1ma.mainloop()
    def mk2ma():
        mk2ma = tk.Tk()
        mk2ma.title("FR SYSTEM")
        mk2ma.geometry("360x500")
        wrapper_mk2ma = LabelFrame(mk2ma, text="mata kuliah")
        wrapper_mk2ma.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk2ma = tk.Label(wrapper_mk2ma,text="PILIH MATA KULIAH")
        lbl_gmk2ma.place(x=100,y=10)
        # create btn
        def masocnet_2ma():
            recogabsen.recabsen.socnet_2ma()
        btn_mk1_2ma = tk.Button(wrapper_mk2ma,text="Social Networking & Creative Cont", width=30, height=2, command=masocnet_2ma)
        btn_mk1_2ma.place(x=50, y=40)
        def mamanaj_2ma():
            recogabsen.recabsen.manaj_2ma()
        btn_mk2_2ma = tk.Button(wrapper_mk2ma,text="Manajemen & Komunikasi Organisasi", width=30, height=2, command=mamanaj_2ma)
        btn_mk2_2ma.place(x=50, y=85)
        def mahuman_2ma():
            recogabsen.recabsen.human_2ma()
        btn_mk3_2ma = tk.Button(wrapper_mk2ma,text="Human Relations *", width=30, height=2, command=mahuman_2ma)
        btn_mk3_2ma.place(x=50, y=130)
        def magrafkom_2ma():
            recogabsen.recabsen.grafkom_2ma()
        btn_mk4_2ma = tk.Button(wrapper_mk2ma,text="Grafika Komp.untuk Komunikasi **", width=30, height=2, command=magrafkom_2ma)
        btn_mk4_2ma.place(x=50, y=175)
        def maopini_2ma():
            recogabsen.recabsen.opini_2ma()
        btn_mk5_2ma = tk.Button(wrapper_mk2ma,text="Opini Publik", width=30, height=2, command=maopini_2ma)
        btn_mk5_2ma.place(x=50, y=220)
        def maradio_2ma():
            recogabsen.recabsen.radio_2ma()
        btn_mk6_2ma = tk.Button(wrapper_mk2ma,text="Peng. Teknologi Radio & TV **", width=30, height=2, command=maradio_2ma)
        btn_mk6_2ma.place(x=50, y=265)
        def mastat_2ma():
            recogabsen.recabsen.stat_2ma()
        btn_mk7_2ma = tk.Button(wrapper_mk2ma,text="Statistika 2 **", width=30, height=2, command=mastat_2ma)
        btn_mk7_2ma.place(x=50, y=310)
        def maedia_2ma():
            recogabsen.recabsen.media_2ma()
        btn_mk8_2ma = tk.Button(wrapper_mk2ma,text="Media Relations *", width=30, height=2, command=maedia_2ma)
        btn_mk8_2ma.place(x=50, y=355)
        mk2ma.mainloop()
    def mk3ma():
        mk3ma = tk.Tk()
        mk3ma.title("FR SYSTEM")
        mk3ma.geometry("360x470")
        wrapper_mk3ma = LabelFrame(mk3ma, text="mata kuliah")
        wrapper_mk3ma.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk3ma = tk.Label(wrapper_mk3ma,text="PILIH MATA KULIAH")
        lbl_gmk3ma.place(x=100,y=10)
        # create btn
        def mapi_3ma():
            recogabsen.recabsen.pi_3ma()
        btn_mk1_3ma = tk.Button(wrapper_mk3ma,text="Tatap Muka Penulisan Ilmiah", width=30, height=2, command=mapi_3ma)
        btn_mk1_3ma.place(x=50, y=40)
        def maultimed_3ma():
            recogabsen.recabsen.multimed_3ma()
        btn_mk2_3ma = tk.Button(wrapper_mk3ma,text="Sistem Multimedia 2", width=30, height=2, command=maultimed_3ma)
        btn_mk2_3ma.place(x=50, y=85)
        def maetika_3ma():
            recogabsen.recabsen.etika_3ma()
        btn_mk3_3ma = tk.Button(wrapper_mk3ma,text="Etika & Filsafat Komunikasi", width=30, height=2, command=maetika_3ma)
        btn_mk3_3ma.place(x=50, y=130)
        def manaskah_3ma():
            recogabsen.recabsen.naskah_3ma()
        btn_mk4_3ma = tk.Button(wrapper_mk3ma,text="Penulisan Naskah Komunikasi II", width=30, height=2, command=manaskah_3ma)
        btn_mk4_3ma.place(x=50, y=175)
        def maevent_3ma():
            recogabsen.recabsen.event_3ma()
        btn_mk5_3ma = tk.Button(wrapper_mk3ma,text="Event Management", width=30, height=2, command=maevent_3ma)
        btn_mk5_3ma.place(x=50, y=220)
        def makampanye_3ma():
            recogabsen.recabsen.kampanye_3ma()
        btn_mk6_3ma = tk.Button(wrapper_mk3ma,text="Perencanaan Kampanye Komunikasi", width=30, height=2, command=makampanye_3ma)
        btn_mk6_3ma.place(x=50, y=265)
        def masabigdat_3ma():
            recogabsen.recabsen.sabigdat_3ma()
        btn_mk7_3ma = tk.Button(wrapper_mk3ma,text="Sains Data & Analisis Big Data", width=30, height=2, command=masabigdat_3ma)
        btn_mk7_3ma.place(x=50, y=310)
        mk3ma.mainloop()
    def mk4ma():
        mk4ma = tk.Tk()
        mk4ma.title("FR SYSTEM")
        mk4ma.geometry("360x360")
        wrapper_mk4ma = LabelFrame(mk4ma, text="mata kuliah")
        wrapper_mk4ma.pack(fill="both", expand="yes", padx=20, pady=10)
        # create label Greeting
        lbl_gmk4ma = tk.Label(wrapper_mk4ma,text="PILIH MATA KULIAH")
        lbl_gmk4ma.place(x=100,y=10)
        # create btn
        def macyber_4ma():
            recogabsen.recabsen.cyber_4ma()
        btn_mk1_4ma = tk.Button(wrapper_mk4ma,text="Cyber Public Relations", width=30, height=2, command=macyber_4ma)
        btn_mk1_4ma.place(x=50, y=40)
        def mamasy_4ma():
            recogabsen.recabsen.masy_4ma()
        btn_mk2_4ma = tk.Button(wrapper_mk4ma,text="Kecerdasan Artifisial & Masy.", width=30, height=2, command=mamasy_4ma)
        btn_mk2_4ma.place(x=50, y=85)
        def mapsikologi_4ma():
            recogabsen.recabsen.psikologi_4ma()
        btn_mk3_4ma = tk.Button(wrapper_mk4ma,text="Psikologi Komunikasi", width=30, height=2, command=mapsikologi_4ma)
        btn_mk3_4ma.place(x=50, y=130)
        def matourism_4ma():
            recogabsen.recabsen.tourism_4ma()
        btn_mk4_4ma = tk.Button(wrapper_mk4ma,text="Tourism Communication", width=30, height=2, command=matourism_4ma)
        btn_mk4_4ma.place(x=50, y=175)
        mk4ma.mainloop()