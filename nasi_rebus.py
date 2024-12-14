import pandas as pd

file_path = 'D:\Kuliah\Semester 5\Pemrograman Dasar\Reguler\Tugas 10 Pemdas\disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv'  # Ganti dengan path ke file Anda
df_sampah = pd.read_csv(file_path)

filter_kolom = ['id', 'kode_kabupaten_kota', 'nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']
df_sampah = df_sampah[filter_kolom]

#nomor 2

total_produksi_2016 = 0

for index, row in df_sampah.iterrows():
    if row['tahun'] == 2016:
        total_produksi_2016 += row['jumlah_produksi_sampah']

print(f"Total sampah 2016: {total_produksi_2016:.2f}")


#nomor 3

total_per_tahun = {}

for index, row in df_sampah.iterrows():
    tahun = row['tahun']
    prod_sampah = row['jumlah_produksi_sampah']
    
    if tahun in total_per_tahun:
        total_per_tahun[tahun] += prod_sampah
    else:
        total_per_tahun[tahun] = prod_sampah

for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun}: Total jumlah produksi sampah = {total:.2f}")
    
#nomor 4

total_kotapertahun = {}

for index, row in df_sampah.iterrows():
    tahun = row['tahun']
    kota = row['nama_kabupaten_kota']
    prod_sampah = row['jumlah_produksi_sampah']
    
    if tahun not in total_kotapertahun:
        total_kotapertahun[tahun] = {}
    
    if kota not in total_kotapertahun[tahun]:
        total_kotapertahun[tahun][kota] = 0
    
    total_kotapertahun[tahun][kota] += prod_sampah

for tahun, data_kota in total_kotapertahun.items():
    print(f"Tahun {tahun}:")
    for kota, total in data_kota.items():
        print(f"  {kota}: {total:.2f}")

data_per_kota_per_tahun = []
for tahun, data_kota in total_kotapertahun.items():
    for kota, total in data_kota.items():
        data_per_kota_per_tahun.append([tahun, kota, total])

df_kota_per_tahun = pd.DataFrame(data_per_kota_per_tahun, columns=['Tahun', 'Kota/Kabupaten', 'Total Produksi Sampah'])


df_kota_per_tahun.to_csv('total_per_kota_per_tahun.csv', index=False)
df_kota_per_tahun.to_excel('total_per_kota_per_tahun.xlsx', index=False)