import subprocess
import sys

def install_pkg(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install_pkg("numpy")
install_pkg("pandas")
install_pkg("matplotlib")
install_pkg("seaborn")
install_pkg("scipy")
install_pkg("streamlit")
install_pkg("babel")



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

customers_df = pd.read_csv("day.csv")

customers_df.rename(columns={
    "cnt": "jumlah_user_total",
    "atemp": "suhu_relatif"
}, inplace=True)

byworkday_df = customers_df.groupby(by="workingday").agg({
    "jumlah_user_total"   : "sum",
})

st.header("Hello, i will present my analysis on chart bellow")

st.subheader("Number of Customer by working day")
st.write("berdasarkan grafik dibawah bisa dilihat bahwa lebih banyak orang yang menggunakan sepeda pada saat hari kerja")
plt.figure(figsize=(10, 5))
colors = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="jumlah_user_total", 
    x="workingday",
    data=byworkday_df,
    palette=colors
)
plt.title("Number of Customer by working day", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel("1 = workday, 0 = not workday")
plt.tick_params(axis='x', labelsize=12)
 
st.pyplot(plt)



st.subheader("Number of Customer by season")
st.write("jumlah user paling tinggi tercatat pada musim fall yang dilanjutkan dengan musim summer dan winter.")

byseason_df = customers_df.groupby(by="season").agg({
    "jumlah_user_total"   : "sum",
})
 
plt.figure(figsize=(10, 5))
colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="jumlah_user_total", 
    x="season",
    data=byseason_df.sort_values(by="jumlah_user_total", ascending=False),
    palette=colors
)
plt.title("Number of Customer by seasons", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel("season (1:springer, 2:summer, 3:fall, 4:winter)")
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt)

st.subheader("Number of Customer by weather")
st.write("jumlah user paling tinggi bila cuaca cerah , dan berdasarkan grafik semakin parah cuaca semakin menurun jumlah pengguna, sampai pada cuaca extrim (4) sama sekali tidak ada user")

byweather_df = customers_df.groupby(by="weathersit").agg({
    "jumlah_user_total"   : "sum",
})
 
plt.figure(figsize=(10, 5))
colors = ["#72BCD4", "#D3D3D3",  "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="jumlah_user_total", 
    x="weathersit",
    data=byweather_df.sort_values(by="jumlah_user_total", ascending=False),
    palette=colors
)
plt.title("Number of Customer by weather", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(plt)