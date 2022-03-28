# default currenthp = 75
# default kurangihp = 50
# default maxhp = 100
#define r = Character('Raven', color="#ffffff", image="Raven")
image ctc_anchored:
       "gui/ctc.png"
       yalign 0.96 xalign 0.95 #Adjust these numbers to fit your own textbox
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 


define t = Character('Tika', 
        color="#ffffff",
        ctc="ctc_anchored")
image define tika senyum = "side tika senyum.png"

define f = Character('Fahmi ', color="#ffffff")
define r = Character('Rika ', color="#ffffff")
define i = Character("Ibu", color="#ffffff", image="ibu")
image define ibu senyum = "side ibu senyum.png"

define a = Character('Ayah Tika', color="#ffffff")
define bs = Character('Bu Iska', color="#ffffff")
define pi = Character('Pak Indra', color="#ffffff")
define ay = Character('Ayu', color="#c8ffc8")
define pa = Character('Kak Adi', color="#ffffff")
# define t = Character('Tika', color="#09090a", show_two_window=True, ctc="ctc_blink",
#         ctc_position="nestled", show_side_image=Image("Tika", xalign=0.0, yalign=1.0))

image ctc_blink:
       "gui/ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 

image black ="#000"


define N = Character(' ', color="#c8ffc8")
#narator

define b20 = Character('bar20', color="#c8ffc8")

# Deklarasikan karakter yang digunakan di game.


##Image Chapter Pemisah
image prolog 01 = "images/Prolog 01.png"
image prolog 02 = "images/Prolog 02.png"

image b20 = "bar/hp30.png"
image b30 = "bar/hp60.png"

# Animasi
image Tikab:
    "Tika-diam-senyum.png"
    1.0
    "Tika-diam-senyum-kedip.png" with Dissolve(0.5, alpha=True)
    1.0
    repeat


image Tika SD awal = "images/Tika/Tika_Hodie_senyum.png"
image Tika SD red = "images/Tika/Tika_Hodie_SD.png"
image Ayah starter = "images/Tika/ayahh.png"
image ibu starter = "images/Tika/ibu1.png"
image ibu kedip = "images/Tika/ibu2.png"
image Rika = "images/Tika/Rika_senyum.png"
image Rika senyum = "images/Tika/Rika_senyum2.png"
image Rika nangis = "images/Tika/Rika_nangis.png"
image Rika menangis = "images/Tika/Rika_nangis2.png"
image penjual gulali = "images/Tika/penjual gulali_before.png"
image Rika menangis = "images/Tika/Rika_nangis2.png"
image Tika menyerahkan_1 = "images/Tika/Tika_menyerahkan_balon.png"
image Tika menyerahkan_2 = "images/Tika/Tika_menyerahkan_end.png"
image Rika menerima_1 = "images/Tika/Rika_senyum_menerima.png"


image main dakon = "images/Tika/main-dakon.png"




image Tika senang = "images/Tika/Tika_Hodie_senang.png"
image Tika senyum = "images/Tika/Tika_Hodie_senyum.png"

image fahmi curiga = "images/fahmi/bk1.png"

image ibu marah = "images/ibu/ib1.png"
image ibu kuatir = "images/ibu/ib2.png"
image ibu diam = "images/ibu/ib3.png"
image ibu bicara = "images/ibu/ib4.png"

image pak edi senyum = "images/pak edi/pe1.png"
image pak edi kedip = "images/pak edi/pe3.png"
image pak edi gula = "images/pak edi/pe4.png"

#################### ========================   ANIMASI GAMBAR ==================
screen animasi:
    add "mages"

image animasi_bintang:
        "images/trophy_icon2.png"
        yalign .2 xalign .5
        linear 1.0 xalign .1 yalign .0 # yalign posisi kanan ke kiri semaakin besar ke kekiri semkn kcil naik



image mages:
        "images/trophy_icon2.png"
        yalign 1 subpixel True
        
        parallel:
            xalign .5
            linear 1.0 xalign 0.0 # menurun kiri 1.0 jika yalign
            linear 0.1 xalign .25
            repeat

        parallel:
            alpha 1.0 zoom 2.0
            linear .3 alpha .5 zoom .9
            linear .5 alpha .9 zoom 1.0
            repeat

        parallel:
            rotate 0
            linear 3 rotate 360
            repeat

#################### ========================   GAMBAR BACKGROUND ==================
image bg rumah2d = "images/BG/rumah 2d.png"
image bg sekolah2d = "images/BG/sekolah.png"
image bg halaman rumah = "images/BG/background_awal.png"
image bg penjual = "images/BG/bang-gulali.jpg"
image bg balon nyangkut = "images/BG/balon_nyangkut.jpg"
image bg balon lepas = "images/BG/balon_lepass.jpg"
image bg ruang kelas sd = "images/BG/ruang kelas.jpg"



