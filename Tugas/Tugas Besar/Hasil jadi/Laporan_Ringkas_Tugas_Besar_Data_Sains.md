# TUGAS BESAR DATA SAINS
## STRUKTUR DATA, EXPLORATORY DATA ANALYSIS, DAN DATA PRE-PROCESSING DATASET UK ROAD SAFETY 2025

Disusun oleh:
- Maheswara Ariq Athallah (101032300050)
- Muhammad Al Qarnie (101032330043)
- Daffa Hermansyah (101032330090)

**Program Studi S1 Teknik Komputer**  
**Fakultas Teknik Elektro**  
**Telkom University**  
**Bandung**  
**2026**

---

## 1. Struktur Data
Dataset *UK Road Safety Statistics* tahun 2025 terdiri dari tiga tabel utama berformat CSV dan satu file kamus data (*Data Guide* `.xlsx`). Seluruh 101.525 kejadian pada tabel *Collision* terhubung dengan tabel *Vehicle* dan *Casualty* melalui kunci penghubung `collision_index`. Setiap kejadian yang tercatat melibatkan minimal satu korban manusia, mulai dari luka ringan (*Slight*), luka serius (*Serious*), hingga meninggal dunia (*Fatal*).

| Tabel | Baris | Kolom | Kunci Penghubung | Cakupan Data |
| :--- | :---: | :---: | :--- | :--- |
| **Collision** | 101.525 | 44 | `collision_index` | Waktu, lokasi, batas kecepatan, cuaca, tingkat keparahan. |
| **Vehicle** | 183.948 | 32 | `collision_index` | Jenis kendaraan, kapasitas mesin, profil pengemudi. |
| **Casualty** | 127.883 | 23 | `collision_index` | Usia, jenis kelamin, tingkat luka korban. |

Pada dataset ini, nilai **`-1`** menandakan data kosong atau tidak tersedia. Karena dataset berbentuk data tabel (tabular), teknik pengolahan citra seperti *Image Segmentation* tidak diterapkan.

### 1.1 Pemilihan Parameter dari Total 99 Kolom Asli
Dari total **99 kolom asli** yang tersebar di ketiga tabel (44 di *Collision*, 32 di *Vehicle*, dan 23 di *Casualty*), tidak semuanya perlu dipakai. Kita **hanya memilih 15 parameter utama** (13 kolom dari *Collision* ditambah 2 kolom ringkasan dari *Vehicle*, plus kolom turunan `month` dari `date`).

| Sumber Tabel | Parameter yang Dipakai | Alasan Pemakaian |
| :--- | :--- | :--- |
| **Collision** (13 kolom) | `collision_index` | Kunci penghubung utama untuk menggabungkan tabel. |
| **Collision** | `date`, `day_of_week`, `hour` (dari `time`) | Mengetahui pola hari, jam sibuk, dan bulan kejadian. |
| **Collision** | `collision_severity` | Mengukur tingkat keparahan kecelakaan (Fatal, Serious, Slight). |
| **Collision** | `number_of_vehicles`, `number_of_casualties` | Mengukur skala besarnya tabrakan dan jumlah korban. |
| **Collision** | `road_type`, `speed_limit`, `urban_or_rural_area` | Menggambarkan karakter fisik jalan, batas kecepatan, dan lokasi kota/desa. |
| **Collision** | `light_conditions`, `weather_conditions`, `road_surface_conditions` | Faktor lingkungan, cahaya, cuaca, dan kondisi permukaan jalan. |
| **Vehicle** (2 kolom) | `age_of_driver` → `avg_driver_age`, `engine_capacity_cc` → `avg_engine_cc` | Mengukur rata-rata usia pengemudi dan kapasitas mesin kendaraan per kejadian. |

**Alasan ~84 kolom lainnya dihilangkan:**
1. **Terlalu banyak data kosong (`-1`) atau kolom lama (`*_historic`):** Misalnya `local_authority_district` dan `age_of_vehicle` (seluruh datanya berisi `-1`), serta kolom `*_historic` dan `special_conditions_at_site` (~86%–88% kosong).
2. **Redundan dan rawan kebocoran data:** Misalnya `enhanced_severity_collision` (13,47% kosong dan isinya mengulang `collision_severity`) serta `age_band_of_driver` (sudah diwakili `age_of_driver`).
3. **Terlalu spesifik atau hanya label kode wilayah:** Seperti `collision_ref_no`, ribuan kode wilayah kecil (`lsoa`), dan merek kendaraan (`generic_make_model` yang punya 777 variasi).

Tabel *Casualty* berisi rincian profil tiap individu korban (peran korban sebagai pengemudi/penumpang/pejalan kaki, usia, jenis kelamin, tingkat luka per orang, hingga posisi di kendaraan/trotoar). Pada proyek ini, tabel *Casualty* **tetap digunakan** pada tahap Struktur Data (verifikasi 127.883 baris & 100% kecocokan `collision_index`) dan tahap EDA *Outlier* (fitur `age_of_casualty` pada Tabel 3), namun **tidak digabungkan ke dataset akhir *Pre-processing***. Fokus utama analisis adalah per satu kejadian kecelakaan (101.525 baris); jika Tabel *Casualty* digabung langsung dengan baris individu korban, satu kecelakaan berkorban banyak akan terhitung berulang kali, sedangkan total korban dan tingkat keparahannya sudah terwakili oleh `number_of_casualties` dan `collision_severity` di tabel *Collision*.

