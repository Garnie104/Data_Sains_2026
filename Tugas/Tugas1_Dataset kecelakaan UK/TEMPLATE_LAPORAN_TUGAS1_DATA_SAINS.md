# TEMPLATE LAPORAN TUGAS 1: DATA SAINS (EXPLORATORY DATA ANALYSIS)
> **Petunjuk Penggunaan:**  
> Salin (*copy-paste*) kerangka di bawah ini ke Microsoft Word atau Google Docs.  
> Bahasanya sudah dibuat **sangat sederhana, santai, mudah dipahami orang awam**, dan bebas dari istilah teknis yang rumit.  
> Gambar grafik tinggal Anda ambil langsung dari folder: `eda_output/`.

---

# [HALAMAN 1: COVER]

```text
                                TUGAS 1 DATA SAINS
    ANALISIS DATA EKSPLORATIF POLA DAN FAKTOR KEPARAHAN KECELAKAAN LALU LINTAS
                              DI BRITANIA RAYA



                                  Nama Anggota:
                           [Nama Mahasiswa 1]  [NIM 1]
                           [Nama Mahasiswa 2]  [NIM 2]
                           [Nama Mahasiswa 3]  [NIM 3]



                         PROGRAM STUDI S1 TEKNIK KOMPUTER
                             FAKULTAS TEKNIK ELEKTRO
                                TELKOM UNIVERSITY
                                    2026/2027
```

---

# [HALAMAN 2: DESKRIPSI DATASET & SUB-BAB 1]

## 1. Deskripsi Dataset
**Link Dataset:** UK Road Safety Open Dataset 2025 (Department for Transport / GOV.UK)

Dataset ini berisi catatan resmi kecelakaan lalu lintas di seluruh wilayah Britania Raya (Inggris) sepanjang tahun 2025 yang dicatat langsung oleh pihak kepolisian. Data ini mencatat sebanyak **101.525 kejadian kecelakaan** dengan 44 informasi penting, seperti jam kejadian, hari, batas kecepatan jalan, cuaca saat tabrakan, kondisi aspal, berapa kendaraan yang terlibat, sampai seberapa parah korban yang terluka. 

Tujuan dari analisis data (EDA) ini adalah untuk menjawab pertanyaan-pertanyaan sederhana sehari-hari: jam berapa jalanan paling berbahaya, hari apa yang paling rawan tabrakan, seberapa bahaya mengebut di jalan, dan faktor apa saja yang paling sering membuat pengendara celaka.

---

## 2. Hasil Analisis Data Eksploratif (EDA)

### a. Seberapa Parah Akibat dari Kecelakaan yang Terjadi?
*(Sisipkan Gambar: `eda_output/1_distribusi_keparahan.png`)*

Grafik di atas memperlihatkan seberapa parah akibat dari 101.525 tabrakan yang tercatat di jalan raya:
- Sebagian besar, yaitu **74.881 kejadian (73,8%)**, adalah kecelakaan **luka ringan** (seperti lecet, memar, atau terkilir yang tidak memerlukan rawat inap di rumah sakit).
- Sekitar **25.191 kejadian (24,8%)** termasuk kecelakaan **luka berat** (seperti patah tulang atau luka parah yang harus dirawat inap).
- Sebanyak **1.453 kejadian (1,4%)** berujung pada **korban meninggal dunia**.

Dari data ini, kabar baiknya adalah sebagian besar kecelakaan tidak berujung maut. Namun, angka korban meninggal dan luka berat tetap menjadi pengingat bahwa risiko fatal di jalan raya masih nyata jika pengemudi tidak berhati-hati.

---

# [HALAMAN 3: SUB-BAB 2 & SUB-BAB 3 (WAKTU KEJADIAN)]

### b. Jam Berapa Kecelakaan Paling Sering Terjadi dalam Sehari?
*(Sisipkan Gambar: `eda_output/2_tren_jam_kejadian.png`)*

Grafik garis di atas menunjukkan tren kejadian kecelakaan selama 24 jam penuh. Polanya terlihat sangat jelas mengikuti jam aktivitas masyarakat sehari-hari dan memiliki dua waktu puncak:
- **Puncak Pagi (Pukul 08:00):** Terjadi lonjakan kecelakaan sebanyak **6.716 kejadian**, bertepatan dengan waktu orang-orang berbondong-bondong berangkat kerja dan anak-anak pergi ke sekolah.
- **Puncak Sore (Pukul 17:00):** Merupakan waktu paling berbahaya dalam sehari dengan **8.877 kejadian** saat jam orang-orang pulang kantor.

Kecelakaan di sore hari jauh lebih banyak dibanding pagi hari karena saat pulang kerja kondisi fisik dan pikiran pengemudi biasanya sudah lelah setelah beraktivitas seharian, ditambah kondisi jalan yang mulai gelap menjelang malam. Sebaliknya, waktu paling aman dengan kecelakaan paling sedikit adalah tengah malam hingga subuh (pukul 01:00–05:00) saat jalanan sepi.

---

### c. Hari Apa yang Paling Sering Terjadi Kecelakaan?
*(Sisipkan Gambar: `eda_output/3_distribusi_hari.png`)*

