# Analisis Detail & Menyeluruh Video Materi Data Sains (LMS)

Dokumen ini berisi hasil ekstraksi dan analisis mendalam terhadap seluruh 6 video materi yang terdapat pada folder `video materi di lms/`, serta pemetaan relevansinya terhadap pengerjaan **Tugas Besar Data Sains (Dataset UK Road Safety 2025)**.

---

## Ringkasan Peta Video Materi

| Video | Judul | Pembuat / Kanal | Durasi | Sumber Analisis | Fokus Utama | Relevansi ke Tugas Besar (UTS) |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
| **Video 1** | *Intro to Data Science: What is Data Science?* | Steve Brunton | 08:15 | Transkrip YouTube | Siklus Data Science, *Data Cleaning*, *Visualization*, & *T-shaped skills* | **Tinggi** (Konsep siklus feedback, cleaning, outlier & visualisasi) |
| **Video 2** | *Welcome to Data Science Methodology 101* | Cognitive Class (IBM) | 04:10 | Transkrip YouTube | Metodologi Data Science IBM (John Rollins — 10 Pertanyaan Terstruktur) | **Sedang–Tinggi** (Kerangka berpikir terstruktur sebelum olah data) |
| **Video 3** | *Complete Python Pandas Data Science Tutorial!* | Keith Galli | 60:26 | Transkrip & Outline Resmi | Tutorial lengkap `pandas` (CSV/Excel, filter, sorting, `groupby`, `chunksize`) | **Sangat Tinggi** (Seluruh teknik inti dipakai di `.ipynb`) |
| **Video 4** | *Working with APIs in Python [For Your Data Science Project]* | StrataScratch | 28:32 | Transkrip YouTube | Pengumpulan data via REST API (`requests`), parsing JSON ke DataFrame | **Rendah** (Untuk data API; dataset Tugas Besar sudah berupa CSV lokal) |
| **Video 5** | *Data Visualization: Overview* | Bing Wen Brunton | 04:55 | Deskripsi & Referensi Kuliah *(Subtitle nonaktif)* | Tujuan visualisasi: *Exploration* vs *Communication* | **Tinggi** (Prinsip grafik EDA vs grafik laporan) |
| **Video 6** | *Data cleaning and preparation* | Prof. Fabian Froese | 24:00 | Transkrip YouTube | Pembersihan data, *Bias*, Asumsi Statistik, *Winsorizing*, *Recoding*, & Transformasi | **Sangat Tinggi** (Landasan teori cleaning, outlier, encoding & transformasi) |

---

## 1. Analisis Video 1: *Intro to Data Science: What is Data Science?*
- **Link:** https://www.youtube.com/watch?v=FsSrzmRawUg
- **Pembuat:** Steve Brunton (University of Washington) | **Durasi:** 8 menit 15 detik

### Poin-Poin Inti dari Transkrip:
1. **Data Science sebagai *Data-Driven Inquiry*:** Inti dari Data Science bukan sekadar algoritma, melainkan kemampuan mengajukan pertanyaan yang tepat dan menjawabnya menggunakan data dalam sebuah **siklus umpan balik (*feedback cycle*)**.
2. **Porsi Terbesar adalah *Data Engineering* & *Cleaning*:** Sebagian besar waktu kerja di dunia nyata dihabiskan untuk mengumpulkan, menyimpan, mengkurasi, dan membersihkan data (*collecting, curating, storing, cleaning*). Data dunia nyata selalu berantakan (*messy*), sehingga identifikasi outlier dan pengisian *missing data* adalah langkah krusial sebelum masuk ke *Machine Learning*.
3. **Peringatan "Data Lake vs Data Creek":** Steve Brunton menekankan bahwa membangun tempat penyimpanan data besar (*Data Lake*) saja tidak cukup tanpa investasi pada analisis, visualisasi, dan pemodelan.
4. **Peran Visualisasi sebagai Komunikasi:** Manusia adalah makhluk visual. Ide atau temuan analisis sebaik apa pun tidak akan berdampak jika tidak mampu dikomunikasikan melalui visualisasi yang jelas.
5. **Kolaborasi Tim & *T-Shaped People*:** Data Science adalah seni kolaboratif yang membutuhkan tim dengan keahlian *T-shaped* (memiliki wawasan luas di banyak bidang terkait, sekaligus keahlian mendalam di satu bidang spesifik).

