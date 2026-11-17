import sqlite3
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

output_dir = "eda_charts"
os.makedirs(output_dir, exist_ok=True)

base_dir = r"zenodo_traffic_data_v2_20260320/zenodo_export"
gpkg_files = glob.glob(os.path.join(base_dir, "*.gpkg"))

city_map = {'smg': 'Semarang', 'bdg': 'Bandung', 'jkt': 'Jakarta'}
period_order = [
    'night', 'morning_peak', 'morning_offpeak', 'lunch_hours', 
    'afternoon_offpeak', 'evening_peak', 'evening_offpeak', 'late_night'
]
period_labels = [
    'Night\n(00-06)', 'Morn Peak\n(06-09)', 'Morn Offpeak\n(09-12)', 'Lunch\n(12-14)',
    'Aft Offpeak\n(14-16)', 'Eve Peak\n(16-19)', 'Eve Offpeak\n(19-22)', 'Late Night\n(22-00)'
]
period_label_dict = dict(zip(period_order, period_labels))

dfs = []
for f in gpkg_files:
    fname = os.path.basename(f)
    parts = fname.replace('.gpkg', '').split('_')
    city_code = parts[-1]
    period = "_".join(parts[:-1])
    
    conn = sqlite3.connect(f)
    table_name = fname.replace('.gpkg', '')
    df = pd.read_sql(f"SELECT osm_composite_id, jam_factor_mean, jam_factor_std, jam_factor_min, jam_factor_max, speed_mean, free_flow_mean FROM {table_name}", conn)
    conn.close()
    
    df['city_code'] = city_code
    df['city'] = city_map[city_code]
    df['period'] = period
    df['speed_kmh'] = df['speed_mean'] * 3.6
    df['free_flow_kmh'] = df['free_flow_mean'] * 3.6
    df['speed_ratio'] = df['speed_mean'] / (df['free_flow_mean'] + 1e-5)
    df['speed_ratio'] = df['speed_ratio'].clip(0, 1.5)
    
    # Categorization based on HERE Jam Factor Scale
    # 0.0–1.0: Free flow
    # 1.0–3.0: Light traffic
    # 3.0–6.0: Moderate traffic
    # 6.0–8.0: Heavy traffic
    # 8.0–10.0: Severe congestion
    conditions = [
        (df['jam_factor_mean'] < 1.0),
        (df['jam_factor_mean'] >= 1.0) & (df['jam_factor_mean'] < 3.0),
        (df['jam_factor_mean'] >= 3.0) & (df['jam_factor_mean'] < 6.0),
        (df['jam_factor_mean'] >= 6.0) & (df['jam_factor_mean'] < 8.0),
        (df['jam_factor_mean'] >= 8.0)
    ]
    categories = ['Free Flow (0-1)', 'Light (1-3)', 'Moderate (3-6)', 'Heavy (6-8)', 'Severe (8-10)']
    df['congestion_category'] = np.select(conditions, categories, default='Unknown')
    
    dfs.append(df)

all_df = pd.concat(dfs, ignore_index=True)
all_df['period'] = pd.Categorical(all_df['period'], categories=period_order, ordered=True)

print(f"Total compiled records: {len(all_df)}")

# 1. CHART 1: Jam Factor Distribution across Cities (Evening Peak vs Night)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
palette = {'Semarang': '#2b5c8f', 'Bandung': '#2ca02c', 'Jakarta': '#d62728'}

sns.kdeplot(
    data=all_df[all_df['period'] == 'evening_peak'], 
    x='jam_factor_mean', hue='city', common_norm=False, 
    fill=True, palette=palette, alpha=0.3, ax=axes[0]
)
axes[0].set_title("Distribusi Kemacetan saat Jam Sibuk Sore (Evening Peak, 16:00-19:00)", fontsize=11, fontweight='bold')
axes[0].set_xlabel("Rata-rata Jam Factor (0 = Lancar, 10 = Macet Total)")
axes[0].set_ylabel("Kepadatan (Density)")
axes[0].set_xlim(0, 10)

sns.kdeplot(
    data=all_df[all_df['period'] == 'night'], 
    x='jam_factor_mean', hue='city', common_norm=False, 
    fill=True, palette=palette, alpha=0.3, ax=axes[1]
)
axes[1].set_title("Distribusi Kemacetan saat Dini Hari (Night, 00:00-06:00)", fontsize=11, fontweight='bold')
axes[1].set_xlabel("Rata-rata Jam Factor (0 = Lancar, 10 = Macet Total)")
axes[1].set_ylabel("Kepadatan (Density)")
axes[1].set_xlim(0, 10)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "1_distribution_peak_vs_night.png"))
plt.close()
print("Saved 1_distribution_peak_vs_night.png")

# 2. CHART 2: 24-Hour Temporal Congestion Profile (Average Jam Factor by Period)
temporal_agg = all_df.groupby(['city', 'period'], observed=False)['jam_factor_mean'].agg(['mean', 'std']).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
for city in ['Jakarta', 'Bandung', 'Semarang']:
    cdata = temporal_agg[temporal_agg['city'] == city]
    ax.plot(range(8), cdata['mean'], marker='o', linewidth=2.5, markersize=8, label=city, color=palette[city])
    ax.fill_between(range(8), cdata['mean'] - 0.2*cdata['std'], cdata['mean'] + 0.2*cdata['std'], color=palette[city], alpha=0.15)

