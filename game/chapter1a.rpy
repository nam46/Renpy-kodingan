label chapter1a:
scene bg sekolah
hide ibu bicara
show Tika Mager
t "{cps=20}Aku kira tadi bakal terlambat"
t "{cps=20}Akhirnya sampai juga disekolah"
t "{cps=20}setelah piket aku pun duduk dibangku"
"Sepertinya guru masuk"
"Pelajaran dimulai"
pg "{cps=20}pagi anak-anak selamat pagi"
pg "{cps=20}pelajaran akan dimulai siapkan buku pelajarannya"
t "{cps=20}baik pak"
"Dipojok kelas ayu terlihat kebingungan"
"lalu pak indra pun mendatangi ayu dan bertanya"
pg "{cps=20}kamu kenapa?"
pg "{cps=20}kok tidak dikeluarkan bukunya?"
ay "{cps=20}maaf pak saya lupa membawa buku bahasa indonesia"
pg "{cps=20}kalau begitu bergabung saja dengan temannya"
pg "{cps=20}lain kali jangan diulangi lagi"
pg "{cps=20}apakah disini ada yang mau berbagi buku dengan ayu?"

t "apakah yang akan kamu lakukan?"
menu:
    "Mendengarkan guru":
        t "Aku pun mendengarkan guru seperti biasa"
        jump pilihan_mendengarkan
    "Mengangkat tangan":
        $yuuki_affection = yuuki_affection + 1
        jump pilihan_berbagi_buku

label pilihan_mendengarkan:
t "{cps=20}ayu pun sedih"
t "{cps=20}karena tidak ada yang membantunya"

label pilihan_berbagi_buku:
t "{cps=20}aku pun mengangkat tangan"
pg"{cps=20}iya ada apa tika?"
t "{cps=20}pak saya mau berbagi dengan ayu"
pg"{cps=20}ah syukurlah ayu ada yang berbagi buku denganmu"
t "{cps=20}pelajaran pun selesai dan bel berbunyi"
t "{cps=20}menandakan jam istirahat dimulai"
"setelah ini apa yang akan kamu lakukan?"
menu:
    "Pergi kekantin":
        t "Aku pun mendengarkan guru seperti biasa"
    "Pergi ke taman sekolah":
        $yuuki_affection = yuuki_affection + 1


label ending_evaluation:
    if yuuki_affection >= 2:
        jump best_ending
    elif yuuki_affection = 1:
        jump bad_ending

label best_ending:
t "Ending yang terbaik"
return
label bad_ending:
t "akhir yang buruk" 
