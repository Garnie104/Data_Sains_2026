# ANALISIS STRUKTUR DATA, EXPLORATORY DATA ANALYSIS, DAN DATA PRE-PROCESSING PADA DATASET KECELAKAAN LALU LINTAS INGGRIS TAHUN 2025

Tema: Transportation

Disusun oleh:

- Maheswara Ariq Athallah (101032300050)
- Muhammad Al Qarnie (101032330043)
- Daffa Hermansyah (101032330090)

2026

---

**ABSTRAK**

Laporan ini disusun sebagai tugas besar pengganti Ujian Tengah Semester (UTS) pada mata kuliah Data Sains dan Analisis. Kajian ini berfokus pada pemahaman struktur data, *Exploratory Data Analysis* (EDA), serta tahapan *Data Pre-processing* menggunakan dataset resmi *UK Road Safety Statistics* tahun 2025 yang terdiri atas 101.525 kejadian kecelakaan, 183.948 data kendaraan, dan 127.883 data korban. Tahapan pengolahan data meliputi seleksi dan penggabungan tabel melalui kunci `collision_index`, pembersihan kode nilai kosong (`-1`), validasi rentang nilai, pengisian data kosong (*imputasi*) menggunakan median dan modus, serta transformasi fitur kategorikal menggunakan teknik *One-Hot Encoding*. Hasil EDA menunjukkan bahwa mayoritas kecelakaan tergolong ringan (73,76%), memuncak pada hari Jumat dan pukul 17:00, serta memiliki korelasi tertinggi antara batas kecepatan dengan wilayah perkotaan/pedesaan (+0,67). Tahap *pre-processing* berhasil menghilangkan seluruh nilai kosong dan menghasilkan dataset akhir bersih berukuran 101.525 baris dan 39 kolom yang siap digunakan pada tahap pemodelan *Machine Learning* menjelang UAS.

Kata kunci: data sains, *exploratory data analysis*, *pre-processing*, *one-hot encoding*, kecelakaan lalu lintas

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang
Kecelakaan lalu lintas merupakan permasalahan keselamatan publik yang dipengaruhi oleh berbagai faktor secara bersamaan, mulai dari kondisi jalan, cuaca, waktu kejadian, hingga karakteristik pengemudi dan kendaraan. Sebelum kumpulan data kecelakaan dapat dimanfaatkan untuk membangun model prediksi (*Machine Learning*), data mentah perlu dipahami terlebih dahulu struktur dan isinya, dieksplorasi pola umumnya, serta dibersihkan dari nilai yang rusak atau kosong agar tidak menghasilkan kesimpulan yang keliru.

### 1.2 Batasan Masalah
Sesuai ketentuan tugas besar pengganti UTS, kajian dalam laporan ini dibatasi pada tahap pemahaman struktur data, *Exploratory Data Analysis* (EDA), dan *Data Pre-processing* (seleksi, pembersihan, validasi, imputasi, dan *One-Hot Encoding*) pada dataset *UK Road Safety Statistics* tahun 2025. Karena dataset berbentuk data tabel (tabular) dan bukan data citra, metode pengolahan gambar seperti *Image Segmentation* tidak diterapkan. Tahap pemodelan *Machine Learning* juga belum dilakukan pada laporan ini karena akan dilanjutkan menjelang UAS.

### 1.3 Rumusan Masalah
Berdasarkan latar belakang tersebut, rumusan masalah yang dikaji dalam laporan ini meliputi: (1) bagaimana struktur dan keterkaitan antar-tabel pada dataset kecelakaan lalu lintas UK tahun 2025; (2) bagaimana pola distribusi kejadian, nilai ekstrem (*outlier*), dan korelasi antar-variabel utama; serta (3) bagaimana tahapan pembersihan dan transformasi data (*pre-processing*) agar dataset siap digunakan untuk pemodelan.

### 1.4 Tujuan
Tujuan dari penyusunan laporan ini adalah untuk memetakan struktur dataset *UK Road Safety Statistics* 2025, menyajikan hasil analisis eksploratif (*outlier* dan korelasi) yang mudah dipahami, serta menghasilkan dataset akhir yang bersih dan terstruktur melalui proses *pre-processing* lengkap.

### 1.5 Metode Penulisan
Pengolahan data dilakukan menggunakan bahasa pemrograman Python pada lingkungan Jupyter Notebook / Google Colab (`Tugas_Besar_Data_Sains.ipynb`) dengan pustaka `pandas`, `numpy`, `matplotlib`, `seaborn`, dan `scikit-learn`. Seluruh tahapan teknis mengacu pada gabungan materi kuliah Pertemuan 1 hingga 7 dari dosen pengampu serta modul LMS.

---

## 2. STRUKTUR DATA DAN METODOLOGI