---

## 2. Exploratory Data Analysis (EDA)

### 2.1 Distribusi Keparahan, Pola Waktu, dan Kondisi Jalan
Dari 101.525 kecelakaan selama tahun 2025, mayoritas adalah kecelakaan ringan sebanyak **74.881 kasus (73,76%)**, serius **25.191 kasus (24,81%)**, dan fatal **1.453 kasus (1,43%)**. Rata-rata tiap kecelakaan melibatkan 1,81 kendaraan dan 1,26 korban. Sebanyak **66,14%** kejadian (67.148 kasus) terjadi di area perkotaan dan **48,93%** (49.673 kasus) berada di jalan dengan batas kecepatan 30 mph. Berdasarkan waktu, kecelakaan memuncak pada hari **Jumat (16.811 kasus)** dan pukul **17:00 (8.877 kasus)** saat jam pulang kerja, serta paling rendah pada hari **Minggu (11.197 kasus)** dan pukul **04:00 pagi (634 kasus)**.

![Gambar 1](output_grafik/1_eda_distribusi_keparahan_hari.png)
![Gambar 2](output_grafik/2_eda_tren_jam.png)

### 2.2 Deteksi Outlier (Metode IQR dan Boxplot)
Deteksi *outlier* dilakukan pada 6 fitur numerik utama menggunakan metode *Interquartile Range* (IQR) dan *Boxplot* dengan mengecualikan kode `-1`.

| Fitur Numerik | Q1 | Q3 | Batas Atas | Jumlah Outlier | Persentase | Maksimum |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `number_of_vehicles` | 1,0 | 2,0 | 3,5 | 1.939 | 1,91% | 17 kendaraan |
| `number_of_casualties` | 1,0 | 1,0 | 1,0 | 18.208 | 17,93% | 142 korban |
| `speed_limit` | 30,0 | 40,0 | 55,0 | 18.309 | 18,03% | 70 mph |
| `age_of_driver` | 28,0 | 54,0 | 93,0 | 65 | 0,04% | 105 tahun |
| `engine_capacity_cc` | 1.200 | 1.984 | 3.160 | 6.146 | 4,42% | 48.000 cc |
| `age_of_casualty` | 23,0 | 53,0 | 98,0 | 7 | 0,01% | 105 tahun |

Seluruh *outlier* tersebut **tetap dipertahankan (tidak dihapus)** karena merupakan kejadian nyata di lapangan seperti tabrakan beruntun 17 kendaraan, kecelakaan bus dengan 142 korban, truk bermesin besar, dan jalan tol berbatas 70 mph, bukan kesalahan input. Selain itu, pada `number_of_casualties`, nilai Q1 dan Q3 sama-sama 1 sehingga setiap kecelakaan dengan korban 2 orang atau lebih langsung terhitung sebagai outlier oleh rumus IQR. Jika dibuang, hampir 18% kasus kecelakaan nyata akan hilang.

![Gambar 3](output_grafik/3_eda_boxplot_outlier.png)

### 2.3 Analisis Korelasi dan Fitur yang Digunakan
Tidak semua kolom dimasukkan ke dalam korelasi. Kolom identitas (`collision_index`), tanggal/teks, serta fitur kategorikal nominal murni seperti `road_type` (karena kode angka 1, 2, 3, 6-nya sekadar nama jenis jalan, bukan urutan besar-kecil) dikeluarkan. Sebelas fitur numerik dan ordinal bermakna yang dimasukkan adalah `collision_severity`, `number_of_vehicles`, `number_of_casualties`, `speed_limit`, `urban_or_rural_area`, `light_conditions`, `weather_conditions`, `road_surface_conditions`, `hour`, `avg_driver_age`, dan `avg_engine_cc`.

![Gambar 4](output_grafik/4_eda_heatmap_korelasi.png)

Tiga hubungan terkuat pada matriks korelasi adalah: (1) `speed_limit` vs `urban_or_rural_area` (**+0,67**), menandakan jalan luar kota/pedesaan memiliki batas kecepatan lebih tinggi dibanding dalam kota; (2) `weather_conditions` vs `road_surface_conditions` (**+0,43**), menandakan cuaca buruk langsung membuat jalan menjadi basah atau licin; dan (3) `light_conditions` vs `hour` (**+0,21**), mencerminkan kaitan antara jam kejadian dengan tingkat pencahayaan siang/malam.

---

## 3. Data Pre-processing

### 3.1 Seleksi dan Penggabungan Data
Karena satu kecelakaan di tabel *Collision* dapat melibatkan lebih dari satu kendaraan di tabel *Vehicle*, maka data `age_of_driver` dan `engine_capacity_cc` pada tabel *Vehicle* diringkas terlebih dahulu dengan menghitung rata-ratanya per `collision_index` (`groupby`). Hasil ringkasan tersebut digabungkan ke 13 kolom pilihan dari tabel *Collision* sehingga menghasilkan ukuran awal **101.525 baris × 16 kolom** (termasuk kolom tambahan `month` dari `date`).

