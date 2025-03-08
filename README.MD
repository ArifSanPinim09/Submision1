# 📊 Proyek Analisis Data: Bike Sharing Dataset

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda berdasarkan berbagai faktor seperti musim, hari kerja, cuaca, dan waktu. Analisis dilakukan menggunakan Python dan divisualisasikan melalui dashboard interaktif dengan Streamlit.

## 📂 Struktur Folder
```
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   ├───data_1.csv
│   └───data_2.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## 🚀 Cara Menjalankan Proyek
### 1️⃣ Menjalankan Notebook
Buka dan jalankan `notebook.ipynb` untuk melihat analisis data secara keseluruhan.

### 2️⃣ Menjalankan Dashboard
1. Pastikan semua dependensi telah terinstal dengan menjalankan:
   ```sh
   pip install -r requirements.txt
   ```
2. Jalankan Streamlit dengan perintah:
   ```sh
   streamlit run dashboard/dashboard.py
   ```
3. Buka link yang muncul di terminal untuk mengakses dashboard interaktif.

## 📊 Fitur Dashboard
Dashboard ini memiliki beberapa fitur analisis yang dapat dipilih:
- 📅 **Penyewaan Sepeda per Musim**: Visualisasi distribusi penyewaan sepeda berdasarkan musim.
- 🏢 **Penyewaan Sepeda per Hari Kerja**: Perbandingan penyewaan sepeda antara hari kerja dan hari libur.
- 📈 **Tren Penyewaan per Bulan**: Grafik tren penyewaan sepeda per bulan selama dua tahun.
- 🌦 **Pengaruh Cuaca terhadap Penyewaan**: Analisis dampak kondisi cuaca terhadap jumlah penyewaan sepeda.
- 🔍 **Analisis RFM**: Evaluasi Recency, Frequency, dan Monetary untuk memahami pola penyewaan.
- 🗺 **Peta Stasiun Sepeda**: Visualisasi lokasi stasiun sepeda dengan peta interaktif.
- 🎯 **Clustering Penggunaan Sepeda**: Pengelompokan jumlah penyewaan berdasarkan kategori penggunaan.

## 📌 Dependensi
Pastikan Anda memiliki dependensi berikut:
- Python 3.x
- Streamlit
- Pandas
- Seaborn
- Matplotlib
- Folium
- Streamlit-Folium

Semua dependensi dapat diinstal dengan:
```sh
pip install -r requirements.txt
```

## 📚 Sumber Data
Dataset yang digunakan dalam proyek ini berasal dari **Bike Sharing Dataset**, yang mencakup data penyewaan sepeda berdasarkan faktor-faktor cuaca, hari kerja, dan musim.

## 👥 Kontributor
- Arifsan Pinim

## 📜 Lisensi
Proyek ini berlisensi MIT. Anda bebas untuk menggunakan dan memodifikasinya sesuai kebutuhan.