### 2.1 Struktur Dataset Kecelakaan Lalu Lintas UK 2025
Dataset *UK Road Safety Statistics* tahun 2025 terdiri dari tiga tabel utama berformat CSV dan satu file kamus data (*Data Guide*) berformat Excel:

| No | Nama Tabel | Jumlah Baris | Jumlah Kolom | Kunci Penghubung | Penjelasan Isi Data |
| :---: | :--- | :---: | :---: | :--- | :--- |
| 1 | Collision (Kecelakaan) | 101.525 | 44 | `collision_index` | Waktu, lokasi, batas kecepatan, cuaca, dan tingkat keparahan. |
| 2 | Vehicle (Kendaraan) | 183.948 | 32 | `collision_index`, `vehicle_reference` | Jenis kendaraan, kapasitas mesin, dan profil pengemudi. |
| 3 | Casualty (Korban) | 127.883 | 23 | `collision_index`, `vehicle_reference`, `casualty_reference` | Usia, jenis kelamin, dan tingkat luka korban. |

Seluruh tabel memiliki kecocokan kunci `collision_index` sebesar 100%, artinya seluruh 101.525 kejadian di tabel *Collision* tercatat lengkap di tabel *Vehicle* dan *Casualty*. Pada dataset resmi pemerintah Inggris ini, angka `-1` memiliki arti khusus yaitu data kosong atau di luar jangkauan (*missing or out of range*).

### 2.2 Alur Pengolahan Data
Proses pengolahan data dijalankan secara berurutan mulai dari penggabungan fitur relevan antar-tabel (*selection & merging*), pembersihan duplikasi dan kode `-1` (*cleaning & validation*), pengisian nilai kosong (*imputasi*) menggunakan median dan modus, hingga pengubahan kolom kategori menjadi kolom biner (*One-Hot Encoding*).

---

## 3. ANALISIS DAN PEMBAHASAN

### 3.1 Analisis Eksploratif (*Exploratory Data Analysis*)
Dari total 101.525 kejadian kecelakaan sepanjang tahun 2025, mayoritas merupakan kecelakaan ringan (*Slight*) sebanyak 74.881 kasus (73,76%), diikuti kecelakaan serius (*Serious*) sebanyak 25.191 kasus (24,81%), dan kecelakaan fatal (*Fatal*) sebanyak 1.453 kasus (1,43%). Berdasarkan waktu kejadian, hari Jumat mencatat jumlah kecelakaan tertinggi (16.811 kasus) dan hari Minggu paling rendah (11.197 kasus). Kecelakaan memuncak pada pukul 17:00 (8.877 kasus) bertepatan dengan jam pulang kerja, dan paling rendah pada pukul 04:00 pagi (634 kasus).

![Gambar 1](output_grafik/1_eda_distribusi_keparahan_hari.png)
![Gambar 2](output_grafik/2_eda_tren_jam.png)

### 3.2 Deteksi Nilai Ekstrem (*Outlier*)
Secara sederhana, *outlier* adalah nilai data yang menyimpang jauh dari kebiasaan mayoritas data lainnya. Deteksi dilakukan menggunakan metode *Interquartile Range* (IQR) dan *Boxplot* dengan mengecualikan kode `-1`.

| Fitur Numerik | Q1 | Q3 | Batas Atas Normal | Jumlah Outlier | Persentase | Nilai Maksimum |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `number_of_vehicles` | 1,0 | 2,0 | 3,5 | 1.939 | 1,91% | 17 kendaraan |
| `number_of_casualties` | 1,0 | 1,0 | 1,0 | 18.208 | 17,93% | 142 korban |
| `speed_limit` | 30,0 | 40,0 | 55,0 | 18.309 | 18,03% | 70 mph |
| `age_of_driver` | 28,0 | 54,0 | 93,0 | 65 | 0,04% | 105 tahun |
| `engine_capacity_cc` | 1.200 | 1.984 | 3.160 | 6.146 | 4,42% | 48.000 cc |
| `age_of_casualty` | 23,0 | 53,0 | 98,0 | 7 | 0,01% | 105 tahun |

Nilai ekstrem tersebut bukan merupakan kesalahan penulisan data, melainkan kejadian nyata yang memang jarang terjadi, seperti tabrakan beruntun hingga 17 kendaraan, kecelakaan angkutan massal dengan 142 korban, kendaraan berat berkapasitas mesin besar, serta jalan bebas hambatan berbatas kecepatan 70 mph. Oleh sebab itu, data *outlier* tetap dipertahankan agar informasi kejadian fatal tidak hilang.

![Gambar 3](output_grafik/3_eda_boxplot_outlier.png)

