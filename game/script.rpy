# default score = 0 
# default yuuki_affection = 0

# Define points here!
label start:
    $ hp_pts = 50
    $ opp_pts = 1
    $ exp_pts = 20
    $ health = 50
# show screen StatsUI

# play music "music/bensound-littleidea.mp3"

# "{cps=25}Tika.. Itulah namaku.. "
# "{cps=25}Ayahku bekerja sebagai petugas konservasi alam"
# "{cps=25}Aku becita-cita untuk seperti ayahku"
# "{cps=25}Dan berikut adalah kisah petualanganku"
########## ########## ##########   CERITA  WAKTU DIRUMAH ########## ########## ########## ########## ########## 

show screen health_bar
show screen score()
show screen gameUI

scene bg rumah2d with fade
show Tika SD awal at kanan with movef
"{cps=20}Alkisah adalah seorang anak bernama TIKA"
show Tika SD awal at kiri with movef
"{cps=20}TIKA adalah Putri dari Pak Fahmi dan Bu Aida."
hide Tika SD awal 

scene bg sekolah2d #BG diatas karakter
show Tika SD red at tengah
"{cps=20}Saat ini TIKA duduk di bangku Sekolah Dasar kelas 1."
"{cps=20}TIKA adalah anak yang periang dan suka membantu temannya."
hide Tika SD red

scene bg ruang makan
show Ayah starter
"{cps=20}Bapak fahmi adalah ayah dari tika dia bekerja sebagai guru smp "
"{cps=20}Fahmi ayah yang baik hati sangat menyayangi keluarganya dan anaknya"
hide Ayah Tika starter with dissolve

show Rika
"{cps=20}TIKA memiliki seorang adik perempuan namanya Rika"
"{cps=20}Rika berumur 5 tahun"
hide Rika with dissolve

show ibu starter
"{cps=20}Bu Aida adalah seorang ibu rumah tangga "
"{cps=20}Bu Aida seorang ibu yang memiliki wajah yang menarik dan sayang pada kedua anaknya"
hide ibu starter with dissolve

show ibu kedip
"{cps=20}Bu aida memiliki rambut yang ikal dan hitam "
"{cps=20}Bu aida sering membantu tetangga yang kesulitan."
hide ibu kedip with dissolve
jump sdkelas1


#======================#   #======================#   #======================#

# scene bg ruang makan
# show ibu kuatir
# i "{cps=20}Tika bisa bantu ibu sebentar?"
# i "{cps=20}Tolong beli gula di toko sebelah"
# menu:
#     "Iya bu":
#         # $yuuki_affection = yuuki_affection + 1
#         $ player_pts += 20 #MENAMBAH SCORE
#         $ opp_pts += 2  
#         $ health = 40
#         jump pilihan_beli_gula
#     "Sebentar bu":
#         $ player_pts -=10  # MENGKURANGI SCORE 
#         $ health -= 10
#         jump pilihan_sebentar

# label pilihan_beli_gula:
# scene bg ruang makan
# show Tika senang
# t "{cps=20}baik bu tika belikan"
# show Tika senyum
# t "{cps=20}beli berapa nih?"
# i senyum "{cps=20}beli satu aja"  # Side image
# hide Tika senang
# # show Tika senyum #with moveinleft
# t senyum "{cps=20}aku berangkat dulu"

# scene bg Toko Gula1
# t "{cps=20}akhirnya sampai juga di toko"
# show pak edi senyum
# pa "{cps=20}eh dek tika, mau beli apa?"
# t senyum "{cps=20}iya tadi disuruh ibu beli gula"
# show pak edi kedip
# pa "{cps=20}pinter banget dek"
# pa "{cps=20}tunggu sebentar ya"
# hide pak edi kedip

# scene loading with fade
# with Pause(8)
# stop music fadeout 2.0

# scene bg Toko Gula1
# play music "music/bensound-littleidea.mp3"

# show pak edi gula
# pa "{cps=20}ini gulanya"
# t senyum "{cps=20}terima kasih kak"
# pa "{cps=20}sama-sama hati hati ya dijalan"
# scene bg ruang makan
# show Tika senang
# t "{cps=20}ini bu gulanya ada kembaliannya nih"
# hide Tika senang
# show ibu diam
# i "{cps=20}wah anak ibu pinter banget"
# hide ibu diam
# show ibu bicara
# i "{cps=20}kembaliannya ambil saja"
# t "{cps=20}terimakasih bu"
# jump chapter2

