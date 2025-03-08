import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Load dataset
day_df = pd.read_csv("main_data.csv")

day_df['dteday'] = pd.to_datetime(day_df['dteday'])  # Konversi tanggal

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

# Pilihan visualisasi
option = st.selectbox(
    "Pilih Analisis yang Ingin Ditampilkan:",
    ("Penyewaan Sepeda per Musim", "Penyewaan Sepeda per Hari Kerja", "Tren Penyewaan per Bulan", 
     "Pengaruh Cuaca terhadap Penyewaan", "Analisis RFM", "Peta Stasiun Sepeda", "Clustering Penggunaan")
)

# Visualisasi Penyewaan Sepeda per Musim
if option == "Penyewaan Sepeda per Musim":
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='season', y='cnt', data=day_df, palette='Set2', ax=ax)
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

# Visualisasi Penyewaan Sepeda per Hari Kerja
elif option == "Penyewaan Sepeda per Hari Kerja":
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='workingday', y='cnt', data=day_df, palette='coolwarm', ax=ax)
    ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
    ax.set_xlabel("Tipe Hari")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_title("Perbandingan Penyewaan Sepeda antara Hari Kerja dan Hari Libur")
    st.pyplot(fig)

# Visualisasi Tren Penyewaan Sepeda per Bulan
elif option == "Tren Penyewaan per Bulan":
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(x='mnth', y='cnt', hue='yr', data=day_df, marker='o', palette='Dark2', ax=ax)
    ax.set_xticks(range(1,13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_title("Tren Penyewaan Sepeda per Bulan di Tahun 2011 & 2012")
    ax.legend(title="Tahun", labels=["2011", "2012"])
    st.pyplot(fig)

# Visualisasi Pengaruh Cuaca terhadap Penyewaan
elif option == "Pengaruh Cuaca terhadap Penyewaan":
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='weathersit', y='cnt', data=day_df, palette='coolwarm', ax=ax)
    ax.set_xticklabels(['Cerah', 'Berawan', 'Hujan Ringan/Snow', 'Hujan Deras/Snow Tebal'])
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan Sepeda")
    ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
    st.pyplot(fig)

# Analisis RFM
elif option == "Analisis RFM":
    max_date = day_df['dteday'].max()
    day_df['Recency'] = (max_date - day_df['dteday']).dt.days
    day_df['Frequency'] = day_df['cnt']
    day_df['Monetary'] = day_df['cnt']
    
    st.write("### Hasil Analisis RFM")
    st.dataframe(day_df[['dteday', 'Recency', 'Frequency', 'Monetary']].head(10))

# Peta Stasiun Sepeda (Dummy Data)
elif option == "Peta Stasiun Sepeda":
    bike_stations = [
        {"lat": 38.8951, "lon": -77.0364, "name": "Station 1"},
        {"lat": 38.8895, "lon": -77.0353, "name": "Station 2"},
    ]
    
    m = folium.Map(location=[38.8951, -77.0364], zoom_start=12)
    for station in bike_stations:
        folium.Marker(
            location=[station["lat"], station["lon"]],
            popup=station["name"],
            icon=folium.Icon(color="blue")
        ).add_to(m)
    
    folium_static(m)

# Clustering Penggunaan Sepeda
elif option == "Clustering Penggunaan":
    bins = [0, 2000, 4000, 7000]
    labels = ['Rendah', 'Sedang', 'Tinggi']
    day_df['Usage_Category'] = pd.cut(day_df['cnt'], bins=bins, labels=labels)
    
    st.write("### Pengelompokan Penggunaan Sepeda")
    st.dataframe(day_df[['dteday', 'cnt', 'Usage_Category']].head(10))
