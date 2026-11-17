import sqlite3
import os
import glob
import pandas as pd
import numpy as np

base_dir = r"zenodo_traffic_data_v2_20260320/zenodo_export"
gpkg_files = glob.glob(os.path.join(base_dir, "*.gpkg"))

print(f"Total GPKG files found: {len(gpkg_files)}")

records = []
city_map = {'smg': 'Semarang', 'bdg': 'Bandung', 'jkt': 'Jakarta'}
period_order = ['night', 'morning_peak', 'morning_offpeak', 'lunch_hours', 'afternoon_offpeak', 'evening_peak', 'evening_offpeak', 'late_night']

for f in gpkg_files:
    fname = os.path.basename(f)
    parts = fname.replace('.gpkg', '').split('_')
    city_code = parts[-1]
    period = "_".join(parts[:-1])
    
    conn = sqlite3.connect(f)
    table_name = fname.replace('.gpkg', '')
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    
    city_name = city_map.get(city_code, city_code)
    records.append({
        'filename': fname,
        'city_code': city_code,
        'city': city_name,
        'period': period,
        'rows': len(df),
        'jam_factor_mean': df['jam_factor_mean'].mean(),
        'jam_factor_median': df['jam_factor_mean'].median(),
        'jam_factor_std': df['jam_factor_mean'].std(),
        'jam_factor_max': df['jam_factor_max'].max(),
        'speed_mean_kmh': (df['speed_mean'] * 3.6).mean(), # converting m/s to km/h if it is in m/s, let's verify
        'free_flow_kmh': (df['free_flow_mean'] * 3.6).mean(),
        'missing_values': df.isnull().sum().sum(),
        'unique_segments': df['osm_composite_id'].nunique()
    })

summary_df = pd.DataFrame(records)
print("=== SUMMARY PER FILE ===")
print(summary_df.to_string())

# Let's inspect one sample to verify speed units
conn = sqlite3.connect(os.path.join(base_dir, "morning_peak_smg.gpkg"))
sample_df = pd.read_sql("SELECT speed_mean, free_flow_mean, jam_factor_mean FROM morning_peak_smg LIMIT 10", conn)
conn.close()
print("\n=== SAMPLE RAW VALUES (morning_peak_smg) ===")
print(sample_df)
