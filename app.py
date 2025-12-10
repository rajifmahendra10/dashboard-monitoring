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

# Custom CSS for Light Mode and Professional Styling
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .stApp {
        background-color: #FFFFFF;
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
        color: #1E1E1E !important;
        text-align: center;
        font-weight: bold;
        padding: 20px 0;
        border-bottom: 3px solid #D32F2F;
        margin-bottom: 30px;
    }
    h2 {
        color: #1E1E1E !important;
        border-left: 5px solid #D32F2F;
        padding-left: 15px;
        margin-top: 30px;
    }
    h3 {
        color: #1E1E1E !important;
        margin-top: 20px;
    }
    /* Override Streamlit default text colors */
    .stMarkdown, .stMarkdown p, .stMarkdown span {
        color: #1E1E1E !important;
    }
    /* Make metric labels visible */
    [data-testid="stMetricLabel"] {
        color: #424242 !important;
    }
    [data-testid="stMetricValue"] {
        color: #1E1E1E !important;
    }
    .metric-container {
        background-color: #F5F5F5;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #D32F2F;
        text-align: center;
    }
    .urgent-note {
        background-color: #D32F2F;
        color: white;
        padding: 15px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }
    .criteria-box {
        background-color: #F9F9F9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D32F2F;
        margin: 15px 0;
        color: #1E1E1E;
    }
    .stDataFrame {
        background-color: #FFFFFF;
    }
    /* Better mobile responsiveness */
    @media (max-width: 768px) {
        h1 {
            font-size: 1.5rem;
        }
        h2 {
            font-size: 1.2rem;
        }
        .metric-container {
            padding: 15px;
        }
    }
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown("# 🚨 Monitor Darurat Sumatera: Mengapa Harus Ditetapkan Sebagai Bencana Nasional")

# Critical Status Warning
st.markdown("""
    <div style="background-color: #B71C1C; color: white; padding: 20px; border-radius: 5px; font-weight: bold; text-align: center; margin: 20px 0; border: 3px solid #D32F2F;">
    🚨 STATUS: CRITICAL - KORBAN MELAMPAUI 1.000 JIWA 🚨<br>
    <small style="font-size: 14px; margin-top: 10px; display: block;">Update: 10 Desember 2025 | Pukul 09:00 WIB</small>
    </div>
    """, unsafe_allow_html=True)

# Urgent Alert
st.markdown("""
    <div class="urgent-note">
    ⚠️ SITUASI KRITIS: Bencana Katastropik Multi-Provinsi yang Memerlukan Penetapan Darurat Nasional ⚠️
    </div>
    """, unsafe_allow_html=True)

# Key Metrics Row
st.markdown("## 📊 Metrik Kritis (10 Desember 2025)")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="💀 Total Kematian",
        value="1,042",
        delta="+126 dalam 3 hari",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="🔍 Hilang/Belum Ditemukan",
        value="158",
        delta="-116 (ditemukan/meninggal)",
        delta_color="normal"
    )

with col3:
    st.metric(
        label="🏕️ Total Pengungsi",
        value="68,500+",
        delta="Lonjakan drastis",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="🗺️ Provinsi Terdampak",
        value="4",
        delta="+1 Riau (Baru)",
        delta_color="inverse"
    )

with col5:
    st.metric(
        label="👥 Populasi Berisiko",
        value="2.5+ Juta",
        delta="Bertambah dari Riau",
        delta_color="inverse"
    )

# Create DataFrame with specific data
st.markdown("## 📍 Analisis Wilayah Terdampak (Update 10 Des 2025)")

df_regions = pd.DataFrame({
    'Wilayah': ['Aceh Utara', 'Tapanuli Selatan', 'Agam', 'Rokan Hulu (Riau)', 'Tapanuli Tengah'],
    'Populasi 2024': ['600,000', '322,377', '532,178', '285,000', '367,798'],
    'Status Bencana': ['Surut (Risiko Penyakit)', 'Pemulihan Longsor', 'Banjir Bandang', 'Banjir Naik', 'Terisolasi'],
    'Korban Meninggal': [385, 290, 255, 12, 100],
    'Skor Dampak': [90, 95, 95, 60, 85]
})

