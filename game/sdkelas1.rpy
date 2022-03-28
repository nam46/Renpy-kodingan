# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

# The game starts here.

# This shows a character sprite. 

# These display lines of dialogue.

label sdkelas1:


######### ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 1

"{cps=20}Pada suatu pagi "
"{cps=20}Ibu menyapa tika "
show ibu starter
i "{cps=20}Tika... kamu lagi ngapain sayang?"
hide ibu starter
show main dakon
t "{cps=20}Sedang bermain dakon sama adek bu"
hide main dakon

show ibu starter
i "{cps=20}Tolong ambilkan sapu dibelakang pintu"
hide ibu starter
show Tika SD awal
menu:
    "Baik bu":
        # $yuuki_affection = yuuki_affection + 1
        $ health += 10
        $ hp_pts += 10 #MENAMBAH SCORE
        $ exp_pts += 2 
        jump pilihan_baik_bu
    "Tika Masih main bu":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump tika_masih_main


label pilihan_baik_bu:
scene bg ruang makan
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
pause 1.0
hide screen animasi with dissolve
t "{cps=20}baik bu tika ambilkan sapu"
show Tika SD awal
i senyum "{cps=20}Terima kasih tika"  # Side image
hide Tika SD awal
jump stage2

label tika_masih_main:
show Tika SD awal
t "{cps=20}Tika masih main bu"
hide Tika SD awal
show ibu starter
i "{cps=20}Yasudah kalo masih main"
hide ibu starter
jump stage2

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 2
label stage2:
    
play music "music/JP Soundworks - Event4.ogg" fadeout 1  # MUSIC
show Rika nangis
r " huuuuuuuu "
hide Rika nangis

show Rika menangis
i " Tika adekmu kenapa kok nangis terus?"
hide Rika menangis
show Tika SD awal
t " Itu bu Adek Minta beli permen bu"
i "kalau begitu tolong belikan permen di toko sebelah"
menu:
    "Baik bu":
        # $yuuki_affection = yuuki_affection + 1
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 2
        jump pilihan_baik_bu_2
    "Ndak mau bu tika lagi males":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump tika_lagi_males


label pilihan_baik_bu_2:
scene bg ruang makan
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}baik bu tika belikan"
show Tika SD awal
t "{cps=20}setelah itu aku memberikan pada adikku"
hide Tika SD awal
show Rika senyum
r "{cps=20}terima kasih kak"
hide Rika senyum
show Tika senyum
t "{cps=20}sama-sama dek"
show Tika senyum
 # Side image
jump stage3

label tika_lagi_males:
scene bg ruang makan
show Tika SD awal
t "{cps=20}ndak mau bu"
show Tika SD awal
t "{cps=20}tika lagi males"
i senyum "{cps=20}yasudah kalo gitu ibu yang beli"  # Side image
hide Tika SD awal
jump stage3
stop music fadeout 1
 

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 3
label stage3:
play music "music/bensound-littleidea.mp3" fadeout 1   # MUSIC
scene bg penjual
" Pada saat itu di pagi hari ada penjual gulali"
" Gulali... gulali ... "
show Tika SD awal 
t "{cps=20}Ibu… ibu… Tika mau beli gulali dan es cao"
show ibu starter at kanan
i "{cps=20}Jangan banyak-banyak tika, beli salah satu saja"
hide ibu starter with dissolve
hide Tika SD awal with dissolve

show Tika SD awal  
t "{cps=20}Aku mau es sama permen ibu"
show ibu starter at kanan with movef
i "{cps=20}Kalau begitu nanti dibagi sama adek ya"
menu:
    "Iya bu":
        # $yuuki_affection = yuuki_affection + 1
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 2
        jump tika_berbagi
    "Ndak Bu":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump tika_tidak_berbagi

label tika_berbagi:
scene bg ruang makan
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}setelah membeli permen dan es aku berbagi ke adek"
show Tika SD awal at kanan
show Rika senyum
r "{cps=20}Terima kasih kakak"
show Tika senyum
t "{cps=20}iya sama-sama"
hide Tika SD awal
hide Tika senyum
hide Rika senyum

jump stage4

label tika_tidak_berbagi:
scene bg ruang makan
show Tika SD awal
t "{cps=20}aku akhirnya memakannya sendiri"
hide Tika SD awal
jump stage4

########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 4
label stage4:
play music "music/Folksy Days_Sad.mp3" fadeout 1   # MUSIC
"Tak lama kemudian aku melihat adek sedih"
t "{cps=20}dek kenapa kamu sedih?"
show Rika nangis
t "{cps=20}Ini kak aku menggambar tapi gambaranku jelek :( "
hide Rika nangis

show Tika SD awal
i "{cps=20}mana buku gambarnya?"
hide Tika SD awal
hide Rika menangis

show Rika senyum
r "{cps=20}Apakah kakak mau membantuku?"
show Tika SD awal
menu:
    "Ya":
        # $yuuki_affection = yuuki_affection + 1
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 2
        jump membantu_rika
    "Tidak":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump tidak_membantu_rika

label membantu_rika:
scene bg ruang makan
show Tika SD awal
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}akhirnya aku membantu adek menggambar"
hide Tika SD awal
show Rika senyum
r "{cps=20}wah jadi bagus kak"
r "{cps=20}terima kasih kak" # Side image
hide Tika SD
jump stage5

label tidak_membantu_rika:
scene bg ruang makan
show Tika SD awal
t "{cps=20}maaf aku gak bisa bantu"
t "{cps=20}karena aku lagi males banget" # Side image
hide Tika SD awal
jump stage5


########## ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ STAGE 5
label stage5:
scene bg balon lepas
"Pada Sore itu rika bermain didepan rumah dengan membawa balon"
"Angin berhembus meniup balon dan menyangkut dipohon"
#show tika disini
show Tika senyum at tengah
t "{cps=20}Dek tadi kamu bermain membawa balon"
t "{cps=20}mana balonmu kok nggak ada?"
show Rika nangis at nganan
r "{cps=20}tadi balonku terhembus angin dan menyangkut "
r "{cps=20}Apakah kakak bisa membantuku mengambilnya?"
hide Rika menangis
menu:
    "Ya":
        # $yuuki_affection = yuuki_affection + 1
        $ health += 5
        $ hp_pts += 5 #MENAMBAH SCORE
        $ exp_pts += 2
        jump mengambil_balon
    "Tidak":
        $ health -= 5
        $ hp_pts -= 5 #MENAMBAH SCORE
        $ exp_pts -= 1 
        jump menolak_mengambil

label mengambil_balon:
scene bg balon lepas
show Tika menyerahkan_1 at tengah 
show screen animasi   #### MENAMPILKAN STAR SCREEN
hide screen animasi with dissolve
t "{cps=20}ini dek tadi kakak ambil ternyata bisa"
show Tika menyerahkan_2 at tengah
show Rika menerima_1 at kanan
r "{cps=20}Terima Kasih kak"
r "{cps=20}akhirnya rika bisa main lagi"  # Side image
hide Tika SD
jump sdkelas2

label menolak_mengambil:
scene bg ruang makan
show Tika SD awal
t "{cps=20}ndak mau bu"
show Tika SD awal
t "{cps=20}tika lagi males"
i senyum "{cps=20}yasudah kalo gitu ibu yang beli"  # Side image
hide Tika SD awal
jump sdkelas2

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

        
    
        
    