### Relevansi dengan Tugas Besar:
- Prinsip Steve Brunton tentang pentingnya membersihkan data, menangani *outlier* dan *missing values* sebelum masuk ke *Machine Learning* selaras 100% dengan batasan Tugas Besar UTS Anda (fokus EDA & Pre-processing sebelum Modeling di UAS).

---

## 2. Analisis Video 2: *Welcome to Data Science Methodology 101*
- **Link:** https://www.youtube.com/watch?v=gE6Ya-8OB78
- **Pembuat:** Cognitive Class (IBM) | **Durasi:** 4 menit 10 detik

### Poin-Poin Inti dari Transkrip:
1. **Pentingnya Metodologi:** Video ini memperingatkan bahaya langsung melompat ke solusi/model tanpa memahami pertanyaan masalah dan cara memanipulasi data secara tepat.
2. **Kerangka Kerja John Rollins (IBM):** Metodologi Data Science dibagi menjadi **10 pertanyaan dasar dalam urutan terstruktur**:
   - **2 pertanyaan awal:** Mendefinisikan masalah dan menentukan pendekatan analitik yang digunakan.
   - **4 pertanyaan tengah:** Mengorganisasi data yang dibutuhkan (kebutuhan data, pengumpulan, pemahaman, dan persiapan data).
   - **4 pertanyaan akhir:** Memvalidasi data dan pendekatan/model yang dirancang (pemodelan, evaluasi, *deployment*, dan *feedback*).
3. **Studi Kasus Kesehatan (Hospital Readmissions):** Menunjukkan bagaimana data historis rumah sakit dapat membantu dokter mengambil keputusan berbasis data untuk mengoptimalkan anggaran perawatan pasien.

### Relevansi dengan Tugas Besar:
- Tugas Besar Anda berada tepat pada fase awal hingga pertengahan metodologi IBM (memahami masalah & struktur data, mengumpulkan, memahami lewat EDA, dan mempersiapkan data lewat *pre-processing*).

---

## 3. Analisis Video 3: *Complete Python Pandas Data Science Tutorial!*
- **Link:** https://www.youtube.com/watch?v=vmEHCJofslg
- **Pembuat:** Keith Galli | **Durasi:** 60 menit 26 detik (menggunakan dataset Pokémon dari Kaggle)

### Poin-Poin Inti dari Transkrip & Struktur Materi:
1. **Mengapa `pandas` Lebih Unggul dari Excel:**
   - **Fleksibilitas penuh** bahasa pemrograman Python dibandingkan keterbatasan fitur Excel.
   - **Skalabilitas data besar** (*big data*), karena Excel melambat/gagal saat memuat file berukuran sangat besar.
2. **Operasi Dasar Pembacaan Data:**
   - Memuat file CSV, Excel, maupun TXT (`pd.read_csv`).
   - Membaca kolom, baris (`iloc`, `loc`), sel spesifik, dan melakukan iterasi baris.
   - Mendapatkan statistik ringkas data (`describe()` untuk `min`, `max`, `mean`, `std`).
3. **Sorting, Filtering & Modifikasi DataFrame:**
   - Mengurutkan data secara alfabetis maupun numerik (`sort_values`).
   - Menambah kolom baru, menghapus kolom (`drop`), menyusun ulang kolom, serta menyimpan hasil ke CSV/Excel baru.
   - *Filtering* lanjutan dengan banyak kondisi (`&`, `|`), *reset index* (`reset_index()`), serta *Regex Filtering* untuk pola teks.
   - Perubahan nilai bersyarat (*Conditional Changes*) pada kolom tertentu.