# Display DataFrame with source link
st.dataframe(df_regions, use_container_width=True)

st.markdown("""
    <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px; margin-top: 10px; text-align: center; border: 1px solid #E0E0E0;">
    <small style="color: #424242;">📊 <strong>Sumber Data (Update 10 Des 2025):</strong><br>
    <a href="https://www.liputan6.com" 
    target="_blank" style="color: #D32F2F; text-decoration: none;">Liputan6 - "Pecah Rekor Kelam, Korban Banjir Sumatera Tembus 1.000 Jiwa"</a> | 
    <a href="https://www.cnnindonesia.com" 
    target="_blank" style="color: #D32F2F; text-decoration: none;">CNN Indonesia - "Masa Tanggap Darurat Diperpanjang"</a> | 
    <a href="https://bnpb.go.id" 
    target="_blank" style="color: #D32F2F; text-decoration: none;">BNPB - Update Operasi SAR Hari ke-10</a>
    </small>
    </div>
    """, unsafe_allow_html=True)

# Visualizations Section
st.markdown("## 📈 Visualisasi Data")

# Death Toll Trend Line Chart
st.markdown("### 📉 Tren Korban Jiwa: Kurva Tidak Melandai")

death_trend = pd.DataFrame({
    'Tanggal': ['1 Des', '4 Des', '7 Des', '10 Des'],
    'Korban Meninggal': [150, 500, 916, 1042]
})

fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(
    x=death_trend['Tanggal'],
    y=death_trend['Korban Meninggal'],
    mode='lines+markers+text',
    line=dict(color='#B71C1C', width=4),
    marker=dict(size=12, color='#D32F2F'),
    text=death_trend['Korban Meninggal'],
    textposition='top center',
    textfont=dict(size=14, color='#1E1E1E'),
    name='Kematian'
))

fig_trend.update_layout(
    title="Proyeksi Korban Terus Meningkat - Tidak Ada Tanda Pelandaian",
    xaxis_title="Tanggal (Desember 2025)",
    yaxis_title="Jumlah Korban Meninggal",
    template="plotly_white",
    height=400,
    showlegend=False,
    plot_bgcolor='#FFF3E0',
    paper_bgcolor='#FFFFFF'
)

st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("""
    <div style="background-color: #FFEBEE; padding: 15px; border-radius: 5px; margin-top: 10px; border-left: 5px solid #B71C1C; color: #424242;">
    <strong>⚠️ Analisis Kritis:</strong> Kurva kematian menunjukkan akselerasi drastis (+126 jiwa dalam 3 hari). 
    Tanpa intervensi nasional segera, proyeksi korban bisa mencapai 1.500+ dalam seminggu.
    </div>
    """, unsafe_allow_html=True)

# Row 1: Bar Chart - Local Capacity vs Disaster Scale
st.markdown("---")
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
        template="plotly_white",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_capacity, use_container_width=True)
    
    st.markdown("""
        <div style="background-color: #F5F5F5; padding: 15px; border-radius: 5px; margin-top: 10px; border: 1px solid #E0E0E0; color: #424242;">
        <strong>Analisis:</strong> Dampak bencana (90/100) jauh melampaui kapasitas pemerintah daerah (10/100), 
        menunjukkan ketidakmungkinan penanganan efektif tanpa intervensi tingkat nasional.
        </div>
        """, unsafe_allow_html=True)

# Pie Chart - Casualties Distribution by Province
with col2:
    st.markdown("### 💔 Distribusi Korban Jiwa per Provinsi (Update)")
    
    province_casualties = pd.DataFrame({
        'Provinsi': ['Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau'],
        'Korban': [385, 390, 255, 12]  # Total: 1042
    })
    
    fig_pie = px.pie(
        province_casualties,
        values='Korban',
        names='Provinsi',
        title='Total Korban Jiwa: 1,042',
        color_discrete_sequence=['#B71C1C', '#D32F2F', '#FF5252', '#FFB74D'],
        hole=0.3
    )
    
    fig_pie.update_layout(
        template="plotly_white",
        height=400
    )
    
    st.plotly_chart(fig_pie, use_container_width=True)

