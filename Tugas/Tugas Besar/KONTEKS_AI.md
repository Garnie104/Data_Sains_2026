# Konteks AI — Tugas Besar Mata Kuliah Data Sains (Pengganti UTS)

Dokumen ini merangkum hasil analisis instruksi, klarifikasi ruang lingkup, pemetaan materi referensi, serta aturan pengerjaan Tugas Besar agar AI (dan pengembang) memiliki pemahaman yang seragam dan akurat.

---

## 1. Informasi Umum & Ruang Lingkup
- **Sumber Instruksi Asli:** [Instruksi.txt](file:///c:/Users/LENOVO/Documents/Data%20Sains/Tugas/Tugas%20Besar/Instruksi.txt)
- **Fungsi Tugas:** Laporan Tugas Besar sebagai **pengganti UTS**.
- **Format Pengumpulan:** Dikumpulkan dalam **bentuk fisik (*hardcopy*)** (sehingga desain laporan PDF perlu rapi, jelas dibaca saat dicetak, dengan margin dan ukuran grafik/tabel yang sesuai untuk cetak).
- **Format Laporan Acuan:** Menggunakan **versi ringkas** (`Laporan_Ringkas_Tugas_Besar_Data_Sains.*` — langsung ke inti materi data sains tanpa pengantar/metodologi berbelit-belit). Dokumen versi lengkap diarsipkan terpisah pada folder `Hasil jadi/Arsip Laporan Lengkap/`.
- **Deadline & Presentasi:**
  - Deadline pengerjaan: **1 minggu**.
  - Presentasi dimulai **tanggal 20** (perlu membuat janji jadwal sendiri).
- **Batas Ruang Lingkup (PENTING):**
  - Pengerjaan **TIDAK sampai tahap Machine Learning / Modeling / Evaluasi Model** (tahap modeling akan dilanjutkan menjelang UAS).
  - Fokus penuh pada: **Struktur Data**, **EDA**, serta **Pre-processing / Data Construction**.

---

## 2. Dataset yang Digunakan
Tugas Besar ini menggunakan **Dataset Kecelakaan UK 2025** yang berada di folder `dataset kecelakan UK/`:
1. `dft-road-casualty-statistics-collision-2025.csv` (data kejadian tabrakan)
2. `dft-road-casualty-statistics-vehicle-2025.csv` (data kendaraan terlibat)
3. `dft-road-casualty-statistics-casualty-2025.csv` (data korban)
4. `dft-road-casualty-statistics-road-safety-open-dataset-data-guide-2025.xlsx` (kamus data / panduan kode)

> **Catatan:** Folder `Dataset lalu lintas bdg, jkt, smg/` **tidak digunakan** untuk Tugas Besar ini.

---

## 3. Pemetaan Materi Referensi (Gabungan Pak Surya & LMS)
Instruksi mengacu pada materi pertemuan 1–7 (*Slide 1–7*). Karena berkas slide di kedua folder masing-masing tidak utuh 1–7, digunakan **gabungan** dari `Materi dari pak Surya/` dan `Materi di lms/` yang terbukti saling melengkapi:

| Tahap Materi | Materi Pak Surya | Materi LMS | Keterangan Kelengkapan |
| :--- | :--- | :--- | :--- |
| **Pengantar & Tools** | *(Week 1–2 tidak ada)* | `Pertemuan 01`, `Pertemuan 04` | Ditutupi oleh materi LMS |
| **Data Understanding 1 (Statistik)** | `Week 3 - SMC.pdf` | `Pertemuan 05` | Topik identik |
| **Data Understanding 2 (Visualisasi)** | `Week 4 - SMC.pdf` | `Pertemuan 06` | Topik identik (48 halaman) |
| **Data Preparation 1 & 2 (Selecting, Cleaning, Validation)** | `Week 5 - SMC.pdf` | `Pertemuan 07` *(P08 tidak ada)* | **`Week 5` Pak Surya menutupi `Pertemuan 08` LMS yang kosong** (lengkap membahas *Cleaning* & *Validasi Data*) |
| **Data Preparation 3 (Data Construction)** | `Week 6 - SMC.pdf` | `Pertemuan 09` | Di `Pertemuan 09` terdapat materi **`Hands-on: OneHotEncoding`** (hal. 70–75) dan **`Image Segmentation`** (hal. 96–107) |

### Referensi Tambahan (`video materi di lms/`)
- Seluruh 6 link video YouTube (`Video 1` s.d. `Video 6`) berstatus aktif dan publik.
- `Video 1`, `Video 2`, `Video 3`, `Video 4`, dan `Video 6` memiliki transkrip/subtitle bawaan YouTube yang dapat diekstrak bila dibutuhkan.
- `Video 5` (*Data Visualization: Overview* — Bing Wen Brunton) tidak memiliki transkrip bawaan di payload awal, namun metadata/deskripsinya aktif.

---

## 4. Checklist Komponen Wajib Laporan & Klarifikasi Istilah

1. **Struktur Data**
   - Jelaskan struktur tabel, jumlah baris & kolom, tipe data tiap fitur, relasi antar file CSV (`accident_index` / kunci penghubung), dan pemetaan kode dari file panduan `.xlsx`.

2. **Exploratory Data Analysis (EDA)**
   - Statistik deskriptif dan visualisasi data yang relevan.
   - **Deteksi Outlier:** Temukan dan analisis outlier pada fitur numerik yang relevan (misalnya dengan metode IQR / Boxplot / Z-Score).
   - **Analisis Korelasi:** Hitung dan visualisasikan korelasi antar variabel, serta **jelaskan secara eksplisit fitur/data apa saja yang dimasukkan ke dalam perhitungan korelasi** beserta alasannya.

3. **Data Pre-processing (Mengacu Materi 1–7 / Gabungan Slide)**
   - **Selecting / Filtering:** Pemilihan fitur/objek yang relevan.
   - **Cleaning:** Penanganan duplikasi, format tidak konsisten, nilai tidak valid (pada dataset UK Road Safety, perhatikan kode `-1` yang biasanya menandakan *Data missing or out of range*).
   - **Validation:** Validasi tipe data, rentang nilai, dan integritas referensial antar tabel.
   - **Imputasi *(klarifikasi istilah `input`)*:** Kata `input` pada `Instruksi.txt` merujuk pada **Imputasi (*Imputation*)** sesuai pembahasan di `Week 6 - SMC.pdf` dan `Pertemuan 09` (penanganan *missing values* menggunakan metode *mean/median*, *arbitrary*, *end-of-tail*, atau penghapusan bila sesuai).
   - **Data Construction — One-Hot Encoding (WAJIB):** Terapkan **One-Hot Encoding** untuk fitur kategorikal nominal yang sesuai (mengacu pada `Pertemuan 09` hal. 70–75).
   - **Penyesuaian Jenis Data:** **Dilarang memaksakan teknik data citra seperti *Image Segmentation*** karena dataset yang digunakan adalah data tabular, bukan gambar.
