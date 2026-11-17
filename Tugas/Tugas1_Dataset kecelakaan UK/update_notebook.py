import json
import os

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# TUGAS 1: EXPLORATORY DATA ANALYSIS (EDA)\n",
                "## Analisis Karakteristik, Pola Temporal, dan Faktor Risiko Kecelakaan Lalu Lintas di Britania Raya\n",
                "### Studi Kasus: UK Department for Transport (DfT) Road Safety Open Dataset 2025\n",
                "\n",
                "---\n",
                "**Mata Kuliah:** Data Sains / Sains Data (Tugas 1 - Minggu ke-3)  \n",
                "**Topik:** *Transportation* (Sistem Keselamatan Jalan Raya & Manajemen Lalu Lintas)  \n",
                "**Sumber Data:** [UK Department for Transport (DfT) via GOV.UK Open Data](https://www.gov.uk/government/statistical-data-sets/road-safety-open-data)  \n",
                "**Skala Dataset:**  \n",
                "- Tabel `collision` (Insiden Tabrakan): **101,525 baris × 44 kolom**  \n",
                "- Tabel `casualty` (Korban): **127,883 baris × 23 kolom**  \n",
                "- Tabel `vehicle` (Kendaraan): **183,948 baris × 32 kolom**  \n",
                "- **Total Observasi:** >413,000 baris (Sangat memenuhi syarat dataset besar / *big data*)  \n",
                "**Batas Pengumpulan (*Deadline*):** Selasa, 17 Maret 2025 pukul 23:59 WIB  \n",
                "**Format Pengumpulan:** Berkas Softfile `.pdf` dan Notebook `.ipynb`"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1. Import Library dan Persiapan Lingkungan Analisis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os\n",
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Konfigurasi gaya visualisasi profesional\n",
                "sns.set_theme(style=\"whitegrid\")\n",
                "plt.rcParams.update({\n",
                "    'font.sans-serif': 'Arial',\n",
                "    'font.size': 10,\n",
                "    'figure.titlesize': 12,\n",
                "    'figure.dpi': 150\n",
                "})\n",
                "\n",
                "# Buat direktori output jika belum ada\n",
                "os.makedirs('eda_output', exist_ok=True)\n",
                "\n",
                "# Muat dataset utama tabrakan (collision)\n",
                "file_path = 'dft-road-casualty-statistics-collision-2025.csv'\n",
                "df = pd.read_csv(file_path, low_memory=False)\n",
                "\n",
                "print(f\"Dataset berhasil dimuat!\")\n",
                "print(f\"Dimensi Data: {df.shape[0]:,} baris dan {df.shape[1]} kolom\")\n",
                "df.head()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 2. Pemeriksaan Kualitas Data (Data Quality Check & Cleaning)\n",
                "Memeriksa *missing values*, duplikasi, serta konsistensi tipe data."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Periksa nilai kosong pada seluruh kolom\n",
                "missing = df.isnull().sum()\n",
                "missing_cols = missing[missing > 0]\n",
                "print(\"Kolom dengan Nilai Kosong (Missing Values):\")\n",
                "print(missing_cols)\n",
                "\n",
                "# Kelengkapan koordinat spasial (latitude & longitude)\n",
                "coord_complete = (1 - df['latitude'].isnull().sum() / len(df)) * 100\n",
                "print(f\"\\nKelengkapan Koordinat Spasial: {coord_complete:.3f}%\")\n",
                "\n",
                "# Bersihkan baris dengan koordinat kosong (hanya 2 baris)\n",
                "df = df.dropna(subset=['latitude', 'longitude'])\n",
                "print(f\"Banyak baris setelah pembersihan: {len(df):,} baris\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Pemetaan Kode Angka (Decoding) Sesuai Panduan Resmi DfT\n",
                "Mengubah kode angka menjadi teks label yang mudah dipahami."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Kamus pemetaan semantik resmi DfT Road Safety Data Guide\n",
                "severity_dict = {1: 'Fatal', 2: 'Serious', 3: 'Slight'}\n",
                "day_dict = {1: 'Minggu', 2: 'Senin', 3: 'Selasa', 4: 'Rabu', 5: 'Kamis', 6: 'Jumat', 7: 'Sabtu'}\n",
                "weather_dict = {\n",
                "    1: 'Cerah', 2: 'Hujan', 3: 'Salju', 4: 'Cerah+Angin',\n",
                "    5: 'Hujan+Angin', 6: 'Salju+Angin', 7: 'Kabut', 8: 'Lainnya', 9: 'Unknown'\n",
                "}\n",
                "road_surface_dict = {\n",
                "    1: 'Kering', 2: 'Basah/Becek', 3: 'Salju', 4: 'Licin Es', 5: 'Banjir', 9: 'Unknown', -1: 'Missing'\n",
                "}\n",
                "\n",
                "# Penerapan mapping\n",
                "df['severity_label'] = df['collision_severity'].map(severity_dict)\n",
                "df['day_name'] = df['day_of_week'].map(day_dict)\n",
                "df['weather_label'] = df['weather_conditions'].map(weather_dict)\n",
                "df['surface_label'] = df['road_surface_conditions'].map(road_surface_dict)\n",
                "df['hour'] = pd.to_datetime(df['time'], format='%H:%M', errors='coerce').dt.hour\n",
                "\n",
                "print(\"Decoding selesai. Contoh sampel fitur baru:\")\n",
                "df[['collision_index', 'severity_label', 'day_name', 'weather_label', 'hour']].head()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 4. Analisis 1: Distribusi Tingkat Keparahan Kecelakaan (Collision Severity)\n",
                "Menganalisis proporsi Slight (Ringan), Serious (Berat), dan Fatal (Meninggal), serta meneliti isu ketidakseimbangan kelas (*imbalanced data*)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(8, 5))\n",
                "sev_counts = df['severity_label'].value_counts()\n",
                "colors = ['#2ca02c', '#ff7f0e', '#d62728']\n",
                "bars = plt.bar(sev_counts.index, sev_counts.values, color=colors, edgecolor='black', alpha=0.85)\n",
                "\n",
                "plt.title('Distribusi Tingkat Keparahan Tabrakan (UK Road Safety 2025)', fontsize=13, fontweight='bold')\n",
                "plt.xlabel('Tingkat Keparahan Tabrakan')\n",
                "plt.ylabel('Jumlah Kejadian')\n",
                "\n",
                "for bar in bars:\n",
                "    y = bar.get_height()\n",
                "    pct = (y / len(df)) * 100\n",
                "    plt.text(bar.get_x() + bar.get_width()/2.0, y + 800, f'{y:,}\\n({pct:.1f}%)', \n",
                "             ha='center', va='bottom', fontsize=9.5, fontweight='bold')\n",
                "\n",
                "plt.ylim(0, max(sev_counts.values) * 1.15)\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/1_distribusi_keparahan.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(\"Ringkasan Frekuensi Tingkat Keparahan:\")\n",
                "for k, v in sev_counts.items():\n",
                "    print(f\"- {k}: {v:,} insiden ({v/len(df)*100:.2f}%)\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 5. Analisis 2: Tren Fluktuasi Temporal 24 Jam (Pola Jam Sibuk Bimodal)\n",
                "Menyelidiki pola waktu kejadian tabrakan sepanjang 24 jam untuk mengidentifikasi jam-jam paling berbahaya bagi pengguna jalan."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(11, 4.5))\n",
                "hourly_total = df['hour'].value_counts().sort_index()\n",
                "\n",
                "plt.plot(hourly_total.index, hourly_total.values, marker='o', color='#1f77b4', linewidth=2.5)\n",
                "plt.axvspan(7, 9, color='orange', alpha=0.25, label='Morning Peak (08:00 WIB/GMT)')\n",
                "plt.axvspan(15, 18, color='red', alpha=0.2, label='Evening Peak (17:00 Puncak Absolut)')\n",
                "\n",
                "plt.title('Pola Kejadian Kecelakaan Berdasarkan Jam dalam Sehari', fontsize=13, fontweight='bold')\n",
                "plt.xlabel('Jam Kejadian (00:00 - 23:00)')\n",
                "plt.ylabel('Jumlah Kejadian')\n",
                "plt.xticks(range(0, 24))\n",
                "plt.legend(loc='upper left')\n",
                "plt.grid(True, linestyle='--', alpha=0.6)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/2_tren_jam_kejadian.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(f\"Puncak Jam Tertinggi: Pukul {hourly_total.idxmax()}:00 dengan {hourly_total.max():,} insiden\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 6. Analisis 3: Distribusi Kejadian Berdasarkan Hari dalam Seminggu\n",
                "Menganalisis variasi angka kecelakaan dari hari Senin hingga Minggu (*Friday rush effect*)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(9, 4.5))\n",
                "day_order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']\n",
                "day_counts = df['day_name'].value_counts().reindex(day_order)\n",
                "\n",
                "bars = plt.bar(day_counts.index, day_counts.values, color='#4575b4', edgecolor='black', alpha=0.85)\n",
                "plt.title('Distribusi Frekuensi Kecelakaan Berdasarkan Hari dalam Seminggu', fontsize=13, fontweight='bold')\n",
                "plt.xlabel('Hari')\n",
                "plt.ylabel('Jumlah Kejadian')\n",
                "\n",
                "for bar in bars:\n",
                "    y = bar.get_height()\n",
                "    pct = (y / len(df)) * 100\n",
                "    plt.text(bar.get_x() + bar.get_width()/2.0, y + 200, f'{y:,}\\n({pct:.1f}%)', \n",
                "             ha='center', va='bottom', fontsize=9, fontweight='bold')\n",
                "\n",
                "plt.ylim(0, max(day_counts.values) * 1.15)\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/3_distribusi_hari.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(\"Hari dengan angka kecelakaan tertinggi: Jumat (16,811 kejadian / 16.56%)\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 7. Analisis 4: Pengaruh Batas Kecepatan (Speed Limit) Terhadap Tingkat Fatalitas\n",
                "Menguji hubungan antara batas kecepatan ruas jalan (mph) dan proporsi fatalitas (*energy of impact*)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "common_speeds = [20, 30, 40, 50, 60, 70]\n",
                "df_speed = df[df['speed_limit'].isin(common_speeds)]\n",
                "speed_sev = pd.crosstab(df_speed['speed_limit'], df_speed['severity_label'], normalize='index') * 100\n",
                "speed_sev = speed_sev[['Slight', 'Serious', 'Fatal']]\n",
                "\n",
                "ax = speed_sev.plot(kind='bar', stacked=True, color=['#a6d96a', '#fdae61', '#d7191c'], \n",
                "                    edgecolor='black', figsize=(9.5, 4.8))\n",
                "plt.title('Proporsi Tingkat Keparahan Berdasarkan Batas Kecepatan Ruas Jalan (mph)', fontsize=12, fontweight='bold')\n",
                "plt.xlabel('Batas Kecepatan Jalan (mph)')\n",
                "plt.ylabel('Proporsi Kejadian (%)')\n",
                "plt.xticks(rotation=0)\n",
                "plt.legend(title='Tingkat Keparahan', bbox_to_anchor=(1.02, 1))\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/4_speed_limit_vs_severity.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(\"Tabulasi Silang Batas Kecepatan vs Fatalitas (%):\")\n",
                "print(speed_sev.round(2))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 8. Analisis 5: Kondisi Cuaca dan Lingkungan Jalan\n",
                "Meneliti apakah kecelakaan lebih dipicu oleh cuaca buruk atau kondisi jalan (*Risk Compensation Theory*)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(10, 4.8))\n",
                "weather_counts = df['weather_label'].value_counts(ascending=True)\n",
                "bars = plt.barh(weather_counts.index, weather_counts.values, color='#313695', edgecolor='black', alpha=0.8)\n",
                "\n",
                "plt.title('Distribusi Kejadian Kecelakaan Berdasarkan Kondisi Cuaca', fontsize=12, fontweight='bold')\n",
                "plt.xlabel('Jumlah Kejadian')\n",
                "plt.ylabel('Kondisi Cuaca')\n",
                "\n",
                "for bar in bars:\n",
                "    w = bar.get_width()\n",
                "    pct = (w / len(df)) * 100\n",
                "    plt.text(w + 500, bar.get_y() + bar.get_height()/2.0, f'{w:,} ({pct:.1f}%)', \n",
                "             ha='left', va='center', fontsize=8.5, fontweight='bold')\n",
                "\n",
                "plt.xlim(0, max(weather_counts.values) * 1.18)\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/5_cuaca_dominan.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(f\"Proporsi Cuaca Cerah: {df['weather_label'].value_counts()['Cerah'] / len(df) * 100:.2f}%\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 9. Analisis 6: Deteksi Nilai Ekstrem (Outlier) pada Korban dan Kendaraan\n",
                "Menggunakan boxplot untuk mendeteksi peristiwa tabrakan massal (*pileup* dan kecelakaan bus)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))\n",
                "\n",
                "# Boxplot jumlah kendaraan\n",
                "sns.boxplot(y=df['number_of_vehicles'], ax=axes[0], color='#80cdc1')\n",
                "axes[0].set_title('Outlier Jumlah Kendaraan per Tabrakan', fontweight='bold')\n",
                "axes[0].set_ylabel('Jumlah Kendaraan Terlibat')\n",
                "\n",
                "# Boxplot jumlah korban (skala log)\n",
                "sns.boxplot(y=df['number_of_casualties'], ax=axes[1], color='#f4a582')\n",
                "axes[1].set_title('Outlier Jumlah Korban per Tabrakan', fontweight='bold')\n",
                "axes[1].set_ylabel('Jumlah Korban Jiwa / Luka (Skala Log)')\n",
                "axes[1].set_yscale('log')\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.savefig('eda_output/6_outlier_kendaraan_korban.png', dpi=300)\n",
                "plt.show()\n",
                "\n",
                "print(f\"Maksimum Kendaraan Terlibat dalam 1 Insiden: {df['number_of_vehicles'].max()} unit\")\n",
                "print(f\"Maksimum Korban dalam 1 Insiden: {df['number_of_casualties'].max()} orang\")"
            ]
        }
    ],
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.11"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open('EDA_Tugas1_Road_Safety.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print("Notebook EDA_Tugas1_Road_Safety.ipynb updated successfully!")