ax.set_xticks(range(8))
ax.set_xticklabels([period_label_dict[p] for p in period_order], fontsize=9)
ax.set_ylabel("Rata-rata Jam Factor", fontsize=11, fontweight='bold')
ax.set_title("Profil Fluktuasi Kemacetan Spasio-Temporal 24 Jam (8 Periode Waktu)", fontsize=13, fontweight='bold')
ax.legend(title="Kota Metropolitan", frameon=True)
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(0, 4.5)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "2_temporal_congestion_profile.png"))
plt.close()
print("Saved 2_temporal_congestion_profile.png")

# 3. CHART 3: Speed vs Free Flow Comparison across Time Periods
speed_agg = all_df.groupby(['city', 'period'], observed=False)[['speed_kmh', 'free_flow_kmh']].mean().reset_index()

fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
for i, city in enumerate(['Jakarta', 'Bandung', 'Semarang']):
    cdata = speed_agg[speed_agg['city'] == city]
    x = np.arange(8)
    width = 0.38
    
    axes[i].bar(x - width/2, cdata['speed_kmh'], width, label='Kecepatan Aktual', color=palette[city], alpha=0.85)
    axes[i].bar(x + width/2, cdata['free_flow_kmh'], width, label='Kecepatan Ideal (Free-flow)', color='#95a5a6', alpha=0.5)
    
    axes[i].set_title(f"Kota {city}", fontsize=12, fontweight='bold')
    axes[i].set_xticks(x)
    axes[i].set_xticklabels([period_label_dict[p].split('\n')[0] for p in period_order], rotation=45, fontsize=8)
    axes[i].grid(True, linestyle='--', alpha=0.5)
    if i == 0:
        axes[i].set_ylabel("Kecepatan Rata-rata (km/jam)", fontsize=10, fontweight='bold')
    axes[i].legend(loc='upper right', fontsize=8)

plt.suptitle("Perbandingan Kecepatan Aktual vs Kondisi Bebas Hambatan (Free-Flow)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "3_speed_vs_freeflow.png"))
plt.close()
print("Saved 3_speed_vs_freeflow.png")

# 4. CHART 4: Proportion of Congestion Severity by City in Evening Peak
peak_df = all_df[all_df['period'] == 'evening_peak']
cat_order = ['Free Flow (0-1)', 'Light (1-3)', 'Moderate (3-6)', 'Heavy (6-8)', 'Severe (8-10)']
color_cats = ['#2ecc71', '#3498db', '#f39c12', '#e67e22', '#e74c3c']

cat_prop = peak_df.groupby(['city', 'congestion_category'], observed=False).size().unstack(fill_value=0)
cat_prop = cat_prop[cat_order]
cat_prop_pct = cat_prop.div(cat_prop.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 6))
cat_prop_pct.loc[['Semarang', 'Bandung', 'Jakarta']].plot(
    kind='barh', stacked=True, color=color_cats, ax=ax, edgecolor='white', width=0.65
)
ax.set_title("Proporsi Tingkat Keparahan Kemacetan Segmen Jalan (Evening Peak, 16:00-19:00)", fontsize=12, fontweight='bold')
ax.set_xlabel("Persentase Segmen Jalan (%)", fontsize=10, fontweight='bold')
ax.set_ylabel("Kota Metropolitan", fontsize=10, fontweight='bold')
ax.legend(title="Tingkat Kemacetan", bbox_to_anchor=(1.02, 1), loc='upper left')
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Annotate percentages in bars
for c in ax.containers:
    labels = [f"{v.get_width():.1f}%" if v.get_width() > 5 else "" for v in c]
    ax.bar_label(c, labels=labels, label_type='center', color='white', fontweight='bold', fontsize=8)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "4_congestion_severity_proportion.png"))
plt.close()
print("Saved 4_congestion_severity_proportion.png")

# 5. CHART 5: Speed Drop Correlation with Jam Factor (Scatter + Trend)
sample_scatter = all_df.sample(n=6000, random_state=42)

fig, ax = plt.subplots(figsize=(10, 6))
for city in ['Jakarta', 'Bandung', 'Semarang']:
    cdata = sample_scatter[sample_scatter['city'] == city]
    ax.scatter(cdata['jam_factor_mean'], cdata['speed_kmh'], alpha=0.3, label=city, color=palette[city], s=15)

ax.set_title("Hubungan Non-Linear Antara Jam Factor dan Kecepatan Rata-rata Kendaraan", fontsize=12, fontweight='bold')
ax.set_xlabel("Jam Factor Rata-rata (Indeks Kemacetan 0-10)", fontsize=10, fontweight='bold')
ax.set_ylabel("Kecepatan Kendaraan (km/jam)", fontsize=10, fontweight='bold')
ax.legend(title="Kota")
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "5_jam_factor_vs_speed_scatter.png"))
plt.close()
print("Saved 5_jam_factor_vs_speed_scatter.png")

# 6. CHART 6: Jam Factor Boxplot Comparison Across Periods for Jakarta
fig, ax = plt.subplots(figsize=(12, 5))
jkt_df = all_df[all_df['city'] == 'Jakarta']
sns.boxplot(
    data=jkt_df, x='period', y='jam_factor_mean', 
    palette='Blues', ax=ax, flierprops={'marker': '.', 'markersize': 2, 'alpha': 0.2}
)
ax.set_xticks(range(8))
ax.set_xticklabels([period_label_dict[p] for p in period_order], fontsize=9)
ax.set_title("Boxplot Sebaran Jam Factor Jakarta di Setiap Periode Waktu (Mendeteksi Pencilan)", fontsize=12, fontweight='bold')
ax.set_xlabel("Periode Waktu", fontsize=10, fontweight='bold')
ax.set_ylabel("Jam Factor (0-10)", fontsize=10, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "6_jkt_period_boxplot.png"))
plt.close()
print("Saved 6_jkt_period_boxplot.png")

print("All EDA charts generated successfully!")