image loading = "images/BG/loading.jpg"
image bg nontontv = "images/BG/nonton-tv.jpg"
image bg gading = "images/BG/gading.jpg"
image bg kamar kotor = "images/BG/bed-kotor.jpg"
image bg kamar bersih = "images/BG/bed-bersih.jpg"
image bg kamar tidur bed = "images/BG/PlayerHomeM_Morning3.png"
image bg kamar tidur door = "images/BG/PlayerHomeM_Morning2.png"
image bg Toko Gula1 = "images/BG/toko-gula1.jpg"

## RUANG MAKAN
image bg ruang makan = "images/BG/ruang-makan.png"
image bg langit = "images/BG/langit.jpg"
image bg sekolah = "images/BG/sekolah.jpg"
image bg kelas = "images/BG/kelas.jpg"

image bg rumah = "images/BG/rumah.png"
image bg rumah sore = "images/BG/rumah sore.jpg"
image bg jalan = "images/BG/jalan.png"
image bg sampah_kotor = "images/BG/sampah_berserakan.png"
image bg sampah_bersih = "images/BG/bersih.png"
##################################################### POSISI KARAKTER / TRANSFORM #######
transform tengah:
    xalign 0.5
    yalign 1.0
transform kanan:
    xalign 0.75
    yalign 1.0
transform nganan:
    xalign 0.85
    yalign 1.0
transform pojokkanan:
    xalign 1.0
    yalign 1.0
transform kiri:
    xalign 0.25
    yalign 1.0
transform ngiri:
    xalign 0.15
    yalign 1.0
transform pojokkiri:
    xalign 0.0
    yalign 1.0

##################################################### POSISI KARAKTER / TRANSFORM #######

image Tika = Null()
image Tika diam = Null()
image Tika mulai = Null()
image Tika kaget = Null()
# image Tika senyum = Null()
image Tika kedip = Null()

image side Tika = "images/side/side_1.png"
image side Tika diam = "images/side/side_1.png"
image side Tika mulai = "images/side/side_2.png"
image side Tika kaget = "images/side/side_3.png"
image side Tika senyum = "images/side/side_4.png"
image side Tika kedip = "images/side/side_5.png"

define gerakan_kiri = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)
define gerakan_kanan = ComposeTransition(dissolve, before=moveoutright, after=moveinleft)

init:

    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ move = MoveTransition(1.0)
    $ movef = MoveTransition(0.40)
    $ quickDissolve = Dissolve(0.1)

define kiri = Position(xpos=0.15, xanchor='left',ypos=0.35, yanchor=0.33)
define kiri_atas = Position(xpos=0.15, xanchor='left',ypos=0.60, yanchor=0.60)
define kiri_atas_2 = Position(xpos=0.14, xanchor='left',ypos=0.60, yanchor=0.60)
define kanan = Position(xpos=0.85, xanchor='right',ypos=0.35, yanchor=0.33)
define kanan_2 = Position(xpos=0.86, xanchor='right',ypos=0.35, yanchor=0.33)
define kanan_3 = Position(xpos=0.85, xanchor='right',ypos=0.36, yanchor=0.33)
define kanan_atas = Position(xpos=0.85, xanchor='right',ypos=0.60, yanchor=0.60)
define kanan_atas_2 = Position(xpos=0.85, xanchor='right',ypos=0.61, yanchor=0.60)
define kanan_atas_3 = Position(xpos=0.86, xanchor='right',ypos=0.60, yanchor=0.60)
define tengah = Position(xpos=0.5, xanchor='center',ypos=0.35, yanchor=0.33)
define tengah_2 = Position(xpos=0.6, xanchor='center',ypos=0.35, yanchor=0.33)
define tengah_atas = Position(xpos=0.5, xanchor='center',ypos=0.60, yanchor=0.60)
define tengah_atas_2 = Position(xpos=0.6, xanchor='center',ypos=0.60, yanchor=0.60)
define tengah_atas_3 = Position(xpos=0.5, xanchor='center',ypos=0.36, yanchor=0.33)

define wiperight = CropMove(1.0, "wiperight")
define wipeleft = CropMove(1.0, "wipeleft")
define wipeup = CropMove(1.0, "wipeup")
define wipedown = CropMove(1.0, "wipedown")  


define pojok = Position(xpos=0.9, xanchor='left',ypos=0.30, yanchor=0.50)
define pojok2 = Position(xpos=0.87,ypos=0.1, yanchor=0.65)

# cara penggunaan : show lisa senang at kanan_atas with movef


    