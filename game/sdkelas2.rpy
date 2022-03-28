# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# The game starts here.

# This shows a character sprite. 

# These display lines of dialogue.

label sdkelas2:

######### ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 1

"{cps=20}Kini Tika duduk dibangku kelas 2 SD"
"{cps=20}Pada pagi itu aku bangun pagi dan segera berangkat kesekolah"
show Tika senyum
t "{cps=20}Aku pun masuk kelas dan menunggu kelas dimulai"
hide Tika senyum
bs "{cps=20}Selamat pagi anak-anak kini kalian berada dikelas 2"
bs "{cps=20}saya biasa dipanggil bu iska"
bs "{cps=20}bagi yang ingin bertanya silahkan bertanya"
show Tika senyum
menu:
    "Bertanya":
        # $yuuki_affection = yuuki_affection + 1
        $ health +=5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 2
        jump bertanya
    "Tidak":
        $ health -=5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump tidak_bertanya

label bertanya:
scene bg balon lepas
show Tika menyerahkan_1 at tengah 
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}saya bu mau bertanya"
show Tika menyerahkan_2 at tengah
show Rika menerima_1 at kanan 
hide Tika SD
jump stage7

label tidak_bertanya:
scene bg ruang makan
show Tika SD awal
t "{cps=20}karena terlalu malu aku tidak bertanya" 
hide Tika SD awal
jump stage7

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 6

label stage7:
# show tika disini
# show Tika senyum at tengah
scene bg ruang kelas sd
pi "{cps=20}Selamat pagi anak- anak saya mengajar materi pelajaran ppkn"
pi "{cps=20}Lingkungan sangat penting bagi kelangsungan hidup bagi makhluk hidup." 
pi "{cps=20}setelah bapak memberi materi tolong dicatat dan dirangkum"
menu:
    "Tidur":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 2
        jump tidur_dikelas
    "Memperhatikan guru":
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 1 
        jump memperhatikan

label tidur_dikelas:
scene bg ruang kelas sd
t "{cps=20}tidak sengaja aku tertidur dikelas"
pi "{cps=20}Tika jangan tidur dikelas!!"
t "{cps=20}iya pak maaf ketiduran"
hide Tika SD
jump stage8

label memperhatikan:
scene bg ruang kelas sd
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}aku memperhatikan pelajaran" 
t "{cps=20}aku menulis dan merangkum materi pelajaran" 
hide Tika SD awal
jump stage8

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 7

label stage8:
# show tika disini
# show Tika senyum at tengah
t "{cps=20}Ayu mendatangiku dan berkata kepadaku"
ay "{cps=20}Tik tadi ada tugas mau gak ikut denganku merangkum materi?" 
ay "{cps=20}Berhubung jam istirahat, mau nggak ikut bersamaku ke perpus?"
menu:
    "Tidak":
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 1 
        jump menolak_rika
    "Ya":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 2
        jump ikut_rika

label ikut_rika:
scene bg ruang kelas sd
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}oke kalau begitu aku ikut" 
t "{cps=20}ayo keperpustakaan bersama" 
return
# jump stage9

label menolak_rika:
scene bg ruang kelas sd
t "{cps=20}maaf aku lagi pengen kekantin dulu"
hide Tika SD
return
# jump stage9
# jump goodend

# label goodend:
#     if health >= 60:
#       t "Kamu mendapatkan ending yang baik"
#       show black
#       centered "{size=25}{b}ENDING YG BAGUS{/size}{/b}"
#       return
#     if health <= 50:
#       t "Kamu mendapatkan ending yang buruk"
#       show black
#       centered "{size=25}{b}ENDING YG BURUK{/size}{/b}"
#       return




# show ibu starter
# i "{cps=20}Tolong ambilkan sapu dibelakang pintu"
# hide ibu starter
# menu:
#     "Baik bu":
#         # $yuuki_affection = yuuki_affection + 1
#         $ health +=10
#         $ hp_pts += 10 #MENAMBAH SCORE
#         $ exp_pts += 2 
#         jump pilihan_baik_bu
#     "Tika Masih main bu":
#         $ health -=5
#         $ hp_pts -= 5 #MENAMBAH SCORE
#         $ exp_pts -= 1 
#         jump tika_masih_main