# label pilihan_sebentar:
# t "{cps=20}Sebentar bu tika lagi asyik nonton tv"
# i "{cps=20}loh jadi beli gak nih?"
# t "{cps=20}oh iya bu lupa"
# i "{cps=20}kalau begitu ibu saja yang beli sendiri"
# jump chapter2

# ##########  CERITA  WAKTU DIRUMAH END
# label chapter2:
# scene bg langit
# "KEESOKAN HARINYA" 
# t "{cps=20}Matahari pagi sudah terbit menyambut pagi" ################ CERITA PAS SEKOLAH
# scene bg kamar tidur bed with wiperight
# t "{cps=20}Terdengar suara ibu yang membangunkanku"
# show Tika Tidur
# t "{cps=20}Nanti bu sebentar lagi"
# scene bg kamar tidur door with hpunch

# show ibu marah # Posisi Kiri
# i "{cps=20}Nanti terlambat sekolah loh"
# hide ibu marah  # Posisi Kiri
# show ibu kuatir
# i "{cps=20}hampir jam 7 loh"
# hide ibu kuatir
# scene bg kamar tidur bed with vpunch
# show Tika Ngigau
# t "{cps=20}aduh beneran udah mau jam 7"
# show Tika Kaget
# t "{cps=20}Aduh aku lupa kalau ada piket hari ini"
# hide Tika Kaget

# scene bg ruang makan
# show fahmi curiga 
# a "{cps=20}untung saja ibu membangunkanmu"
# a "{cps=20}kalau begitu segera mandi dan persiapan berangkat sekolah"
# a "{cps=20}sudah sarapan belum?"
# hide fahmi curiga
# show Tika Mager 
# t "{cps=20}belum, waktunya nggak sempat keburu terlambat"
# hide Tika Mager
# show Tika Ingat 
# t "{cps=20}aku teringat ternyata hari ini ada jadwal piketku dikelas"
# show ibu diam at right with moveinright # Posisi dari kanan kekiri
# i "{cps=20}untuk uang sakunya udah ibu masukkan tas"
# show ibu bicara
# i "{cps=20}dan minumannya juga sudah ibu masukkan tas"
# show Tika Bicara with moveinright
# # hide ibu bicara at right with moveoutright
# t "{cps=20}aku berangkat dulu"
# show Tika Senyum with moveinleft # Posisi Kiri
# pause(3.0)
# hide Tika Senyum with moveoutleft # Posisi Kiri
# pause(3.0)
# hide Tika Bicara 
# hide ibu diam at right with moveinright 

# hide Tika Mager
# show ibu bicara 
# i "{cps=20}hati hati ya dijalan"
# hide ibu diam
# jump chapter1a

#======================#   #======================#   #======================#


    # label questioningends:
    # if score >= 3:
    #     t "Selamat ilihanmu benar semua"
    #     "Kamu memperoleh nilai yang baik"
    # elif score == 2:
    #     "Teacher" "Not bad."
    # else:
    #     "Teacher" "GET OUT!" with hpunch

    # "Permainan Berakhir"
    # return
    
    # label score_increased:
    # $ score += 20
    # "Selamat Jawabanmu Benar"



# # jump chapter1
# screen StatsUI:
#     # add "UI/bg peach.png"
#     frame:
#         xalign 0.98 ### Posisi Kotak kanan atau kiri 0.5
#         yalign 0.04 ### Posisi Kotak score kebawah
#         xpadding 20 ## Posisi margin
#         ypadding 20 ## Posisi margin

#         hbox:
#             spacing 40
#             # Text Column

#             vbox:
#                 # # spacing 10
#                 text "Score" size 40 ### menampilkan teks sja
#                 # text "Charm" size 40
#                 # text "Tika" size 40
#                 # text "Kindness" size 40
#                 # text "Proficiency" size 40

#             # Values Column     
#             vbox:    
#                 spacing 10
#                 text str(score) size 40 ### menampilkan point sja

# ## This was copied from "Point and Click Sample Project" by SusanTheCat
# ## https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=20541

# screen displayTextScreen:  
#     default displayText = ""
#     vbox:
#         xalign 0.5
#         yalign 0.5
#         frame:
#             text displayText