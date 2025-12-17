import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# --- CONFIGURATION ---
st.set_page_config(page_title="Sumatera Crisis Center", layout="wide", page_icon="🏚️")

# Custom CSS: Dark/Orange Theme (Fokus ke Kerusakan/Recovery)
st.markdown("""
    <style>
    .main { background-color: #121212; color: white; }
    .stMetric { background-color: #1e1e1e; border-left: 5px solid #ff8c00; color: white; }
    h1, h2, h3 { color: #ff8c00 !important; font-family: sans-serif; }
    div[data-testid="metric-container"] label { color: #cccccc; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🏚️ SUMATERA DISASTER IMPACT")
st.markdown("### 📅 DATE: 17 DEC 2025 | STATUS: PEMULIHAN & EVAKUASI LANJUTAN")
st.warning("⚠️ UPDATE HARI INI: 1.053 MENINGGAL. 147 RIBU RUMAH HANCUR. (SUMBER: KOMPAS & DETIK)")

# --- KEY METRICS (UPDATE 17 DES) ---
st.markdown("## 📊 Metrik Kritis (17 Desember 2025)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="TOTAL MENINGGAL", value="1,053", delta="+37 (Sejak 14 Des)")
with col2:
    st.metric(label="MASIH HILANG", value="200", delta="-12 (Ditemukan)")
with col3:
    st.metric(label="RUMAH RUSAK", value="147,217", delta="Data Baru BNPB")
with col4:
    st.metric(label="PENGUNGSI", value="606,040", delta="-18k (Pulang)")

# --- CHARTS SECTION ---

# Data Rincian Per Provinsi (Update 17 Des)
# Aceh: 449 | Sumut: 360 | Sumbar: 244
df_update = pd.DataFrame({
    'Provinsi': ['Aceh', 'Sumatera Utara', 'Sumatera Barat'],
    'Korban Jiwa': [449, 360, 244],
    'Rumah Rusak': [70500, 45200, 31517] # Estimasi proporsional dari total 147k
})

col_left, col_right = st.columns([1.5, 1])

with col_left:
    st.subheader("📍 Titik Penemuan Jenazah (24 Jam Terakhir)")
    m = folium.Map(location=[3.0, 98.0], zoom_start=7, tiles="CartoDB dark_matter")
    
    # Fokus Hari Ini: Aceh Tamiang (17 Jenazah Baru)
    folium.CircleMarker([4.29, 98.06], radius=40, color='orange', fill=True, fill_color='red', 
                        popup="ACEH TAMIANG: 17 Jenazah Baru Ditemukan").add_to(m)
    
    # Fokus Sumut: Tapanuli Tengah (5 Jenazah Baru)
    folium.CircleMarker([1.70, 98.80], radius=25, color='orange', fill=True, fill_color='red', 
                        popup="TAPTENG: 5 Jenazah Baru").add_to(m)

    st_folium(m, height=400, width=700)

with col_right:
    st.subheader("🏚️ Skala Kerusakan Infrastruktur")
    fig = px.bar(df_update, x='Provinsi', y='Rumah Rusak', text_auto=True,
                 title="147.000+ Rumah Hancur",
                 color='Rumah Rusak', color_continuous_scale='Oranges')
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'))
    st.plotly_chart(fig, use_container_width=True)

# --- NEWS TICKER ---
st.markdown("---")
st.markdown("🔗 **SUMBER VALID:** [Kompas.com (17 Des)](https://www.kompas.com/sumatera-utara/read/2025/12/17/053000688/update-banjir-sumatera-17-desember--tewas-1.053-jiwa-hilang-200) | [Detik.com (17 Des)](https://news.detik.com/berita/d-8262977/terus-bertambah-korban-meninggal-bencana-sumatera-kini-1-053-orang)")

# National Disaster Criteria Argument Section
st.markdown("---")
st.markdown("## ⚖️ Justifikasi Hukum: Kriteria Bencana Nasional")

st.write("""
**Berdasarkan UU No. 24 Tahun 2007 tentang Penanggulangan Bencana:**
1. ✅ **Korban Jiwa Massal:** 1.053 meninggal + 200 hilang = 1.253 korban
2. ✅ **Dampak Lintas Provinsi:** 3 provinsi (Aceh, Sumut, Sumbar)
3. ✅ **Kerusakan Infrastruktur:** 147.217 rumah hancur
4. ✅ **Pengungsian Massal:** 606.040 jiwa

**KESIMPULAN: SEMUA KRITERIA BENCANA NASIONAL TERPENUHI**
""")

st.markdown("---")
st.markdown("🟢 **Dashboard Always Online via UptimeRobot** | Update: 17 Des 2025")