# label pilihan_baik_bu:
# scene bg ruang makan
# show Tika SD awal
# show screen animasi   #### MENAMPILKAN STAR SCREEN
# pause 1.0
# hide screen animasi with dissolve
# t "{cps=20}baik bu tika ambilkan sapu"
# show Tika SD awal
# i senyum "{cps=20}Terima kasih tika"  # Side image
# hide Tika SD awal
# jump stage2

# label tika_masih_main:
# show Tika SD awal
# t "{cps=20}Tika masih main bu"
# hide Tika SD awal
# show ibu starter
# i "{cps=20}Yasudah kalo masih main"
# hide ibu starter
# jump stage2

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 2
# label stage2:
    
# play music "music/JP Soundworks - Event4.ogg" fadeout 1  # MUSIC
# show Rika nangis
# r " huuuuuuuu "
# hide Rika nangis

# show Rika menangis
# i " Tika adekmu kenapa kok nangis terus?"
# hide Rika menangis
# show Tika SD awal
# t " Itu bu Adek Minta beli permen bu"
# i "kalau begitu tolong belikan permen di toko sebelah"
# menu:
#     "Baik bu":
#         # $yuuki_affection = yuuki_affection + 1
#         $ hp_pts += 2 #MENAMBAH SCORE
#         $ exp_pts += 2 
#         $ health += 10
#         jump pilihan_baik_bu_2
#     "Ndak mau bu tika lagi males":
#         $ hp_pts -=10  # MENGKURANGI SCORE 
#         $ exp_pts -= 1
#         $ health -= 5
#         jump tika_lagi_males


# label pilihan_baik_bu_2:
# scene bg ruang makan
# show Tika SD awal
# show screen animasi   #### MENAMPILKAN STAR SCREEN
# hide screen animasi with dissolve
# t "{cps=20}baik bu tika belikan"
# show Tika SD awal
# t "{cps=20}beli berapa nih?"
# i senyum "{cps=20}beli satu aja"  # Side image
# hide Tika SD awal
# jump stage3

# label tika_lagi_males:
# scene bg ruang makan
# show Tika SD awal
# t "{cps=20}ndak mau bu"
# show Tika SD awal
# t "{cps=20}tika lagi males"
# i senyum "{cps=20}yasudah kalo gitu ibu yang beli"  # Side image
# hide Tika SD awal
# jump stage3
# stop music fadeout 1
 

# ########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 3
# label stage3:
# play music "music/bensound-littleidea.mp3" fadeout 1   # MUSIC
# scene bg halaman rumah
# " Pada saat itu di pagi hari ada penjual gulali keliling"
# " Gulali-gulali "
# show Tika SD awal at kanan
# t "{cps=20}Ibu… ibu… Tika mau beli gulali dan es cao"
# show ibu starter at kiri
# i "{cps=20}Jangan banyak-banyak tika, beli salah satu saja"
# hide ibu starter with dissolve
# hide Tika SD awal with dissolve

# show Tika SD awal at kanan  
# t "{cps=20}Aku mau es sama permen ibu"
# show ibu starter at kiri with movef
# i "{cps=20}Kalau begitu nanti dibagi sama adek ya"
# menu:
#     "Iya bu":
#         # $yuuki_affection = yuuki_affection + 1
#         $ hp_pts += 2 #MENAMBAH SCORE
#         $ exp_pts += 2 
#         $ health += 10
#         jump tika_berbagi
#     "Ndak Bu":
#         $ hp_pts -=10  # MENGKURANGI SCORE 
#         $ exp_pts -= 1
#         $ health -= 5
#         jump tika_tidak_berbagi

# label tika_berbagi:
# scene bg ruang makan
# show Tika SD awal
# show screen animasi   #### MENAMPILKAN STAR SCREEN
# hide screen animasi with dissolve
# t "{cps=20}setelah membeli permen dan es aku berbagi ke adek"
# show Tika SD awal
# r "{cps=20}Terima kasih kakak"
# hide Tika SD awal
# jump stage4

# label tika_tidak_berbagi:
# scene bg ruang makan
# show Tika SD awal
# t "{cps=20}aku akhirnya memakannya sendiri"
# hide Tika SD awal
# jump stage4

# ########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 4
# label stage4:
# play music "music/Folksy Days_Sad.mp3" fadeout 1   # MUSIC
# "Setelah membeli es aku masuk kerumah entah kenapa si adek menagis"
# t "{cps=20}dek kenapa kamu menangis?"
# show Rika nangis
# t "{cps=20}Ini kak aku menggambar tapi gambaranku jelek :( "
# hide Rika nangis