4. **Agregasi & Efisiensi Memori:**
   - Penggunaan **`groupby()`** (`sum`, `mean`, `count`) untuk meringkas ukuran DataFrame raksasa menjadi tabel ringkasan bermakna.
   - Bekerja dengan dataset berukuran gigabyte menggunakan parameter **`chunksize`** saat membaca file.

### Relevansi dengan Tugas Besar:
- **Sudah diterapkan langsung** di `Tugas_Besar_Data_Sains.ipynb`: penggunaan `pd.read_csv`, `.describe()`, *conditional filtering* (`>= 0`, rentang validasi), `.drop()`, serta **`groupby('collision_index').agg()`** untuk menggabungkan statistik tabel `Vehicle` ke `Collision`.

---

## 4. Analisis Video 4: *Working with APIs in Python [For Your Data Science Project]*
- **Link:** https://www.youtube.com/watch?v=fklHBWow8vE
- **Pembuat:** StrataScratch | **Durasi:** 28 menit 32 detik

### Poin-Poin Inti dari Transkrip:
1. **Alternatif Sumber Data:** Menjelaskan perbandingan mengumpulkan data proyek Data Science melalui **API**, mengimpor CSV, atau menarik dari database.
2. **Praktik Mengakses YouTube Data API v3:**
   - Menggunakan library **`requests`** di Python untuk melakukan HTTP request ke *endpoint* API menggunakan URL dan *API key*.
   - Membaca dokumentasi API resmi untuk menyusun parameter URL dengan benar.
3. **Parsing JSON ke Pandas DataFrame:**
   - Bagian tersulit dari bekerja dengan API adalah menelusuri struktur objek **JSON** bersarang (misal mengambil kunci `items` dan metrik statistik) melalui perulangan (`for loop`) dan menyimpannya ke dalam **Pandas DataFrame**.
4. **Fondasi Rekayasa Perangkat Lunak:** Merapikan kode panggilan API ke dalam fungsi terstruktur (*clean code*) sebelum tahap selanjutnya (mengunggah DataFrame ke database).

### Relevansi dengan Tugas Besar:
- **Tidak perlu diterapkan pada Tugas Besar ini**, karena dataset *UK Road Safety 2025* sudah tersedia lengkap dalam format file CSV lokal (`dataset kecelakan UK/`), bukan diambil secara *real-time* dari API eksternal.

---

## 5. Analisis Video 5: *Data Visualization: Overview*
- **Link:** https://www.youtube.com/watch?v=_XjE3ulgmDY
- **Pembuat:** Bing Wen Brunton (University of Washington) | **Durasi:** 4 menit 55 detik
- *(Catatan: Fitur subtitle/transkrip bawaan dinonaktifkan oleh pemilik video pada YouTube, sehingga analisis disusun berdasarkan deskripsi resmi video dan materi pengantar seri kuliah visualisasi data Bing Brunton).*

### Poin-Poin Inti Materi:
1. **Dua Fungsi Utama Visualisasi Data:**
   - **Untuk Eksplorasi (*Exploring Data*):** Membantu analis menemukan pola tersembunyi, tren waktu, anomali, maupun *outlier* yang sulit dilihat jika hanya menatap tabel angka mentah.
   - **Untuk Komunikasi (*Communicating Insights*):** Mengubah temuan kompleks menjadi grafik yang bersih, mudah dipahami audiens, dan mampu menceritakan pesan utama data secara efektif.
2. **Kekuatan Persepsi Visual Manusia:** Desain grafik yang baik memanfaatkan kemampuan alami mata manusia dalam mengenali warna, panjang, posisi, dan kontras agar kesimpulan dapat ditangkap dalam hitungan detik.

### Relevansi dengan Tugas Besar:
- **Sudah diterapkan** pada Laporan & Notebook: grafik eksplorasi (*Boxplot Outlier* & *Heatmap Korelasi*) serta grafik komunikasi yang rapi untuk laporan cetak (*Distribusi Keparahan*, *Hari*, dan *Tren Jam* beresolusi 300 DPI).

---

## 6. Analisis Video 6: *Data cleaning and preparation*
- **Link:** https://www.youtube.com/watch?v=2Jw5S5EbpwA
- **Pembuat:** Prof. Fabian Froese | **Durasi:** 24 menit 00 detik

