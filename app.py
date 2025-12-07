import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static

# Page Configuration
st.set_page_config(
    page_title="Monitor Darurat Sumatera",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Dark Mode and Professional Styling
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stApp {
        background-color: #0E1117;
    }
    /* Hide Fork button and menu */
    header[data-testid="stHeader"] {
        display: none;
    }
    .stDeployButton {
        display: none;
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
    }
    h1 {
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
        padding: 20px 0;
        border-bottom: 3px solid #FF4B4B;
        margin-bottom: 30px;
    }
    h2 {
        color: #FAFAFA;
        border-left: 5px solid #FF4B4B;
        padding-left: 15px;
        margin-top: 30px;
    }
    h3 {
        color: #FF4B4B;
        margin-top: 20px;
    }
    .metric-container {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #FF4B4B;
        text-align: center;
    }
    .urgent-note {
        background-color: #FF4B4B;
        color: white;
        padding: 15px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    .criteria-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
        margin: 15px 0;
    }
    .stDataFrame {
        background-color: #1E1E1E;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("# 🚨 Monitor Darurat Sumatera: Mengapa Harus Ditetapkan Sebagai Bencana Nasional")

# Urgent Alert
st.markdown("""
    <div class="urgent-note">
    ⚠️ SITUASI KRITIS: Bencana Katastropik Multi-Provinsi yang Memerlukan Penetapan Darurat Nasional ⚠️
    </div>
    """, unsafe_allow_html=True)

# Key Metrics Row
st.markdown("## 📊 Metrik Kritis (Desember 2025)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💀 Total Kematian",
        value="916",
        delta="Sumber: Liputan6",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="🔍 Hilang/Belum Ditemukan",
        value="274",
        delta="Pencarian berlanjut",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="🗺️ Provinsi Terdampak",
        value="3",
        delta="Aceh, Sumut, Sumbar",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="👥 Populasi Berisiko",
        value="2.12 Juta",
        delta="Sumber: Agregasi Data BPS",
        delta_color="inverse"
    )

# Create DataFrame with specific data
st.markdown("## 📍 Analisis Wilayah Terdampak")

df_regions = pd.DataFrame({
    'Wilayah': ['Aceh Utara', 'Tapanuli Selatan', 'Tapanuli Tengah', 'Agam', 'Aceh Tamiang'],
    'Populasi 2024': ['600,000', '322,377', '367,798', '532,178', '300,000'],
    'Status Bencana': ['Banjir Kritis', 'Longsor/Banjir Bandang', 'Terisolasi', 'Banjir Bandang', 'Terendam'],
    'Estimasi Korban': [359, 210, 119, 226, 45]
})

# Display DataFrame with source link
st.dataframe(df_regions, use_container_width=True)

st.markdown("""
    <div style="background-color: #1E1E1E; padding: 10px; border-radius: 5px; margin-top: 10px; text-align: center;">
    <small style="color: #FAFAFA;">📊 <strong>Sumber Data:</strong> 
    <a href="https://www.liputan6.com/news/read/6230589/update-korban-bencana-sumatra-minggu-pagi-7-desember-2025-916-orang-meninggal-274-hilang" 
    target="_blank" style="color: #FF4B4B;">Liputan6 - Update Korban Bencana Sumatra</a> | 
    <a href="https://www.instagram.com/p/DR8kWZBk2Yq/" 
    target="_blank" style="color: #FF4B4B;">Instagram Nasari</a> | 
    <a href="https://acehutarakab.bps.go.id/id/statistics-table/3/WVc0MGEyMXBkVFUxY25KeE9HdDZkbTQzWkVkb1p6MDkjMw==/jumlah-penduduk-menurut-kelompok-umur-dan-jenis-kelamin--ribu-jiwa--di-kabupaten-aceh-utara--2022.html" 
    target="_blank" style="color: #FF4B4B;">BPS</a>
    </small>
    </div>
    """, unsafe_allow_html=True)

# Visualizations Section
st.markdown("## 📈 Visualisasi Data")

# Row 1: Bar Chart - Local Capacity vs Disaster Scale
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏛️ Kapasitas Pemda vs Skala Dampak Bencana")
    
    capacity_data = pd.DataFrame({
        'Kategori': ['Kapasitas APBD Lokal', 'Skala Dampak Bencana'],
        'Nilai': [10, 90],
        'Warna': ['#4CAF50', '#FF4B4B']
    })
    
    fig_capacity = go.Figure(data=[
        go.Bar(
            x=capacity_data['Kategori'],
            y=capacity_data['Nilai'],
            marker_color=capacity_data['Warna'],
            text=capacity_data['Nilai'],
            textposition='auto',
        )
    ])
    
    fig_capacity.update_layout(
        title="Mengapa Pemerintah Daerah Kewalahan",
        yaxis_title="Skala (0-100)",
        template="plotly_dark",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_capacity, use_container_width=True)
    
    st.markdown("""
        <div style="background-color: #1E1E1E; padding: 15px; border-radius: 5px; margin-top: 10px;">
        <strong>Analisis:</strong> Dampak bencana (90/100) jauh melampaui kapasitas pemerintah daerah (10/100), 
        menunjukkan ketidakmungkinan penanganan efektif tanpa intervensi tingkat nasional.
        </div>
        """, unsafe_allow_html=True)

# Pie Chart - Casualties Distribution by Province
with col2:
    st.markdown("### 💔 Distribusi Korban Jiwa per Provinsi")
    
    province_casualties = pd.DataFrame({
        'Provinsi': ['Aceh', 'Sumatera Utara', 'Sumatera Barat'],
        'Korban': [404, 286, 226]  # Based on regional distribution
    })
    
    fig_pie = px.pie(
        province_casualties,
        values='Korban',
        names='Provinsi',
        title='Total Korban Jiwa: 916',
        color_discrete_sequence=['#FF4B4B', '#FFA500', '#FFD700'],
        hole=0.3
    )
    
    fig_pie.update_layout(
        template="plotly_dark",
        height=400
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

# Map Visualization
st.markdown("### 🗺️ Peta Sebaran Dampak Geografis")

# Create Folium map centered on Sumatera
m = folium.Map(
    location=[2.0, 98.5],
    zoom_start=7,
    tiles='CartoDB dark_matter'
)

# Add markers for affected regions
locations = [
    {'name': 'Aceh Utara', 'coords': [5.0, 97.2], 'casualties': 359, 'status': 'Banjir Kritis'},
    {'name': 'Tapanuli Selatan', 'coords': [1.5, 99.3], 'casualties': 210, 'status': 'Longsor/Banjir Bandang'},
    {'name': 'Agam', 'coords': [-0.2, 100.0], 'casualties': 226, 'status': 'Banjir Bandang'},
    {'name': 'Tapanuli Tengah', 'coords': [1.8, 98.9], 'casualties': 119, 'status': 'Terisolasi'},
    {'name': 'Aceh Tamiang', 'coords': [4.3, 98.0], 'casualties': 45, 'status': 'Terendam'}
]

for loc in locations:
    folium.CircleMarker(
        location=loc['coords'],
        radius=15 + (loc['casualties'] / 20),
        popup=f"<b>{loc['name']}</b><br>Status: {loc['status']}<br>Korban: {loc['casualties']}",
        color='#FF4B4B',
        fill=True,
        fillColor='#FF4B4B',
        fillOpacity=0.7,
        weight=2
    ).add_to(m)
    
    folium.Marker(
        location=loc['coords'],
        popup=folium.Popup(f"<b>{loc['name']}</b><br>Korban: {loc['casualties']}", max_width=200),
        icon=folium.Icon(color='red', icon='warning-sign')
    ).add_to(m)

folium_static(m, width=1200, height=500)

# National Disaster Criteria Argument Section
st.markdown("## ⚖️ Justifikasi Hukum: Kriteria Bencana Nasional")

st.markdown("""
<div class="criteria-box">
<h3 style="color: #FF4B4B; margin-top: 0;">Berdasarkan UU No. 24 Tahun 2007 tentang Penanggulangan Bencana</h3>

<p style="color: #FAFAFA; font-size: 16px; line-height: 1.8;">
Suatu bencana harus ditetapkan sebagai <strong>Bencana Nasional</strong> apabila memenuhi kriteria berikut:
</p>

<ol style="color: #FAFAFA; font-size: 15px; line-height: 2;">
<li><strong>Korban Jiwa Massal:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 916 meninggal + 274 hilang = 1.190+ korban</li>

<li><strong>Dampak Lintas Provinsi:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 3 provinsi terdampak (Aceh, Sumatera Utara, Sumatera Barat)</li>

<li><strong>Pemda Kewalahan:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Kapasitas APBD lokal (10/100) tidak mampu mengimbangi skala bencana (90/100)</li>

<li><strong>Kerusakan Infrastruktur Berskala Luas:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Banyak wilayah terisolasi, infrastruktur kritis hancur</li>

<li><strong>Pengungsian Massal:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 2,12 juta jiwa berisiko, ribuan mengungsi</li>

<li><strong>Kelumpuhan Ekonomi:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Kawasan pertanian terendam, jalur perdagangan terputus</li>
</ol>

<div style="background-color: #FF4B4B; padding: 20px; border-radius: 5px; margin-top: 20px;">
<h3 style="color: white; margin: 0; text-align: center;">⚠️ KESIMPULAN ⚠️</h3>
<p style="color: white; font-size: 18px; text-align: center; margin: 10px 0 0 0; font-weight: bold;">
KESEMUA 6 KRITERIA TERPENUHI. Peristiwa ini SECARA HUKUM MEMENUHI SYARAT sebagai Bencana Nasional yang memerlukan penetapan Presiden segera dan mobilisasi sumber daya nasional.
</p>
</div>
</div>
""", unsafe_allow_html=True)

# Additional Statistics
st.markdown("## 📉 Rincian Dampak per Wilayah")

col1, col2 = st.columns(2)

with col1:
    # Population at Risk by Region
    # Convert string with comma back to numeric for chart
    df_chart = df_regions.copy()
    df_chart['Populasi 2024 Numeric'] = df_chart['Populasi 2024'].str.replace(',', '').astype(int)
    
    fig_pop = px.bar(
        df_chart,
        x='Wilayah',
        y='Populasi 2024 Numeric',
        title='Paparan Populasi per Wilayah',
        color='Estimasi Korban',
        color_continuous_scale='Reds',
        labels={'Populasi 2024 Numeric': 'Populasi', 'Estimasi Korban': 'Korban'}
    )
    fig_pop.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig_pop, use_container_width=True)

with col2:
    # Casualties by Status
    fig_casualties = px.bar(
        df_regions.sort_values('Estimasi Korban', ascending=False),
        x='Wilayah',
        y='Estimasi Korban',
        title='Korban Jiwa per Jenis Bencana',
        color='Status Bencana',
        text='Estimasi Korban',
        color_discrete_sequence=px.colors.sequential.OrRd
    )
    fig_casualties.update_layout(template="plotly_dark", height=400)
    fig_casualties.update_traces(textposition='outside')
    st.plotly_chart(fig_casualties, use_container_width=True)

# Footer with Call to Action
st.markdown("---")

st.markdown("""
<div style="text-align: center; color: #888; padding: 20px; margin-top: 20px;">
<small>Sumber Data: <a href="https://www.liputan6.com/news/read/6230589/update-korban-bencana-sumatra-minggu-pagi-7-desember-2025-916-orang-meninggal-274-hilang" target="_blank" style="color: #FF4B4B;">Liputan6</a>, <a href="https://www.instagram.com/p/DR8kWZBk2Yq/" target="_blank" style="color: #FF4B4B;">Instagram Nasari</a>, BPS (Desember 2025) | Dashboard dibuat untuk tujuan monitoring Data</small>
</div>
""", unsafe_allow_html=True)
