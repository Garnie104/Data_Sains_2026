import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class EDAPDFReport(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 6, "Tugas 1 Data Sains: Exploratory Data Analysis (EDA) - Transportasi Metropolitan", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(210, 210, 210)
            self.line(18, self.get_y(), 192, self.get_y())
            self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Halaman {self.page_no()} | Laporan Tugas 1 Data Sains - Kelompok", align="C")

    def chapter_title(self, num, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(24, 43, 73) # Navy blue
        self.set_fill_color(240, 244, 248)
        self.cell(0, 8, f"  {num}. {title}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(35, 75, 120)
        self.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5, text)
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
            self.cell(w, 5.5, str(val), border=1, align=al, fill=fill)
        self.ln()

def generate_report():
    pdf = EDAPDFReport()
    
    # -------------------------------------------------------------
    # HALAMAN 1: COVER & IDENTITAS
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.ln(10)
    
    # Header Banner
    pdf.set_fill_color(24, 43, 73)
    pdf.rect(18, 20, 174, 32, 'F')
    
    pdf.set_xy(18, 24)
    pdf.set_font("Helvetica", "B", 15)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(174, 8, "LAPORAN ANALISIS DATA EKSPLORATIF (EDA)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_text_color(220, 230, 242)
    pdf.cell(174, 6, "Karakteristik & Dinamika Kemacetan Lalu Lintas Tiga Kota Metropolitan", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(174, 5, "(Studi Komparatif: DKI Jakarta, Kota Bandung, dan Kota Semarang)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(12)
    
    # Metadata Box
    pdf.set_fill_color(247, 249, 252)
    pdf.set_draw_color(200, 215, 230)
    pdf.rect(18, pdf.get_y(), 174, 38, 'DF')
    pdf.set_xy(22, pdf.get_y() + 3)
    
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Mata Kuliah", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": Data Sains (Tugas 1 - Minggu ke-3)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Topik Analisis", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": Transportation (Sistem Transportasi Perkotaan)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Skala Dataset", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": 264.9 Juta Observasi Mentah (125,054 Record Segmen Jalan)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Sumber Data", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": HERE Traffic API & OSMnx (Zenodo Open Data Repository)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Anggota Kelompok", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": [Nama Mahasiswa 1 / NIM], [Nama Mahasiswa 2 / NIM], [dst.]", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.set_x(22)
    pdf.set_font("Helvetica", "B", 9.5)
    pdf.set_text_color(24, 43, 73)
    pdf.cell(38, 5, "Tenggat Waktu", 0, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 5, ": Selasa, 17 Maret 2025, 23:59 WIB", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(8)
    
    # Ringkasan Eksekutif
    pdf.chapter_title("1", "RINGKASAN EKSEKUTIF")
    pdf.body_text(
        "Laporan ini menyajikan Analisis Data Eksploratif (Exploratory Data Analysis - EDA) secara komprehensif "
        "terhadap data kemacetan lalu lintas perkotaan di tiga wilayah metropolitan terbesar di Pulau Jawa: "
        "DKI Jakarta, Kota Bandung, dan Kota Semarang. Menggunakan dataset berskala masif yang mengagregasi 264.9 "
        "juta observasi sensor HERE Traffic API selama 11 bulan (Maret 2025 - Februari 2026), analisis ini mengkaji pola "
        "kecepatan kendaraan aktual, indeks kemacetan (Jam Factor: skala 0-10), fluktuasi siklus 24 jam (8 periode waktu), "
        "serta autokorelasi spasial jaringan jalan (OpenStreetMap)."
    )
    pdf.body_text(
        "Temuan utama menunjukkan bahwa kemacetan di seluruh kota mencapai puncaknya pada jam sibuk sore "
        "(Evening Peak: 16:00-19:00), dengan rata-rata kecepatan kendaraan merosot drastis hingga 17.6 km/jam di Jakarta "
        "dan Bandung (penurunan lebih dari 36% dari batas kecepatan ideal). Secara spasial, kemacetan tidak menyebar merata "
        "melainkan membentuk klaster teraglomerasi yang signifikan (Moran's I > 0.29, p < 0.001)."
    )
    
    pdf.ln(2)
    pdf.chapter_title("2", "DESKRIPSI & STRUKTUR DATASET")
    pdf.body_text(
        "Dataset disimpan dalam format GeoPackage (.gpkg) berbasis standar OGC SQLite dengan sistem koordinat WGS 84 "
        "(EPSG:4326). Total terdapat 24 berkas spasial yang merepresentasikan kombinasi 3 kota dan 8 rentang waktu per hari."
    )
    
    # Table of Dataset Scope
    widths = [35, 25, 30, 40, 44]
    headers = ["Kota", "Kode", "Segmen Jalan", "Observasi Sensor", "Karakteristik Wilayah"]
    pdf.table_header(widths, headers)
    pdf.table_row(widths, ["DKI Jakarta", "jkt", "14,549", "206.3 Juta (77.9%)", "Megapolitan Primer"], fill=False, align_list=["L","C","C","C","L"])
    pdf.table_row(widths, ["Kota Bandung", "bdg", "3,069", "43.4 Juta (16.4%)", "Cekungan Vulkanik & Radial"], fill=True, align_list=["L","C","C","C","L"])
    pdf.table_row(widths, ["Kota Semarang", "smg", "1,076", "15.2 Juta (5.7%)", "Pesisir & Perbukitan"], fill=False, align_list=["L","C","C","C","L"])
    pdf.table_row(widths, ["Total / Agregat", "3 Kota", "18,694", "264.9 Juta Observasi", "125,054 Record Waktu"], fill=True, align_list=["L","C","C","C","L"])
    
    # -------------------------------------------------------------
    # HALAMAN 2: ATRIBUT DATA & ANALISIS UNIVARIAT
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.section_title("2.1 Variabel & Pemeriksaan Kualitas Data (Data Quality Check)")
    pdf.body_text(
        "Pemeriksaan data menyeluruh menunjukkan tingkat kelengkapan data 100% (zero missing values). "
        "Setiap segmen jalan memiliki atribut kuantitatif utama: jam_factor_mean (indeks kemacetan rerata), "
        "jam_factor_std (stabilitas/variabilitas kemacetan), speed_mean (kecepatan aktual dalam m/s), dan free_flow_mean "
        "(kecepatan bebas hambatan)."
    )
    
    # Skala Jam Factor
    widths_scale = [32, 38, 104]
    headers_scale = ["Rentang Nilai", "Klasifikasi Kondisi", "Interpretasi Operasional Lalu Lintas"]
    pdf.table_header(widths_scale, headers_scale)
    pdf.table_row(widths_scale, ["0.0 - 1.0", "Free Flow (Lancar)", "Kecepatan maksimal mendekati batas desain jalan"], fill=False)
    pdf.table_row(widths_scale, ["1.0 - 3.0", "Light Traffic (Ringan)", "Lalu lintas bergerak lancar, interaksi kendaraan minim"], fill=True)
    pdf.table_row(widths_scale, ["3.0 - 6.0", "Moderate (Sedang)", "Mulai terjadi perlambatan berkala akibat kepadatan volume"], fill=False)
    pdf.table_row(widths_scale, ["6.0 - 8.0", "Heavy Traffic (Padat)", "Antrean panjang kendaraan, pengereman berulang kali"], fill=True)
    pdf.table_row(widths_scale, ["8.0 - 10.0", "Severe (Macet Total)", "Kondisi gridlock/lumpuh dengan kecepatan mendekati nol"], fill=False)
    
    pdf.ln(3)
    pdf.chapter_title("3", "ANALISIS UNIVARIAT: SEBARAN KEMACETAN & KECEPATAN")
    pdf.body_text(
        "Analisis univariat dilakukan untuk mengkaji tendensi sentral, dispersi, dan bentuk sebaran data. "
        "Secara global, nilai rata-rata jam_factor_mean adalah 2.57 dengan median 1.45 dan deviasi standar 2.77. "
        "Nilai skewness positif sebesar 1.195 menandakan kurva distribusi miring ke kanan (right-skewed). Hal ini "
        "mengindikasikan bahwa sebagian besar jalan berada pada kondisi bebas hambatan, namun terdapat ekor panjang "
        "(long-tail) segmen jalan yang mengalami kemacetan parah di atas skala 6.0."
    )
    
    # Chart 1: Distribution
    chart1_path = "eda_charts/1_distribution_peak_vs_night.png"
    if os.path.exists(chart1_path):
        pdf.image(chart1_path, x=18, y=pdf.get_y(), w=174)
        pdf.set_y(pdf.get_y() + 66)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 1: Perbandingan Fungsi Kepadatan Probabilitas (KDE) Jam Factor saat Jam Sibuk vs Dini Hari", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    pdf.body_text(
        "Pada Gambar 1, terlihat kontras tajam antara jam sibuk sore dan dini hari. Pada malam hari (00:00-06:00), "
        "distribusi probabilitas seluruh kota terkonsentrasi mendekati nilai 0 (lancar sempurna). Sebaliknya, pada sore hari, "
        "kurva merata ke kanan dengan lonjakan drastis pada rentang jam factor 3 hingga 9, terutama di Jakarta dan Bandung."
    )
    
    # -------------------------------------------------------------
    # HALAMAN 3: SIKLUS TEMPORAL 24 JAM
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("4", "ANALISIS TEMPORAL SIKLUS 24 JAM (8 PERIODE WAKTU)")
    pdf.body_text(
        "Untuk memahami ritme pergerakan mobilitas perkotaan, data dibagi ke dalam 8 periode waktu harian. "
        "Uji statistik ANOVA menunjukkan pengaruh periode waktu terhadap indeks kemacetan bersifat sangat signifikan "
        "(Jakarta: F = 740.10, p < 1e-300; Bandung: F = 221.10, p < 1e-300; Semarang: F = 66.42, p < 1e-92)."
    )
    
    # Chart 2: Temporal Profile
    chart2_path = "eda_charts/2_temporal_congestion_profile.png"
    if os.path.exists(chart2_path):
        pdf.image(chart2_path, x=20, y=pdf.get_y(), w=170)
        pdf.set_y(pdf.get_y() + 84)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 2: Fluktuasi Jam Factor Rata-rata Berdasarkan 8 Periode Waktu Harian", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    pdf.body_text(
        "Profil temporal menunjukkan fenomena menarik di mana jam sibuk pagi (Morning Peak, 06:00-09:00) "
        "justru memiliki indeks kemacetan yang lebih rendah (Jakarta: 2.42, Bandung: 2.21, Semarang: 1.93) dibandingkan "
        "jam sibuk sore (Evening Peak: Jakarta: 3.43, Bandung: 3.22, Semarang: 2.74). Hal ini disebabkan oleh arus perjalanan "
        "sore hari yang bercampur antara kepulangan pekerja kantoran, aktivitas logistik, komersial kuliner, dan perjalanan informal."
    )
    
    # Tabel Ringkasan Temporal
    pdf.section_title("Tabel 1: Nilai Rata-rata Jam Factor dan Kecepatan Aktual Antar Periode Waktu")
    w_t = [38, 28, 28, 28, 28, 24]
    h_t = ["Periode Waktu", "Jam (WIB)", "Jakarta (JF)", "Bandung (JF)", "Semarang (JF)", "Rata-rata Speed"]
    pdf.table_header(w_t, h_t)
    temporal_rows = [
        ["Night", "00:00 - 06:00", "1.31", "0.91", "0.92", "27.56 km/jam"],
        ["Morning Peak", "06:00 - 09:00", "2.42", "2.21", "1.93", "22.97 km/jam"],
        ["Morning Offpeak", "09:00 - 12:00", "2.91", "2.75", "2.43", "20.78 km/jam"],
        ["Lunch Hours", "12:00 - 14:00", "2.86", "2.78", "2.39", "20.76 km/jam"],
        ["Afternoon Offpeak", "14:00 - 16:00", "3.00", "2.97", "2.53", "20.28 km/jam"],
        ["Evening Peak", "16:00 - 19:00", "3.43", "3.22", "2.74", "19.49 km/jam"],
        ["Evening Offpeak", "19:00 - 22:00", "2.99", "2.40", "2.21", "21.33 km/jam"],
        ["Late Night", "22:00 - 00:00", "1.97", "1.38", "1.24", "25.10 km/jam"]
    ]
    for i, row in enumerate(temporal_rows):
        pdf.table_row(w_t, row, fill=(i%2==1), align_list=["L","C","C","C","C","C"])

    # -------------------------------------------------------------
    # HALAMAN 4: ANALISIS KECEPATAN & TINGKAT KEPARAHAN
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("5", "ANALISIS BIVARIAT: HUBUNGAN KECEPATAN & KEMACETAN")
    pdf.body_text(
        "Korelasi linier Pearson antara jam factor dan kecepatan kendaraan bernilai r = -0.466, sedangkan koefisien Spearman "
        "bernilai rho = -0.295. Hubungan ini bersifat non-linier: penurunan kecepatan sangat cepat terjadi pada transisi jam factor 0 ke 4, "
        "kemudian melandai ketika kemacetan telah mengunci kecepatan kendaraan pada level batas bawah (gridlock plateau)."
    )
    
    # Chart 3: Speed vs Free-flow
    chart3_path = "eda_charts/3_speed_vs_freeflow.png"
    if os.path.exists(chart3_path):
        pdf.image(chart3_path, x=18, y=pdf.get_y(), w=174)
        pdf.set_y(pdf.get_y() + 64)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 3: Perbandingan Kecepatan Aktual vs Batas Bebas Hambatan (Free-Flow) per Kota", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # Chart 4: Severity Proportion
    chart4_path = "eda_charts/4_congestion_severity_proportion.png"
    if os.path.exists(chart4_path):
        pdf.image(chart4_path, x=22, y=pdf.get_y(), w=166)
        pdf.set_y(pdf.get_y() + 82)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 4: Proporsi Tingkat Keparahan Segmen Jalan pada Jam Sibuk Sore (Evening Peak)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    pdf.body_text(
        "Berdasarkan Gambar 4, pada jam sibuk sore di Jakarta, lebih dari 45% segmen jalan mengalami kemacetan kategori sedang "
        "hingga parah (Moderate 24.1%, Heavy 12.5%, Severe 8.8%). Kota Bandung memiliki proporsi kemacetan parah yang mirip "
        "karena keterbatasan kapasitas jaringan jalan kota tua dan tingginya aktivitas komersial."
    )
    
    # -------------------------------------------------------------
    # HALAMAN 5: KOMPARASI KOTA & AUTOKORELASI SPASIAL
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("6", "ANALISIS SPASIAL & KOMPARATIF TIGA KOTA")
    pdf.body_text(
        "Secara geografis dan morfologi perkotaan, ketiga kota menunjukkan dinamika yang berbeda nyata:"
    )
    pdf.body_text(
        "1. DKI Jakarta: Memiliki skala jaringan jalan terbesar (14,549 segmen) dengan rata-rata jam factor tertinggi (2.64) "
        "dan kecepatan rata-rata terendah (18.9 km/jam). Kemacetan terkonsentrasi di koridor arteri primer, jalan lingkar dalam (Inner Ring Road), "
        "dan simpul perbatasan komuter Bodetabek."
    )
    pdf.body_text(
        "2. Kota Bandung: Berada pada topografi cekungan dataran tinggi vulkanik dengan pola jaringan jalan radial konsentris. "
        "Meskipun segmen jalannya hanya 3,069, tingkat keparahan saat jam sibuk hampir menyamai Jakarta (Jam Factor 3.22 vs 3.43) "
        "karena minimnya jalur alternatif dan bottleneck di perlintasan sebidang serta kawasan wisata kuliner/belanja."
    )
    pdf.body_text(
        "3. Kota Semarang: Menunjukkan kinerja lalu lintas paling lancar dengan rata-rata kecepatan 25.6 km/jam (kecepatan free-flow 32.4 km/jam) "
        "dan jam factor 2.07. Kemacetan hanya terisolasi di koridor pesisir Pantura (Kaligawe) dan jalur tanjakan Semarang Atas (Gombel)."
    )
    
    pdf.section_title("Uji Autokorelasi Spasial (Moran's I)")
    pdf.body_text(
        "Uji statistik spasial Global Moran's I membuktikan adanya pengelompokan spasial (spatial clustering) yang sangat signifikan. "
        "Segmen jalan yang macet dikelilingi oleh jalan-jalan yang juga macet (High-High Spatial Clusters):"
    )
    
    # Table Morans I
    w_m = [35, 35, 35, 35, 34]
    h_m = ["Kota", "Global Moran's I", "Z-Score", "P-Value", "Interpretasi Spasial"]
    pdf.table_header(w_m, h_m)
    pdf.table_row(w_m, ["DKI Jakarta", "0.3101", "+75.59", "< 0.0001", "Klaster Padat Sangat Kuat"], fill=False, align_list=["L","C","C","C","L"])
    pdf.table_row(w_m, ["Kota Bandung", "0.2910", "+31.68", "< 0.0001", "Klaster Padat Kuat"], fill=True, align_list=["L","C","C","C","L"])
    pdf.table_row(w_m, ["Kota Semarang", "0.2984", "+19.50", "< 0.0001", "Klaster Padat Signifikan"], fill=False, align_list=["L","C","C","C","L"])
    
    # Chart 6: Boxplot Jakarta
    chart6_path = "eda_charts/6_jkt_period_boxplot.png"
    if os.path.exists(chart6_path):
        pdf.image(chart6_path, x=18, y=pdf.get_y() + 2, w=174)
        pdf.set_y(pdf.get_y() + 72)
        pdf.set_font("Helvetica", "I", 8)
        pdf.cell(0, 4, "Gambar 5: Boxplot Sebaran Indeks Kemacetan Jakarta Menunjukkan Variabilitas dan Pencilan (Outlier)", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # -------------------------------------------------------------
    # HALAMAN 6: KESIMPULAN & REKOMENDASI DATA SAINS
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.chapter_title("7", "KESIMPULAN & REKOMENDASI DATA SAINS")
    pdf.body_text(
        "Berdasarkan serangkaian proses Exploratory Data Analysis (EDA) terhadap 264.9 juta observasi lalu lintas, dapat ditarik kesimpulan:"
    )
    pdf.body_text(
        "- Asimetri Puncak Kemacetan: Kemacetan sore (Evening Peak) secara konsisten jauh lebih parah daripada pagi (Morning Peak) "
        "di ketiga kota, dengan penurunan kecepatan mencapai 36.3% dibandingkan kondisi bebas hambatan."
    )
    pdf.body_text(
        "- Heterogenitas Antar Kota: Jakarta dan Bandung memiliki tingkat keparahan kemacetan yang sebanding pada jam puncak, "
        "meskipun Jakarta memiliki jaringan jalan 4.7 kali lebih banyak. Semarang mempertahankan kecepatan rata-rata tertinggi (25.6 km/jam)."
    )
    pdf.body_text(
        "- Dependensi Spasial yang Kuat: Nilai Moran's I positif (~0.30, p < 0.001) menegaskan bahwa fenomena kemacetan bersifat menular "
        "(spillover effect) antar ruas jalan yang bertetangga, bukan peristiwa acak/acak murni."
    )
    
    pdf.section_title("Rekomendasi untuk Tahap Pemodelan Data Sains Berikutnya:")
    pdf.body_text(
        "1. Spatial Feature Engineering: Perlu memasukkan fitur lag spasial (spatial lag variable) atau representasi graf jalan "
        "(Graph Convolutional Networks - GCN) dalam memprediksi kemacetan, karena fitur non-spasial saja akan bias."
    )
    pdf.body_text(
        "2. Segmentasi Waktu Khusus: Model prediksi Machine Learning (seperti XGBoost, LightGBM, atau LSTM) harus dilatih dengan "
        "bobot waktu interaktif atau model terpisah untuk jam puncak (peak) vs luar jam puncak (off-peak)."
    )
    pdf.body_text(
        "3. Kebijakan Manajemen Rekayasa Lalu Lintas: Rekayasa lalu lintas dinamis (seperti pengaturan durasi lampu lalu lintas adaptif, "
        "manajemen jalur contraflow, dan integrasi angkutan umum massal) harus difokuskan pada koridor dengan High-High cluster pada rentang 16:00-19:00 WIB."
    )
    
    pdf.ln(4)
    pdf.chapter_title("8", "DAFTAR PUSTAKA & REFERENSI DATASET")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(50, 50, 50)
    ref1 = (
        "1. Hadi, F., Wahyuddin, Y., Sabri, L. M., & Indrajit, A. (2026). An Open-Source Pipeline for Spatiotemporal Traffic Congestion "
        "Analysis: Integrating HERE API, OSMnx, and PySAL Across Indonesian Metropolitan Cities. Computers, Environment and Urban Systems."
    )
    ref2 = (
        "2. HERE Technologies. (2025). HERE Traffic API v7 Documentation. Available at: https://developer.here.com/documentation/traffic-api/"
    )
    ref3 = (
        "3. Boeing, G. (2017). OSMnx: New methods for acquiring, constructing, analyzing, and visualizing complex street networks. "
        "Computers, Environment and Urban Systems, 65, 126-139."
    )
    ref4 = (
        "4. Anselin, L. (1995). Local Indicators of Spatial Association-LISA. Geographical Analysis, 27(2), 93-115."
    )
    pdf.multi_cell(0, 4.5, ref1)
    pdf.ln(1)
    pdf.multi_cell(0, 4.5, ref2)
    pdf.ln(1)
    pdf.multi_cell(0, 4.5, ref3)
    pdf.ln(1)
    pdf.multi_cell(0, 4.5, ref4)
    
    output_pdf_path = "Laporan_Tugas1_Data_Sains_EDA_Transportasi.pdf"
    pdf.output(output_pdf_path)
    print(f"Report successfully saved to {output_pdf_path}")

if __name__ == "__main__":
    generate_report()