### Poin-Poin Inti dari Transkrip:
Video ini membahas 3 pilar utama sebelum data dianalisis:
1. **Data Cleaning (Masalah Umum Data Mentah):**
   - *Unwanted respondents / irrelevant data:* Data yang tidak memenuhi syarat penelitian (perlu *filtering*).
   - *Incomplete responses & Missing values:* Nilai kosong baik secara acak maupun sistematis (*drop-out*).
   - *Wrong / erroneous inputs:* Kesalahan pengisian disengaja maupun tidak disengaja (contoh: ditanya umur, responden malah mengisi tahun lahir `1980`).
2. **Dampak Bias & Asumsi Statistik:**
   - Data kotor menimbulkan **bias** pada estimasi parameter (koefisien terlalu tinggi/rendah), *standard error*, dan *confidence interval*.
   - **Outlier:** Penanganan outlier sebaiknya diuji dengan membandingkan hasil analisis **dengan vs tanpa outlier**. Sering kali outlier menyimpan fenomena penting di balik angka ekstrem tersebut.
   - **Asumsi Analisis Multivariat:** Menjelaskan pentingnya *linearity*, *normal distribution*, *homogeneity of variance* (homoskedastisitas), dan *independence of errors*.
3. **Teknik Mengurangi Bias & Transformasi Data:**
   - **Winsorizing (mis. 95% Winsorizing):** Membatasi nilai ekstrem pada persentil ke-95 tanpa menghapus baris data.
   - **Recoding Data:** Mengubah kode survei (misalnya kode `1` dan `2` menjadi nilai biner **`0` dan `1`**) atau menggabungkan kategori menjadi klaster yang lebih sederhana.
   - **Transformasi Matematis:** Transformasi **Logaritma** (untuk meredam nilai ekstrem dan mendekati distribusi normal), serta **Standardisasi** (*mean = 0, std = 1*) dan *mean-centering*.

### Relevansi dengan Tugas Besar:
- **Sangat selaras dengan Pre-processing yang telah dikerjakan:**
  - Penanganan *erroneous/missing code* (`-1` → `NaN`, penghapusan kolom `age_of_vehicle` yang 100% kosong).
  - Keputusan mempertahankan *outlier* karena merepresentasikan fenomena nyata (tabrakan beruntun & kecelakaan bus) sesuai saran Prof. Fabian Froese.
  - Transformasi kode kategori ke biner `0`/`1` melalui **One-Hot Encoding**.
  - **Bekal untuk UAS:** Teknik *Winsorizing*, transformasi **Logaritma**, dan **Standardisasi** dari Video 6 ini dapat menjadi referensi tambahan yang sangat bagus saat masuk ke tahap pemodelan *Machine Learning* di UAS nanti.

---

## Kesimpulan Evaluasi terhadap Notebook (`Tugas_Besar_Data_Sains.ipynb`)

1. **Sudah Tercakup dengan Baik:** Seluruh materi inti yang relevan untuk tahap UTS dari Video 1, 2, 3, 5, dan 6 (siklus cleaning, penggunaan `pandas` & `groupby`, visualisasi eksploratif vs komunikasi, penanganan nilai salah/hilang, pertimbangan *outlier*, dan pengkodean biner `0`/`1`) **sudah diterapkan** di dalam `Tugas_Besar_Data_Sains.ipynb`.
2. **Bagian yang Sengaja Tidak Dipakai:** Video 4 (API `requests` & JSON) tidak relevan untuk UTS karena dataset sudah tersedia dalam bentuk CSV lokal.
3. **Rekomendasi untuk UAS:** Saat melanjutkan ke tahap *Machine Learning* menjelang UAS, Anda dapat menambahkan langkah **Standardisasi / Transformasi Logaritma** (dari Video 6) pada fitur numerik yang *skewed* seperti `engine_capacity_cc` atau `number_of_casualties` jika menggunakan model sensitif skala (seperti *Logistic Regression*, *SVM*, atau *KNN*).