# show Tika SD awal
# i "{cps=20}mana buku gambarnya?"
# hide Tika SD awal
# hide Rika menangis

# show Rika senyum
# r "{cps=20}Apakah kakak mau membantuku?"
# menu:
#     "Ya":
#         # $yuuki_affection = yuuki_affection + 1
#         $ hp_pts += 2 #MENAMBAH SCORE
#         $ exp_pts += 2 
#         $ health += 10
#         jump membantu_rika
#     "Tidak":
#         $ hp_pts -=10  # MENGKURANGI SCORE 
#         $ exp_pts -= 1
#         $ health -= 5
#         jump tidak_membantu_rika

# label membantu_rika:
# scene bg ruang makan
# show Tika SD awal
# show screen animasi   #### MENAMPILKAN STAR SCREEN
# hide screen animasi with dissolve
# t "{cps=20}akhirnya aku membantu adek menggambar"
# show Tika SD awal
# r "{cps=20}wah jadi bagus kak"
# r "{cps=20}terima kasih kak" # Side image
# hide Tika SD
# jump stage5

# label tidak_membantu_rika:
# scene bg ruang makan
# show Tika SD awal
# t "{cps=20}maaf aku gak bisa bantu"
# t "{cps=20}karena aku lagi males banget" # Side image
# hide Tika SD awal
# jump stage5


# ########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 5
# label stage5:
# "Pada Sore itu rika bermain didepan rumah dengan membawa bola"
# "Angin berhembus meniup balon dan menyangkut dipohon"
# t "{cps=20}Dek kamu gak bermain didepan?"
# show Rika nangis
# r "{cps=20}Itu kak balonku terhembus angin dan menyangkut "
# R "{cps=20}Apakah kakak bisa membantuku mengambil balonku yang tersangkut ?"
# hide Rika menangis
# show Rika_senyum
# menu:
#     "Ya":
#         # $yuuki_affection = yuuki_affection + 1
#         $ hp_pts += 2 #MENAMBAH SCORE
#         $ exp_pts += 2 
#         $ health += 10
#         jump mengambil_balon
#     "Tidak":
#         $ hp_pts -=10  # MENGKURANGI SCORE 
#         $ exp_pts -= 1
#         $ health -= 5
#         jump menolak_mengambil

# label mengambil_balon:
# scene bg ruang makan
# show Tika SD awal
# show screen animasi   #### MENAMPILKAN STAR SCREEN
# hide screen animasi with dissolve
# t "{cps=20}baik bu tika belikan"
# show Tika SD awal
# t "{cps=20}beli berapa nih?"
# i senyum "{cps=20}beli satu aja"  # Side image
# hide Tika SD
# jump stage6

# label menolak_mengambil:
# scene bg ruang makan
# show Tika SD awal
# t "{cps=20}ndak mau bu"
# show Tika SD awal
# t "{cps=20}tika lagi males"
# i senyum "{cps=20}yasudah kalo gitu ibu yang beli"  # Side image
# hide Tika SD awal
# jump stage6

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ 
#  #   #    NEXT CHAPTER SD KELAS 2 #

# label chapter1:

# play music "music/dovewholookforbeans.mp3"
# # Show a background.
# scene bg sekolah
# with fade

# show Tsp1
# N "Tika pun sampai disekolah setelah beberapa menit perjalanan"
# N "Tika pun berkata"
# t "akhirnya aku sampai di sekolah"
# scene bg hitam with fade
# with Pause(2)
# scene kelas with gerakan_kiri
# show Lia_datang at tengah with dissolve
# l "Selamat pagi Tika"
# l "Tumben kamu pergi pagi kesekolah?"
# l "Biasanya kamu terlambat masuk sekolah"
# show Tsp1 at kanan_atas with dissolve
# t "terlambat tapi gak sering kan?? hahaha "
# t "hari ini aku datang pagi ada piket kebersihan "
# t "jadi aku datang pagi kesekolah "
# show Tsp1 at kanan with movef
# show Lia_datang at tengah_atas with movef
# show Lia_datang_oh at tengah_atas with movef
# show Lia_Senyum_kedip at tengah_atas with movef
# hide Lia_datang_oh with dissolve
# l "Oh begitu pantas datang pagi"
# l "pantas kok pagi sekali"
# show Tsp3
# hide Tsp2

        
    
        
    