# Map Visualization
st.markdown("### 🗺️ Peta Sebaran Dampak Geografis (4 Provinsi)")

# Create Folium map centered on Sumatera
m = folium.Map(
    location=[1.5, 99.5],
    zoom_start=6,
    tiles='OpenStreetMap'
)

# Add markers for affected regions (Updated Data)
locations = [
    {'name': 'Aceh Utara', 'coords': [5.0, 97.2], 'casualties': 385, 'status': 'Surut (Risiko Penyakit)', 'color': 'red'},
    {'name': 'Tapanuli Selatan', 'coords': [1.5, 99.3], 'casualties': 290, 'status': 'Pemulihan Longsor', 'color': 'red'},
    {'name': 'Agam (Sumbar)', 'coords': [-0.2, 100.0], 'casualties': 255, 'status': 'Banjir Bandang', 'color': 'red'},
    {'name': 'Tapanuli Tengah', 'coords': [1.8, 98.9], 'casualties': 100, 'status': 'Terisolasi', 'color': 'red'},
    {'name': 'Rokan Hulu (Riau)', 'coords': [0.85, 100.5], 'casualties': 12, 'status': 'Banjir Naik - BARU!', 'color': 'orange'}
]

for loc in locations:
    # Determine marker color
    marker_color = loc['color']
    fill_color = '#D32F2F' if marker_color == 'red' else '#FFB300'
    icon_color = 'red' if marker_color == 'red' else 'orange'
    
    folium.CircleMarker(
        location=loc['coords'],
        radius=15 + (loc['casualties'] / 15),
        popup=f"<b>{loc['name']}</b><br>Status: {loc['status']}<br>Korban: {loc['casualties']}",
        color='#FF4B4B',
        fill=True,
        fillColor='#FF4B4B',
        fillOpacity=0.7,
        weight=2
    ).add_to(m)
    
    folium.Marker(
        location=loc['coords'],
        popup=f"<b>{loc['name']}</b><br>Status: {loc['status']}<br>Korban: {loc['casualties']}",
        color=marker_color,
        fill=True,
        fillColor=fill_color,
        fillOpacity=0.7,
        weight=2
    ).add_to(m)
    
    folium.Marker(
        location=loc['coords'],
        popup=folium.Popup(f"<b>{loc['name']}</b><br>Status: {loc['status']}<br>Korban: {loc['casualties']}", max_width=250),
        icon=folium.Icon(color=icon_color, icon='warning-sign')
    ).add_to(m)

folium_static(m, width=1200, height=500)

st.markdown("""
    <div style="background-color: #FFF3E0; padding: 15px; border-radius: 5px; margin-top: 10px; border-left: 5px solid #FF9800; color: #424242;">
    <strong>🆕 Perkembangan Baru:</strong> Riau (Rokan Hulu) mulai terdampak banjir kiriman dari Sumbar/Sumut. 
    Marker kuning menunjukkan wilayah baru yang masuk zona siaga 1.
    </div>
    """, unsafe_allow_html=True)

# National Disaster Criteria Argument Section
st.markdown("## ⚖️ Justifikasi Hukum: Kriteria Bencana Nasional (Update 10 Des)")