### 3.3 Analisis Korelasi dan Seleksi Fitur
Korelasi mengukur kuat lemahnya hubungan antara dua variabel pada rentang `-1` hingga `+1`. Kolom nomor identitas (`collision_index`, `collision_ref_no`), kolom konstan (`collision_year`), dan kode wilayah acak (`police_force`, `local_authority_district`) dikeluarkan karena hanya berfungsi sebagai label pengenal. Sebelas fitur numerik dan ordinal bermakna yang dimasukkan ke dalam perhitungan korelasi adalah `collision_severity`, `number_of_vehicles`, `number_of_casualties`, `speed_limit`, `urban_or_rural_area`, `light_conditions`, `weather_conditions`, `road_surface_conditions`, `hour`, `avg_driver_age`, dan `avg_engine_cc`.

![Gambar 4](output_grafik/4_eda_heatmap_korelasi.png)

Tiga hubungan paling kuat yang terbaca pada matriks korelasi adalah: (1) `speed_limit` dengan `urban_or_rural_area` (+0,67), yang menunjukkan jalan di luar kota/pedesaan memiliki batas kecepatan jauh lebih tinggi daripada jalan di dalam kota; (2) `weather_conditions` dengan `road_surface_conditions` (+0,43), yang menunjukkan kondisi cuaca buruk secara langsung membuat permukaan jalan menjadi basah atau licin; dan (3) `light_conditions` dengan `hour` (+0,21), yang mencerminkan hubungan jam kejadian dengan pencahayaan alami siang dan malam.

### 3.4 Hasil *Data Pre-processing* dan *One-Hot Encoding*
Sebanyak 13 fitur utama dari tabel *Collision* digabungkan dengan rata-rata usia pengemudi dan kapasitas mesin dari tabel *Vehicle*, menghasilkan dimensi awal 101.525 baris dan 16 kolom. Pada tahap pembersihan dan validasi, ditemukan 0 data duplikat, seluruh kode `-1` dikonversi menjadi `NaN`, dan ditemukan fakta penting bahwa kolom `age_of_vehicle` pada dataset tahun 2025 seluruhnya bernilai `-1` (100% kosong) sehingga kolom tersebut dihapus.

Nilai kosong yang tersisa pada `avg_engine_cc` (13.670 baris), `avg_driver_age` (6.087 baris), `road_surface_conditions` (634 baris), `light_conditions` (16 baris), dan `urban_or_rural_area` (4 baris) ditangani melalui proses *imputasi*. Fitur numerik diisi menggunakan nilai **median** (`avg_driver_age` = 40 tahun; `avg_engine_cc` = 1.560 cc) karena tahan terhadap *outlier*, sedangkan fitur kategorikal diisi menggunakan **modus** (kategori terbanyak), sehingga total nilai kosong menjadi 0.

Selanjutnya, teknik **One-Hot Encoding** diterapkan menggunakan `OneHotEncoder` pada lima fitur kategorikal nominal (`road_type`, `weather_conditions`, `light_conditions`, `road_surface_conditions`, dan `urban_or_rural_area`) agar komputer tidak menganggap kode kategori sebagai angka urutan bertingkat. Transformasi ini mengubah dimensi dataset dari 101.525 × 16 menjadi **101.525 baris dan 39 kolom** (bertambah 28 kolom biner bernilai 0 dan 1).

---

## 4. PENUTUP

### 4.1 Simpulan
Analisis terhadap 101.525 data kecelakaan lalu lintas UK tahun 2025 menunjukkan bahwa kecelakaan mayoritas bersifat ringan (73,76%) dan paling sering terjadi pada hari Jumat serta jam sibuk sore hari (pukul 17:00). Proses *pre-processing* berhasil membersihkan seluruh kode kosong `-1`, menghapus kolom `age_of_vehicle` yang kosong 100%, mengimputasi seluruh nilai hilang hingga tersisa 0 *missing values*, serta menghasilkan dataset akhir berukuran 101.525 × 39 kolom melalui *One-Hot Encoding*.

### 4.2 Saran
Dataset bersih berukuran 101.525 × 39 kolom yang dihasilkan pada tahap ini disarankan untuk langsung disimpan dan dimanfaatkan pada tahap pemodelan *Machine Learning* menjelang UAS, dengan tetap memperhatikan ketidakseimbangan kelas pada variabel target `collision_severity` (di mana kasus fatal hanya sebesar 1,43%).

---

## DAFTAR PUSTAKA

Department for Transport (DfT). (2025). *Road Safety Open Dataset 2025: Collision, Vehicle, Casualty, and Data Guide*. United Kingdom.

Nasution, S. M. (2026). *Materi Kuliah Data Sains dan Analisis: Week 3 – Week 6 (Data Understanding & Data Preparation)*.

Tim Pengajar Data Sains. (2026). *Modul Pembelajaran LMS: Pertemuan 01, 04, 05, 06, 07, dan 09 (Data Understanding & Data Construction)*.
