import sqlite3
import glob
import os
import pandas as pd
import numpy as np
from scipy import stats

base_dir = r"zenodo_traffic_data_v2_20260320/zenodo_export"
gpkg_files = glob.glob(os.path.join(base_dir, "*.gpkg"))
city_map = {'smg': 'Semarang', 'bdg': 'Bandung', 'jkt': 'Jakarta'}

dfs = []
for f in gpkg_files:
    fname = os.path.basename(f)
    parts = fname.replace('.gpkg', '').split('_')
    city_code = parts[-1]
    period = "_".join(parts[:-1])
    
    conn = sqlite3.connect(f)
    table_name = fname.replace('.gpkg', '')
    df = pd.read_sql(f"SELECT osm_composite_id, jam_factor_mean, jam_factor_std, speed_mean, free_flow_mean FROM {table_name}", conn)
    conn.close()
    
    df['city'] = city_map[city_code]
    df['period'] = period
    df['speed_kmh'] = df['speed_mean'] * 3.6
    df['free_flow_kmh'] = df['free_flow_mean'] * 3.6
    dfs.append(df)

all_df = pd.concat(dfs, ignore_index=True)

print("=== STATISTIK DESKRIPTIF GLOBAL ===")
print(all_df[['jam_factor_mean', 'speed_kmh', 'free_flow_kmh']].describe())

print("\n=== SKEWNESS & KURTOSIS ===")
print(f"Jam Factor Skewness: {all_df['jam_factor_mean'].skew():.4f}")
print(f"Jam Factor Kurtosis: {all_df['jam_factor_mean'].kurt():.4f}")
print(f"Speed Skewness: {all_df['speed_kmh'].skew():.4f}")

print("\n=== KORELASI PEARSON & SPEARMAN (Jam Factor vs Speed) ===")
pearson_corr = all_df['jam_factor_mean'].corr(all_df['speed_kmh'], method='pearson')
spearman_corr = all_df['jam_factor_mean'].corr(all_df['speed_kmh'], method='spearman')
print(f"Pearson: {pearson_corr:.4f}")
print(f"Spearman: {spearman_corr:.4f}")

print("\n=== STATISTIK PER KOTA (JAM FACTOR & SPEED) ===")
city_summary = all_df.groupby('city').agg({
    'jam_factor_mean': ['mean', 'median', 'std'],
    'speed_kmh': ['mean', 'median', 'std'],
    'free_flow_kmh': ['mean']
})
print(city_summary)

print("\n=== PERBANDINGAN PEAK (EVENING) VS NIGHT ===")
peak_vs_night = all_df[all_df['period'].isin(['evening_peak', 'night'])].groupby(['city', 'period'], observed=False).agg({
    'jam_factor_mean': 'mean',
    'speed_kmh': 'mean'
}).unstack()
print(peak_vs_night)