### 3.2 Pembersihan dan Validasi Data
1. **Cek duplikasi:** Ditemukan **0 baris ganda** pada kunci `collision_index`.
2. **Konversi kode `-1`:** Seluruh nilai `-1` diubah menjadi `NaN` agar tidak terbaca sebagai angka minus.
3. **Validasi rentang nilai:** Memastikan `speed_limit` berada pada rentang 1–70 mph, `avg_driver_age` pada rentang 10–105 tahun, dan `urban_or_rural_area` hanya bernilai 1 (*Urban*) atau 2 (*Rural*) sehingga 4 baris berkode 3 (*Unallocated*) ikut dibersihkan menjadi `NaN`.
4. **Penghapusan kolom kosong 100%:** Kolom `age_of_vehicle` yang sempat diperiksa dari tabel *Vehicle* ternyata **100% bernilai `-1`** pada data tahun 2025, sehingga kolom tersebut dihapus.

### 3.3 Imputasi *Missing Values*
Untuk mengisi data yang kosong setelah proses validasi, digunakan **Median** pada fitur numerik (karena tahan terhadap *outlier*) dan **Modus** (nilai terbanyak) pada fitur kategorikal:

| Fitur dengan Nilai Kosong | Jumlah Kosong | Persentase | Metode & Nilai Pengisi |
| :--- | :---: | :---: | :--- |
| `avg_engine_cc` (Numerik) | 13.670 | 13,46% | Median = `1.560 cc` |
| `avg_driver_age` (Numerik) | 6.087 | 6,00% | Median = `40 tahun` |
| `road_surface_conditions` (Kategori) | 634 | 0,62% | Modus = Kode `1` (Kering) |
| `light_conditions` (Kategori) | 16 | 0,02% | Modus = Kode `1` (Terang) |
| `urban_or_rural_area` (Kategori) | 4 | < 0,01% | Modus = Kode `1` (Perkotaan) |

Setelah tahap ini selesai, total *missing values* pada seluruh dataset menjadi **0**.

### 3.4 *One-Hot Encoding*
Teknik *One-Hot Encoding* diterapkan menggunakan `OneHotEncoder` pada lima fitur kategorikal nominal agar kode kategori tidak disalahartikan sebagai angka urutan bertingkat. Sebagai contoh, baris dengan `urban_or_rural_area = Urban` dipecah menjadi dua kolom biner: `Urban = 1` dan `Rural = 0`. Sementara itu, `collision_severity` (1 = Fatal, 2 = Serious, 3 = Slight) **tidak** di-*One-Hot Encoding* karena bertipe ordinal sekaligus menjadi variabel target. Dimensi dataset akhir berubah dari **101.525 × 16** menjadi **101.525 baris × 39 kolom** (16 − 5 kolom asli + 28 kolom biner):

| Fitur Awal (Nominal) | Jumlah Kategori | Contoh Kolom Biner Baru (Nilai 0 / 1) |
| :--- | :---: | :--- |
| `road_type` | 6 | `road_type_Roundabout`, `road_type_SingleCarriageway`, dll. |
| `weather_conditions` | 9 | `weather_conditions_Fine_NoHighWinds`, `weather_conditions_Raining_NoHighWinds`, dll. |
| `light_conditions` | 5 | `light_conditions_Light_1`, `Light_4`, `Light_5`, `Light_6`, `Light_7` |
| `road_surface_conditions` | 6 | `road_surface_conditions_Dry`, `road_surface_conditions_WetOrDamp`, dll. |
| `urban_or_rural_area` | 2 | `urban_or_rural_area_Urban`, `urban_or_rural_area_Rural` |
| **Total Kolom Baru** | **28** | **Menggantikan 5 fitur nominal awal menjadi 28 kolom biner (0 / 1)** |

---

## 4. Kesimpulan
Dari total 99 kolom asli pada Dataset *UK Road Safety 2025* (101.525 kejadian), dipilih 15 parameter utama yang paling bersih dan relevan, kemudian dieksplorasi melalui EDA (distribusi, *outlier* IQR, dan korelasi 11 fitur) serta diolah melalui *merging*, pembersihan kode `-1`, validasi, penghapusan `age_of_vehicle`, imputasi median/modus, hingga *One-Hot Encoding*. Dataset akhir berukuran **101.525 baris × 39 kolom** sudah bersih sempurna (0 duplikasi, 0 nilai kosong) dan siap digunakan.

## Referensi
1. Department for Transport (DfT). (2025). *Road Safety Open Dataset 2025: Collision, Vehicle, Casualty, and Data Guide*. United Kingdom.
2. Nasution, S. M. & Tim Pengajar Data Sains. (2026). *Materi Kuliah Data Sains dan Analisis: Week 3–6 & Modul LMS Pertemuan 01, 04–07, 09*.
