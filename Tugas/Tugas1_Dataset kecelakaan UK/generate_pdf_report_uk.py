import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class UKAccidentPDFReport(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, "Tugas 1 Data Sains: Exploratory Data Analysis (EDA) - UK Road Safety 2025", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(210, 210, 210)
            self.line(18, self.get_y(), 192, self.get_y())
            self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Halaman {self.page_no()} | Laporan Tugas 1 Data Sains - Kelompok", align="C")

    def chapter_title(self, num, title):
        self.set_font("Helvetica", "B", 12.5)
        self.set_text_color(24, 43, 73)  # Navy blue
        self.set_fill_color(240, 244, 248)
        self.cell(0, 7.5, f"  {num}. {title}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(35, 75, 120)
        self.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 4.8, text)
        self.ln(1.5)

    def callout_box(self, title, text):
        self.set_fill_color(245, 248, 252)
        self.set_draw_color(180, 205, 230)
        start_y = self.get_y()
        # Draw background and border
        self.set_font("Helvetica", "B", 8.5)
        self.set_text_color(24, 43, 73)
        self.cell(0, 5, f"[Insight] {title}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 4.3, text)
        self.ln(2)

    def table_header(self, col_widths, headers):
        self.set_font("Helvetica", "B", 8.5)
        self.set_fill_color(41, 74, 110)
        self.set_text_color(255, 255, 255)
        for w, h in zip(col_widths, headers):
            self.cell(w, 6, h, border=1, align="C", fill=True)
        self.ln()

    def table_row(self, col_widths, values, fill=False, align_list=None):
        self.set_font("Helvetica", "", 8)
        self.set_text_color(30, 30, 30)
        if fill:
            self.set_fill_color(245, 247, 250)
        else:
            self.set_fill_color(255, 255, 255)
        
        for i, (w, val) in enumerate(zip(col_widths, values)):
            al = align_list[i] if align_list else "L"
            self.cell(w, 5.2, str(val), border=1, align=al, fill=fill)
        self.ln()


def generate_uk_report():
    pdf = UKAccidentPDFReport()
    
    # -------------------------------------------------------------
    # HALAMAN 1: COVER & IDENTITAS + RINGKASAN EKSEKUTIF
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.ln(5)
    
    # Header Banner
    pdf.set_fill_color(24, 43, 73)
    pdf.rect(18, 15, 174, 32, 'F')
    
    pdf.set_xy(18, 19)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(174, 7, "LAPORAN ANALISIS DATA EKSPLORATIF (EDA)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(220, 230, 242)
    pdf.cell(174, 5.5, "Karakteristik, Pola Temporal, dan Faktor Risiko Kecelakaan Lalu Lintas di UK", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(174, 5, "(UK Department for Transport - Road Safety Open Dataset 2025)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(10)
    
    # Metadata Box
    pdf.set_fill_color(247, 249, 252)
    pdf.set_draw_color(200, 215, 230)
    pdf.rect(18, pdf.get_y(), 174, 42, 'DF')
    pdf.set_xy(22, pdf.get_y() + 3)
    
    meta_items = [
        ("Mata Kuliah", ": Data Sains / Sains Data (Tugas 1 - Minggu ke-3)"),
        ("Topik Analisis", ": Transportation (Sistem Keselamatan Jalan Raya & Kecelakaan)"),
        ("Skala Dataset", ": 101,525 Insiden Tabrakan, 127,883 Korban, 183,948 Kendaraan"),
        ("Sumber Data", ": UK Department for Transport (GOV.UK Open Data / Kaggle)"),
        ("Anggota Kelompok", ": [Nama Mahasiswa 1 / NIM], [Nama Mahasiswa 2 / NIM], [Nama Mahasiswa 3 / NIM]"),
        ("Batas Pengumpulan", ": Selasa, 17 Maret 2025, Pukul 23:59 WIB")
    ]
    
    for label, val in meta_items:
        pdf.set_x(22)
        pdf.set_font("Helvetica", "B", 8.5)
        pdf.set_text_color(24, 43, 73)
        pdf.cell(34, 5.8, label, 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_font("Helvetica", "", 8.5)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(0, 5.8, val, 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
    pdf.ln(8)
    
    # Bab 1: Pendahuluan
    pdf.chapter_title("1", "PENDAHULUAN & RINGKASAN EKSEKUTIF")
    pdf.body_text(
        "Kecelakaan lalu lintas merupakan salah satu tantangan keselamatan publik dan ekonomi terbesar di dunia. "
        "Di Britania Raya (UK), Departemen Transportasi (Department for Transport - DfT) secara sistematis merekam setiap "
        "insiden tabrakan jalan raya yang dilaporkan oleh kepolisian melalui instrumen STATS19. Pada Tugas 1 ini, kelompok kami "
        "melakukan Analisis Data Eksploratif (Exploratory Data Analysis - EDA) secara komprehensif terhadap dataset UK Road Safety 2025."
    )
    pdf.body_text(
        "Tujuan utama EDA ini adalah untuk mengidentifikasi integritas data, meneliti disparitas temporal (jam sibuk vs jam lengang), "
        "menganalisis dampak batas kecepatan (speed limit) terhadap tingkat fatalitas korban, mengkaji pengaruh kondisi cuaca dan "
        "permukaan jalan, serta mendeteksi insiden anomali (outlier). Hasil analisis ini menjadi fondasi empiris dalam merancang "
        "kebijakan keselamatan jalan dan mempersiapkan model prediktif Machine Learning pada tugas berikutnya."
    )
    pdf.body_text(
        "Temuan utama menunjukkan bahwa kejadian kecelakaan mencapai titik puncak tertinggi pada sore hari (17:00) dan hari Jumat. "
        "Risiko kematian melonjak drastis secara non-linear sebesar 7.25 kali lipat pada jalan 60 mph dibandingkan zona 20 mph. "
        "Selain itu, lebih dari 82% insiden justru terjadi saat cuaca cerah dan jalanan kering (efek kompensasi risiko / Peltzman Effect)."
    )
    
    # -------------------------------------------------------------
    # HALAMAN 2: STRUKTUR DATASET & QUALITY CHECK
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("2", "DESKRIPSI & STRUKTUR DATASET")
    pdf.body_text(
        "Dataset UK Road Safety 2025 terstruktur dalam format relasional tabular yang saling terhubung melalui kunci unik "
        "collision_index dan collision_ref_no. Arsitektur ini memungkinkan penelusuran relasi 1 : N (satu insiden kecelakaan dapat "
        "melibatkan banyak kendaraan dan menyebabkan banyak korban manusia)."
    )
    
    # Table 1: Dataset Scope
    w_scope = [52, 28, 22, 26, 46]
    h_scope = ["Nama Berkas CSV", "Entitas Utama", "Baris", "Kolom", "Keterangan Variabel"]
    pdf.table_header(w_scope, h_scope)
    pdf.table_row(w_scope, ["collision-2025.csv", "Insiden Tabrakan", "101,525", "44", "Waktu, lokasi, cuaca, severity"], fill=False, align_list=["L","L","C","C","L"])
    pdf.table_row(w_scope, ["casualty-2025.csv", "Korban Terdampak", "127,883", "23", "Demografi, peran korban, keparahan"], fill=True, align_list=["L","L","C","C","L"])
    pdf.table_row(w_scope, ["vehicle-2025.csv", "Kendaraan Terlibat", "183,948", "32", "Tipe kendaraan, manuver, usia"], fill=False, align_list=["L","L","C","C","L"])
    pdf.table_row(w_scope, ["TOTAL RELASIONAL", "Ekosistem Terpadu", "413,356", "99", "Integritas referensial 100% cocok"], fill=True, align_list=["L","L","C","C","L"])
    pdf.ln(3)

    pdf.section_title("2.1 Pemeriksaan Kualitas Data (Data Quality Check)")
    pdf.body_text(
        "Pemeriksaan data menyeluruh menunjukkan integritas dan kebersihan dataset yang sangat tinggi: "
        "1) Pada tabel utama collision, koordinat latitude dan longitude hanya memiliki 2 nilai kosong dari 101,525 baris (kelengkapan 99.998%); "
        "2) Total korban pada tabel collision sama persis dengan total baris pada tabel casualty (127,883 korban); "
        "3) Total kendaraan yang dilaporkan sama persis dengan tabel vehicle (183,948 unit). Seluruh kode numerik dari panduan DfT "
        "didekodekan menjadi label teks semantik berbahasa Indonesia untuk menjamin kemudahan interpretasi."
    )
    
    # Table 2: Decoding Table
    w_dec = [40, 36, 98]
    h_dec = ["Fitur Asli (DfT)", "Nilai Kode", "Label Semantik & Interpretasi"]
    pdf.table_header(w_dec, h_dec)
    pdf.table_row(w_dec, ["collision_severity", "1, 2, 3", "1: Fatal (Tewas), 2: Serious (Luka Berat), 3: Slight (Luka Ringan)"], fill=False)
    pdf.table_row(w_dec, ["day_of_week", "1 s.d. 7", "1: Minggu, 2: Senin, 3: Selasa, 4: Rabu, 5: Kamis, 6: Jumat, 7: Sabtu"], fill=True)
    pdf.table_row(w_dec, ["speed_limit", "20, 30, 40, 50, 60, 70", "Batas kecepatan legal pada ruas jalan dalam mil per jam (mph)"], fill=False)
    pdf.table_row(w_dec, ["weather_conditions", "1 s.d. 9", "1: Cerah, 2: Hujan, 3: Salju, 4: Cerah berangin, 5: Hujan berangin, 7: Kabut"], fill=True)
    pdf.table_row(w_dec, ["road_surface", "1 s.d. 5", "1: Kering (Dry), 2: Basah/Becek (Wet), 3: Salju, 4: Licin Es, 5: Banjir"], fill=False)
    pdf.ln(3)

    pdf.chapter_title("3", "HASIL ANALISIS DATA EKSPLORATIF (EDA)")
    pdf.body_text(
        "Analisis data eksploratif dilakukan melalui pendekatan univariat, bivariat, dan deteksi nilai ekstrem (outlier) "
        "menggunakan pustaka Python (Pandas, Matplotlib, Seaborn). Berikut adalah hasil temuan pada masing-masing dimensi."
    )

    # -------------------------------------------------------------
    # HALAMAN 3: DISTRIBUSI SEVERITY & KELAS TIDAK SEIMBANG
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.section_title("3.1 Distribusi Tingkat Keparahan Tabrakan (Collision Severity)")
    pdf.body_text(
        "Kategori keparahan insiden dikelompokkan menjadi tiga tingkat oleh kepolisian: Slight (luka ringan), Serious (luka berat/rawat inap), "
        "dan Fatal (meninggal dunia). Gambar 1 menyajikan sebaran frekuensi dan proporsi masing-masing kelas."
    )
    
    chart1_path = "eda_output/1_distribusi_keparahan.png"
    if os.path.exists(chart1_path):
        pdf.image(chart1_path, x=25, y=pdf.get_y(), w=145)
        pdf.set_y(pdf.get_y() + 92)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 1: Distribusi Tingkat Keparahan Kecelakaan (UK Road Safety 2025)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # Table 3: Severity Stats
    w_sev = [40, 32, 32, 70]
    h_sev = ["Tingkat Keparahan", "Banyak Kejadian", "Proporsi (%)", "Definisi Operasional STATS19"]
    pdf.table_header(w_sev, h_sev)
    pdf.table_row(w_sev, ["Slight (Ringan)", "74,881", "73.76%", "Luka memar, lecet, terkilir, tidak butuh opname"], fill=False, align_list=["L","C","C","L"])
    pdf.table_row(w_sev, ["Serious (Berat)", "25,191", "24.81%", "Patah tulang, luka dalam parah, rawat inap RS"], fill=True, align_list=["L","C","C","L"])
    pdf.table_row(w_sev, ["Fatal (Meninggal)", "1,453", "1.43%", "Meninggal di lokasi atau dalam kurun 30 hari"], fill=False, align_list=["L","C","C","L"])
    pdf.table_row(w_sev, ["TOTAL TABRAKAN", "101,525", "100.0%", "Seluruh insiden resmi tercatat selama 2025"], fill=True, align_list=["L","C","C","L"])
    pdf.ln(2)

    pdf.callout_box(
        "Implikasi Machine Learning: Extreme Class Imbalance",
        "Data memperlihatkan ketidakseimbangan kelas ekstrem di mana kelas minoritas (Fatal) hanya berjumlah 1.43%. "
        "Penggunaan metrik Akurasi akan sangat menyesatkan karena model naif yang selalu memprediksi non-fatal akan memperoleh "
        "akurasi semu sebesar 98.57%. Pada tahap pemodelan klasifikasi prediktif, wajib diterapkan teknik penyeimbangan data "
        "(seperti SMOTE atau focal loss) serta evaluasi menggunakan Macro F1-Score dan Area Under Precision-Recall Curve (PR-AUC)."
    )

    # -------------------------------------------------------------
    # HALAMAN 4: ANALISIS TEMPORAL (JAM & HARI)
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.section_title("3.2 Analisis Temporal 24 Jam: Pola Bimodal Jam Sibuk")
    pdf.body_text(
        "Analisis sebaran kejadian berdasarkan 24 jam dalam sehari (Gambar 2) menunjukkan pola kurva Bimodal Distribution yang sangat tegas, "
        "yang mencerminkan ritme mobilitas komuter di Britania Raya."
    )
    
    chart2_path = "eda_output/2_tren_jam_kejadian.png"
    if os.path.exists(chart2_path):
        pdf.image(chart2_path, x=18, y=pdf.get_y(), w=174)
        pdf.set_y(pdf.get_y() + 72)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 2: Fluktuasi Jumlah Kejadian Tabrakan Berdasarkan Jam dalam Sehari (00:00 - 23:00)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1.5)

    pdf.body_text(
        "Puncak pertama terjadi pada jam sibuk pagi (Morning Peak, pukul 08:00) dengan 6,716 kejadian saat masyarakat berangkat kerja. "
        "Puncak kedua yang jauh lebih masif terjadi pada sore hari (Evening Peak, 15:00-18:00) dengan puncaknya pada pukul 17:00 (8,877 insiden). "
        "Rentang waktu sore menyumbang 32.4% dari seluruh kecelakaan harian karena kombinasi faktor kelelahan kerja (fatigue) dan mobilitas beragam."
    )
    
    pdf.section_title("3.3 Distribusi Kejadian Berdasarkan Hari dalam Seminggu")
    pdf.body_text(
        "Gambar 3 memperlihatkan tren kecelakaan harian. Hari Jumat mencatat angka kecelakaan tertinggi sebesar 16,811 insiden (16.56%), "
        "diikuti hari Rabu (15,369) dan Kamis (15,304). Hari Minggu merupakan hari paling tenang dengan 11,197 insiden (11.03%)."
    )
    
    chart3_path = "eda_output/3_distribusi_hari.png"
    if os.path.exists(chart3_path):
        pdf.image(chart3_path, x=24, y=pdf.get_y(), w=146)
        pdf.set_y(pdf.get_y() + 82)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 3: Distribusi Frekuensi Kecelakaan Berdasarkan Hari dalam Seminggu", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    # -------------------------------------------------------------
    # HALAMAN 5: SPEED LIMIT VS SEVERITY
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.section_title("3.4 Hubungan Batas Kecepatan (Speed Limit) Terhadap Tingkat Fatalitas")
    pdf.body_text(
        "Kecepatan kendaraan merupakan determinan fisik utama yang menentukan besaran energi kinetik saat benturan. "
        "Gambar 4 dan Tabel 4 membandingkan proporsi keparahan tabrakan pada enam klasifikasi batas kecepatan jalan legal di UK."
    )
    
    chart4_path = "eda_output/4_speed_limit_vs_severity.png"
    if os.path.exists(chart4_path):
        pdf.image(chart4_path, x=22, y=pdf.get_y(), w=150)
        pdf.set_y(pdf.get_y() + 84)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 4: Proporsi Tingkat Keparahan Tabrakan Berdasarkan Batas Kecepatan Ruas Jalan (mph)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # Table 4: Speed limit crosstab
    w_spd = [32, 28, 28, 28, 28, 30]
    h_spd = ["Speed Limit", "Kecepatan (km/j)", "Slight (%)", "Serious (%)", "Fatal (%)", "Rasio vs 20 mph"]
    pdf.table_header(w_spd, h_spd)
    speed_rows = [
        ["20 mph", "~32 km/jam", "77.65%", "21.84%", "0.51%", "1.00x (Acuan)"],
        ["30 mph", "~48 km/jam", "75.19%", "23.95%", "0.86%", "1.69x"],
        ["40 mph", "~64 km/jam", "72.73%", "25.42%", "1.85%", "3.63x"],
        ["50 mph", "~80 km/jam", "70.42%", "27.10%", "2.47%", "4.84x"],
        ["60 mph", "~96 km/jam", "63.62%", "32.68%", "3.70%", "7.25x"],
        ["70 mph", "~112 km/jam", "74.46%", "22.43%", "3.11%", "6.10x"]
    ]
    for i, row in enumerate(speed_rows):
        pdf.table_row(w_spd, row, fill=(i%2==1), align_list=["C","C","C","C","C","C"])
    pdf.ln(2)

    pdf.callout_box(
        "Fisika Tabrakan: Risiko Fatalitas Meningkat 7.25 Kali Lipat di Jalan 60 mph",
        "Probabilitas kecelakaan berujung fatal meningkat secara tajam dari 0.51% pada zona 20 mph menjadi 3.70% pada jalan 60 mph. "
        "Ruas jalan 60 mph (jalan antar-kota satu lajur / single carriageway rural roads) terbukti menjadi segmen paling mematikan di UK. "
        "Sebaliknya, pada jalan tol 70 mph (motorway), fatalitas sedikit menurun (3.11%) karena adanya median pemisah fisik jalur dan ketiadaan pejalan kaki."
    )

    # -------------------------------------------------------------
    # HALAMAN 6: KONDISI LINGKUNGAN & DETEKSI OUTLIER
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.section_title("3.5 Pengaruh Kondisi Cuaca & Lingkungan Jalan")
    pdf.body_text(
        "Investigasi terhadap faktor cuaca (Gambar 5) mengungkap fenomena yang sangat kontras dengan persepsi umum. "
        "Sebanyak 83,405 insiden (82.15%) terjadi saat cuaca Cerah tanpa angin, dan 74.54% terjadi pada jalanan Kering."
    )
    
    chart5_path = "eda_output/5_cuaca_dominan.png"
    if os.path.exists(chart5_path):
        pdf.image(chart5_path, x=20, y=pdf.get_y(), w=154)
        pdf.set_y(pdf.get_y() + 78)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 5: Distribusi Frekuensi Kejadian Kecelakaan Berdasarkan Kondisi Cuaca", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    pdf.section_title("3.6 Deteksi Nilai Ekstrem (Outliers) pada Korban dan Kendaraan")
    pdf.body_text(
        "Gambar 6 memperlihatkan boxplot sebaran jumlah kendaraan dan jumlah korban per insiden. Rata-rata kendaraan terlibat "
        "adalah 1.81 unit (median 2), dan rata-rata korban manusia adalah 1.26 jiwa (median 1)."
    )
    
    chart6_path = "eda_output/6_outlier_kendaraan_korban.png"
    if os.path.exists(chart6_path):
        pdf.image(chart6_path, x=18, y=pdf.get_y(), w=174)
        pdf.set_y(pdf.get_y() + 70)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 6: Boxplot Deteksi Pencilan (Outliers) Jumlah Kendaraan dan Korban per Kejadian", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    pdf.callout_box(
        "Deteksi Insiden Ekstrem: Tabrakan Beruntun 17 Kendaraan & 142 Korban",
        "Meskipun mayoritas kecelakaan bersifat bilateral (2 kendaraan), visualisasi mengidentifikasi pencilan ekstrem: "
        "1) Rekor tabrakan beruntun melibatkan 17 kendaraan sekaligus di jalan bebas hambatan; "
        "2) Rekor insiden dengan 142 korban manusia dalam satu peristiwa kecelakaan massal (melibatkan bus penumpang umum)."
    )

    # -------------------------------------------------------------
    # HALAMAN 7: KESIMPULAN, ROADMAP ML, & DAFTAR PUSTAKA
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("4", "TEMUAN KUNCI & REKOMENDASI KEBIJAKAN TRANSPORTASI")
    pdf.body_text(
        "Berdasarkan analisis data eksploratif terhadap 101,525 rekaman kecelakaan UK 2025, dirumuskan rekomendasi praktis:"
    )
    pdf.body_text(
        "1. Kebijakan Batas Kecepatan 20 mph: Memperluas penetapan zona kecepatan 20 mph di seluruh kawasan pemukiman, sekolah, "
        "dan pusat perbelanjaan, karena zona ini terbukti menekan angka fatalitas hingga level terendah (0.51%)."
    )
    pdf.body_text(
        "2. Rekayasa Geometrik Jalan Rural 60 mph: Jalan pedesaan tanpa pemisah jalur membutuhkan pemasangan median fleksibel dan "
        "marka getar (rumble strips) untuk mencegah tabrakan berlawanan arah (head-on collision) yang mematikan."
    )
    pdf.body_text(
        "3. Manajemen Patroli Waktu Puncak: Otoritas kepolisian perlu mengonsentrasikan pengawasan lalu lintas dan ambulans siaga pada "
        "hari Jumat pukul 15:00 hingga 18:00 sebagai jendela waktu paling kritis dalam sepekan."
    )
    
    pdf.ln(1)
    pdf.chapter_title("5", "RENCANA PEMODELAN DATA SAINS (MACHINE LEARNING ROADMAP)")
    pdf.body_text(
        "Sebagai kelanjutan Tugas 1 ini, kelompok kami merancang tahapan pemodelan Machine Learning:"
    )
    pdf.body_text(
        "- Klasifikasi Prediksi Keparahan (Severity Classification): Membangun model berbasis Gradient Boosting (XGBoost / LightGBM) "
        "untuk memprediksi probabilitas keparahan tabrakan secara real-time berdasarkan variabel cuaca, waktu, dan infrastruktur jalan."
    )
    pdf.body_text(
        "- Spatio-Temporal Hotspot Clustering: Menggunakan algoritma geospasial DBSCAN / HDBSCAN pada koordinat latitude/longitude "
        "untuk memetakan klaster titik hitam (blackspot) kecelakaan jalan raya secara otomatis."
    )
    pdf.body_text(
        "- Penanganan Data Tidak Seimbang: Menerapkan SMOTE dan cost-sensitive weighting guna mengatasi ketidakseimbangan kelas 1.43% fatal."
    )
    
    pdf.ln(1)
    pdf.chapter_title("6", "DAFTAR PUSTAKA & REFERENSI RESMI")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(60, 60, 60)
    
    refs = [
        "1. Department for Transport (DfT), UK. (2025). Reported Road Casualties Great Britain: Road Safety Open Dataset 2025. GOV.UK.",
        "2. World Health Organization (WHO). (2023). Global Status Report on Road Safety 2023. Geneva: WHO Press.",
        "3. Peltzman, S. (1975). The Effects of Automobile Safety Regulation. Journal of Political Economy, 83(4), 677-725.",
        "4. Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley Publishing Company.",
        "5. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. JAIR, 16, 321-357."
    ]
    for r in refs:
        pdf.multi_cell(0, 4.2, r)
        pdf.ln(1)
        
    output_pdf = "Laporan_Tugas1_Data_Sains_EDA_Kecelakaan_UK.pdf"
    pdf.output(output_pdf)
    print(f"PDF Successfully generated: {output_pdf}")

if __name__ == "__main__":
    generate_uk_report()