Grafik batang di atas membandingkan seberapa sering kecelakaan terjadi di setiap hari dalam seminggu:
- Hari **Jumat** adalah hari yang paling rawan celaka, dengan angka tertinggi mencapai **16.811 kejadian (16,6%)**. Hal ini terjadi karena hari Jumat adalah akhir pekan kerja, di mana jalanan sangat padat oleh orang yang pulang kantor, orang yang ingin bepergian ke luar kota, serta orang yang keluar untuk jalan-jalan di malam hari.
- Hari kerja lainnya (Senin sampai Kamis) juga tergolong ramai dengan angka kecelakaan berkisar antara 14 sampai 15 ribu kejadian.
- Hari **Minggu** justru menjadi hari yang paling aman dan paling sedikit kecelakaan (hanya **11.197 kejadian**), karena sebagian besar masyarakat memilih beristirahat di rumah dan volume kendaraan di jalan menurun drastis.

---

# [HALAMAN 4: SUB-BAB 4 & SUB-BAB 5 (KECEPATAN & CUACA)]

### d. Seberapa Bahaya Mengebut? (Batas Kecepatan vs Tingkat Kematian)
*(Sisipkan Gambar: `eda_output/4_speed_limit_vs_severity.png`)*

Grafik di atas membuktikan fakta nyata bahwa semakin kencang laju kendaraan, semakin mematikan dampaknya saat terjadi tabrakan:
- Di jalanan perumahan atau area sekolah yang batas kecepatannya rendah **20 mph (sekitar 32 km/jam)**, persentase korban meninggal sangat kecil, yaitu hanya **0,51%** (artinya dari 200 tabrakan, hampir semuanya selamat).
- Namun, di jalan raya antarkota dengan batas kecepatan **60 mph (sekitar 96 km/jam)**, persentase kecelakaan fatal melonjak drastis hingga **3,70%** (naik **lebih dari 7 kali lipat**).

Hal ini terjadi karena hukum fisik tabrakan: kendaraan yang melaju kencang membawa energi benturan yang jauh lebih dahsyat, sehingga bodi mobil remuk lebih parah dan tubuh manusia di dalamnya sulit bertahan dari benturan keras tersebut.

---

### e. Cuaca Seperti Apa yang Paling Sering Terjadi Kecelakaan?
*(Sisipkan Gambar: `eda_output/5_cuaca_dominan.png`)*

Kebanyakan orang menduga bahwa kecelakaan paling sering terjadi saat hujan lebat, badai angin, atau jalanan licin tertutup salju. Namun, data pada grafik di atas menunjukkan fakta yang justru sebaliknya:
- Sebanyak **83.405 kejadian (82,1%)** kecelakaan justru terjadi pada saat **cuaca cerah dan jalanan kering**.
- Kecelakaan pada saat cuaca hujan hanya sekitar **10,1%**.

Penyebab fenomena ini ada pada perilaku pengemudi. Saat cuaca buruk dan jalanan basah licin, orang biasanya merasa waspada dan takut, sehingga mengemudi pelan-pelan serta menjaga jarak aman. Sebaliknya, saat cuaca cerah dan jalanan kering, pengemudi merasa sangat aman sehingga berani memacu kendaraan lebih kencang, kurang menjaga jarak, atau terdistraksi sambil memainkan ponsel.

---

# [HALAMAN 5: SUB-BAB 6 (KASUS EKSTREM) & KESIMPULAN]

### f. Kasus Luar Biasa: Tabrakan Paling Ekstrem yang Pernah Terjadi
*(Sisipkan Gambar: `eda_output/6_outlier_kendaraan_korban.png`)*

Secara umum, kecelakaan lalu lintas biasanya hanya melibatkan 1 atau 2 mobil saja dengan 1 orang korban luka. Namun, grafik sebaran di atas menunjukkan adanya beberapa kejadian luar biasa yang sangat ekstrem:
- **Tabrakan Beruntun Karambol:** Tercatat pernah terjadi tabrakan beruntun di jalan tol yang melibatkan hingga **17 unit mobil sekaligus** dalam satu peristiwa tabrakan massal.
- **Kecelakaan dengan Korban Massal:** Ditemukan satu peristiwa tabrakan besar yang melibatkan kendaraan umum (bus) dengan jumlah korban luka dan terdampak mencapai **142 orang**.

Kejadian ekstrem ini menjadi pengingat pentingnya selalu menjaga jarak aman dengan mobil di depan, terutama saat melaju di jalan tol, agar tidak terjebak tabrakan beruntun saat mobil di depan mengerem mendadak.

---

## 3. Kesimpulan

Dari hasil analisis data kecelakaan di atas, ada beberapa poin penting yang mudah dipetik:

1. **Waspada di Jam Pulang Kantor:** Waktu paling rawan tabrakan adalah jam 5 sore dan di hari Jumat. Di waktu-waktu inilah pengendara harus ekstra sabar dan fokus karena badan sudah lelah setelah bekerja.
2. **Jangan Mengebut:** Batas kecepatan dibuat untuk menyelamatkan nyawa. Mengemudi di kecepatan 20–30 mph jauh lebih aman dibandingkan memacu kendaraan di atas 60 mph yang risiko kematiannya 7 kali lipat lebih tinggi.
3. **Jangan Lengah Saat Cuaca Cerah:** Sebanyak 8 dari 10 tabrakan justru terjadi di siang hari yang cerah dan aspal kering. Rasa aman semu sering kali membuat orang kurang waspada.
4. **Selalu Jaga Jarak:** Tabrakan beruntun bisa melibatkan belasan mobil sekaligus. Memberi jarak aman dengan kendaraan di depan memberi waktu yang cukup untuk mengerem darurat.
