import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

class CompactEDAReport(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(20, 18, 20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 6, "Laporan Tugas 1 Data Sains - Analisis Sederhana Kecelakaan Lalu Lintas", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_draw_color(220, 220, 220)
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(3)

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-14)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, f"{self.page_no()}", align="C")


def generate_compact_report():
    pdf = CompactEDAReport()
    
    # -------------------------------------------------------------
    # HALAMAN 1: COVER STANDAR TELKOM UNIVERSITY
    # -------------------------------------------------------------
    pdf.add_page()
    pdf.ln(30)
    
    # Judul Tugas
    pdf.set_font("Helvetica", "B", 15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "TUGAS 1 DATA SAINS", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 12.5)
    pdf.cell(0, 6.5, "ANALISIS DATA EKSPLORATIF POLA DAN FAKTOR KEPARAHAN", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 6.5, "KECELAKAAN LALU LINTAS DI BRITANIA RAYA", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(55)
    
    # Identitas Anggota
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 6, "Nama Anggota:", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 5.5, "[Nama Mahasiswa 1]  [NIM 1]", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5.5, "[Nama Mahasiswa 2]  [NIM 2]", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5.5, "[Nama Mahasiswa 3]  [NIM 3]", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.ln(60)
    
    # Lembaga / Kampus
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 5.5, "PROGRAM STUDI S1 TEKNIK KOMPUTER", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5.5, "FAKULTAS TEKNIK ELEKTRO", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5.5, "TELKOM UNIVERSITY", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5.5, "2026/2027", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    # -------------------------------------------------------------
    # HALAMAN 2: DESKRIPSI DATASET & SUB-BAB 1
    # -------------------------------------------------------------
    pdf.add_page()
    
    # 1. Deskripsi Dataset
    pdf.set_font("Helvetica", "B", 11.5)
    pdf.cell(0, 6, "1. Deskripsi Dataset", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 5, "Link Dataset: UK Road Safety Open Dataset 2025 (Department for Transport / GOV.UK)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    desc_text = (
        "Dataset ini berisi catatan resmi kecelakaan lalu lintas di seluruh wilayah Britania Raya (Inggris) sepanjang tahun 2025 "
        "yang dihimpun langsung oleh pihak kepolisian. Data ini mencatat sebanyak 101.525 kejadian kecelakaan dengan 44 informasi penting, "
        "seperti jam kejadian, hari, batas kecepatan ruas jalan, kondisi cuaca, permukaan aspal, berapa kendaraan yang terlibat, hingga "
        "seberapa parah korban yang terluka. Tujuan dari analisis data eksploratif (EDA) ini adalah untuk menjawab pertanyaan-pertanyaan "
        "sederhana sehari-hari: jam berapa jalanan paling berbahaya, hari apa yang paling rawan tabrakan, seberapa bahaya mengebut di jalan, "
        "dan faktor apa saja yang paling sering membuat pengendara celaka."
    )
    pdf.multi_cell(0, 4.8, desc_text)
    pdf.ln(2.5)
    
    # 2. Hasil EDA
    pdf.set_font("Helvetica", "B", 11.5)
    pdf.cell(0, 6, "2. Hasil Analisis Data Eksploratif (EDA)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    # a. Distribusi Keparahan
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "a. Seberapa Parah Akibat dari Kecelakaan yang Terjadi?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart1_path = "eda_output/1_distribusi_keparahan.png"
    if os.path.exists(chart1_path):
        pdf.image(chart1_path, x=26, y=pdf.get_y(), w=142)
        pdf.set_y(pdf.get_y() + 90)
        pdf.ln(1.5)
        
    p1 = (
        "Grafik di atas memperlihatkan seberapa parah akibat dari 101.525 tabrakan yang tercatat di jalan raya. "
        "Sebagian besar, yaitu 74.881 kejadian (73,8%), adalah kecelakaan luka ringan (seperti lecet atau memar yang tidak perlu rawat inap). "
        "Sekitar 25.191 kejadian (24,8%) termasuk luka berat (seperti patah tulang yang harus dirawat di rumah sakit), dan sebanyak 1.453 kejadian "
        "(1,4%) merupakan kecelakaan fatal yang merenggut nyawa korban. Kabar baiknya adalah mayoritas kecelakaan dampaknya masih bisa "
        "diminimalisir, namun angka korban meninggal dan luka berat tetap menunjukkan bahwa risiko fatal di jalan raya sangat nyata."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p1)
    
    # -------------------------------------------------------------
    # HALAMAN 3: POLA JAM & HARI
    # -------------------------------------------------------------
    pdf.add_page()
    
    # b. Pola Jam Kejadian
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "b. Jam Berapa Kecelakaan Paling Sering Terjadi dalam Sehari?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart2_path = "eda_output/2_tren_jam_kejadian.png"
    if os.path.exists(chart2_path):
        pdf.image(chart2_path, x=24, y=pdf.get_y(), w=146)
        pdf.set_y(pdf.get_y() + 64)
        pdf.ln(1.5)
        
    p2 = (
        "Grafik garis di atas menunjukkan tren kecelakaan selama 24 jam penuh. Polanya sangat jelas mengikuti jam kesibukan warga "
        "dan memiliki dua waktu puncak: 1) Puncak Pagi (pukul 08:00) dengan 6.716 kejadian saat jam berangkat kerja dan sekolah; serta "
        "2) Puncak Sore (pukul 17:00) yang merupakan waktu paling berbahaya dalam sehari dengan 8.877 kejadian saat jam pulang kerja. "
        "Kecelakaan sore hari jauh lebih banyak karena kondisi fisik dan pikiran pengemudi sudah lelah setelah seharian beraktivitas, ditambah "
        "jalan yang mulai gelap. Waktu paling aman dengan kecelakaan paling sedikit adalah tengah malam hingga subuh (01:00-05:00)."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p2)
    pdf.ln(3)
    
    # c. Pola Hari
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "c. Hari Apa yang Paling Sering Terjadi Kecelakaan?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart3_path = "eda_output/3_distribusi_hari.png"
    if os.path.exists(chart3_path):
        pdf.image(chart3_path, x=26, y=pdf.get_y(), w=142)
        pdf.set_y(pdf.get_y() + 80)
        pdf.ln(1.5)
        
    p3 = (
        "Grafik batang di atas membandingkan seberapa sering kecelakaan terjadi di setiap hari dalam seminggu. "
        "Hari Jumat adalah hari yang paling rawan celaka, dengan angka tertinggi mencapai 16.811 kejadian (16,6%). Hal ini terjadi karena "
        "hari Jumat adalah akhir pekan kerja di mana jalanan sangat padat oleh orang pulang kantor, bepergian luar kota, dan bepergian malam. "
        "Hari Minggu justru menjadi hari paling aman dengan angka kejadian paling sedikit (11.197 kejadian) karena jalanan relatif lengang."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p3)
    
    # -------------------------------------------------------------
    # HALAMAN 4: SPEED LIMIT & CUACA
    # -------------------------------------------------------------
    pdf.add_page()
    
    # d. Speed limit vs Severity
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "d. Seberapa Bahaya Mengebut? (Batas Kecepatan vs Kematian)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart4_path = "eda_output/4_speed_limit_vs_severity.png"
    if os.path.exists(chart4_path):
        pdf.image(chart4_path, x=26, y=pdf.get_y(), w=142)
        pdf.set_y(pdf.get_y() + 80)
        pdf.ln(1.5)
        
    p4 = (
        "Grafik di atas membuktikan fakta nyata bahwa semakin kencang laju kendaraan, semakin mematikan dampaknya saat terjadi tabrakan. "
        "Di jalanan perumahan atau dekat sekolah dengan batas kecepatan rendah 20 mph (sekitar 32 km/jam), persentase korban meninggal sangat kecil, "
        "yaitu hanya 0,51% (hampir semua orang selamat). Namun, di jalan raya antarkota dengan batas kecepatan 60 mph (sekitar 96 km/jam), "
        "persentase korban meninggal melonjak drastis hingga 3,70% (naik lebih dari 7 kali lipat). Hal ini terjadi karena mobil yang melaju kencang "
        "menghasilkan benturan dahsyat yang menghancurkan bodi mobil dan sangat berbahaya bagi keselamatan manusia di dalamnya."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p4)
    pdf.ln(3)
    
    # e. Cuaca Dominan
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "e. Cuaca Seperti Apa yang Paling Sering Terjadi Kecelakaan?", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart5_path = "eda_output/5_cuaca_dominan.png"
    if os.path.exists(chart5_path):
        pdf.image(chart5_path, x=26, y=pdf.get_y(), w=142)
        pdf.set_y(pdf.get_y() + 73)
        pdf.ln(1.5)
        
    p5 = (
        "Banyak orang menduga kecelakaan paling sering terjadi saat hujan lebat atau badai. Namun, data grafik di atas justru menunjukkan hal sebaliknya: "
        "sebanyak 83.405 kejadian (82,1%) kecelakaan justru terjadi pada saat cuaca Cerah dan jalanan kering. Kecelakaan saat hujan hanya sekitar 10,1%. "
        "Penyebabnya adalah perilaku pengemudi: saat cuaca buruk dan jalanan licin, pengemudi secara sadar lebih takut sehingga mengemudi pelan-pelan "
        "dan menjaga jarak. Sebaliknya saat cuaca cerah dan jalanan kering, pengemudi merasa sangat aman sehingga berani mengebut dan kurang waspada."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p5)
    
    # -------------------------------------------------------------
    # HALAMAN 5: OUTLIER & KESIMPULAN RINGKAS
    # -------------------------------------------------------------
    pdf.add_page()
    
    # f. Outlier
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5, "f. Kasus Luar Biasa: Tabrakan Paling Ekstrem yang Pernah Terjadi", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    chart6_path = "eda_output/6_outlier_kendaraan_korban.png"
    if os.path.exists(chart6_path):
        pdf.image(chart6_path, x=24, y=pdf.get_y(), w=146)
        pdf.set_y(pdf.get_y() + 64)
        pdf.ln(1.5)
        
    p6 = (
        "Secara umum, kecelakaan di jalan raya biasanya hanya melibatkan 1 atau 2 mobil saja dan korbannya 1 orang. Namun, grafik sebaran di atas "
        "menunjukkan adanya beberapa peristiwa luar biasa yang sangat ekstrem: 1) Tabrakan beruntun karambol di jalan tol yang melibatkan hingga "
        "17 mobil sekaligus dalam satu kejadian; dan 2) Kecelakaan bus penumpang umum dengan korban luka dan terdampak mencapai 142 orang. "
        "Kejadian ekstrem ini mengingatkan kita betapa pentingnya selalu menjaga jarak aman dengan mobil di depan agar tidak saling bertubrukan saat ada rem mendadak."
    )
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(0, 4.8, p6)
    pdf.ln(6)
    
    # 3. Kesimpulan
    pdf.set_font("Helvetica", "B", 11.5)
    pdf.cell(0, 6, "3. Kesimpulan", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    
    conclusions = [
        "1. Waspada di Jam Pulang Kantor: Waktu paling rawan tabrakan adalah jam 5 sore dan di hari Jumat. Di waktu inilah jalanan paling padat dan pengendara umumnya sudah lelah setelah seharian bekerja.",
        "2. Batas Kecepatan Menyelamatkan Nyawa: Mematuhi batas kecepatan 20-30 mph terbukti sangat efektif menekan angka kematian hingga di bawah 1%, dibanding memacu kendaraan di atas 60 mph yang risiko kematiannya melonjak 7 kali lipat.",
        "3. Jangan Lengah Saat Cuaca Cerah: Sebanyak 8 dari 10 kecelakaan justru terjadi di siang hari yang cerah dan aspal kering. Rasa aman semu sering membuat orang kurang waspada dan tergoda untuk mengebut.",
        "4. Selalu Jaga Jarak Aman: Tabrakan beruntun bisa melibatkan belasan mobil sekaligus. Memberi jarak yang cukup memberi ruang rem darurat yang aman bagi semua pengendara."
    ]
    
    pdf.set_font("Helvetica", "", 9.5)
    for c in conclusions:
        pdf.multi_cell(0, 4.6, c)
        pdf.ln(1)
        
    output_pdf = "Laporan_Tugas1_Data_Sains_Ringkas_UK.pdf"
    pdf.output(output_pdf)
    print(f"Compact PDF with simple language generated: {output_pdf}")


if __name__ == "__main__":
    generate_compact_report()