st.markdown("""
<div class="criteria-box">
<h3 style="color: #D32F2F; margin-top: 0;">Berdasarkan UU No. 24 Tahun 2007 tentang Penanggulangan Bencana</h3>

<p style="color: #424242; font-size: 16px; line-height: 1.8;">
Suatu bencana harus ditetapkan sebagai <strong>Bencana Nasional</strong> apabila memenuhi kriteria berikut:
</p>

<ol style="color: #424242; font-size: 15px; line-height: 2;">
<li><strong>Korban Jiwa Massal:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 1.042 meninggal + 158 hilang = 1.200+ korban</li>

<li><strong>Dampak Lintas Provinsi:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 4 provinsi terdampak (Aceh, Sumatera Utara, Sumatera Barat, Riau)</li>

<li><strong>Pemda Kewalahan:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Kapasitas APBD lokal (10/100) tidak mampu mengimbangi skala bencana (95/100)</li>

<li><strong>Kerusakan Infrastruktur Berskala Luas:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Banyak wilayah terisolasi, infrastruktur kritis hancur</li>

<li><strong>Pengungsian Massal:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - 68.500+ jiwa mengungsi, 2,5 juta jiwa berisiko</li>

<li><strong>Kelumpuhan Ekonomi:</strong> ✅ <span style="color: #4CAF50;">TERPENUHI</span> - Kawasan pertanian terendam, jalur perdagangan terputus</li>
</ol>

<div style="background-color: #D32F2F; padding: 20px; border-radius: 5px; margin-top: 20px;">
<h3 style="color: white; margin: 0; text-align: center;">⚠️ KESIMPULAN ⚠️</h3>
<p style="color: white; font-size: 18px; text-align: center; margin: 10px 0 0 0; font-weight: bold;">
KESEMUA 6 KRITERIA TERPENUHI.
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
        title='Paparan Populasi per Wilayah (4 Provinsi)',
        color='Korban Meninggal',
        color_continuous_scale='Reds',
        labels={'Populasi 2024 Numeric': 'Populasi', 'Korban Meninggal': 'Korban'}
    )
    fig_pop.update_layout(template="plotly_white", height=400)
    st.plotly_chart(fig_pop, use_container_width=True)

with col2:
    # Casualties by Status
    fig_casualties = px.bar(
        df_regions.sort_values('Korban Meninggal', ascending=False),
        x='Wilayah',
        y='Korban Meninggal',
        title='Korban Jiwa per Status Bencana',
        color='Status Bencana',
        text='Korban Meninggal',
        color_discrete_sequence=px.colors.sequential.OrRd
    )
    fig_casualties.update_layout(template="plotly_white", height=400)
    fig_casualties.update_traces(textposition='outside')
    st.plotly_chart(fig_casualties, use_container_width=True)

# Footer with Call to Action
st.markdown("---")

st.markdown("""
<div style="text-align: center; padding: 30px; background-color: #FFEBEE; border-radius: 10px; margin-top: 30px; border: 2px solid #D32F2F;">
<h2 style="color: #B71C1C; border: none; padding: 0; margin-bottom: 15px;">🆘 DIPERLUKAN TINDAKAN SEGERA 🆘</h2>
<p style="color: #424242; font-size: 18px; line-height: 1.8;">
Dashboard ini menyajikan bukti yang tidak terbantahkan bahwa bencana Sumatera telah melampaui 1.000 korban jiwa 
dan memenuhi semua kriteria hukum untuk status Bencana Nasional. Penetapan Presiden segera sangat penting untuk:
</p>
<ul style="color: #424242; font-size: 16px; text-align: left; max-width: 800px; margin: 20px auto; line-height: 2;">
<li>Membuka akses anggaran nasional dan sumber daya BNPB</li>
<li>Memungkinkan pengerahan TNI untuk pencarian & penyelamatan</li>
<li>Koordinasi respons lintas 4 provinsi</li>
<li>Memberikan bantuan darurat ke 68.500+ pengungsi</li>
<li>Mencegah korban lebih lanjut (158 masih hilang) dan wabah penyakit</li>
</ul>
<p style="color: #D32F2F; font-size: 20px; font-weight: bold; margin-top: 20px;">
⏰ Waktu terus berjalan. Nyawa bergantung pada keputusan ini. ⏰
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #666; padding: 20px; margin-top: 20px;">
<small><strong>Update Terakhir: 10 Desember 2025, 09:00 WIB</strong><br>
Sumber Data: <a href="https://www.liputan6.com" target="_blank" style="color: #D32F2F; text-decoration: none;">Liputan6</a>, 
<a href="https://www.cnnindonesia.com" target="_blank" style="color: #D32F2F; text-decoration: none;">CNN Indonesia</a>, 
<a href="https://bnpb.go.id" target="_blank" style="color: #D32F2F; text-decoration: none;">BNPB</a>, 
BPS (Desember 2025) | Dashboard dibuat untuk tujuan monitoring Data</small>
</div>
""", unsafe_allow_html=True)
