"""
IRCTC Live Dashboard - Dummy Interactive Version
Run this locally with: streamlit run irctc_live_dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="IRCTC Financial Dashboard | Kartik Rao",
    page_icon="🚄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1F4E79;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #424242;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1F4E79 0%, #2E7D32 100%);
        padding: 1.2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #E3F2FD;
        border-left: 5px solid #1F4E79;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-header">🚄 IRCTC Financial Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">3-Statement Model + Scenario Analysis | Prepared by Kartik Rao | MBA Finance 2026</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Dashboard Controls")
st.sidebar.markdown("**Forecast Period:** FY26 – FY30")
scenario = st.sidebar.selectbox("Select Scenario", ["Base Case", "Bull Case", "Bear Case"], index=0)

# Data
years = ['FY25A', 'FY26E', 'FY27E', 'FY28E', 'FY29E', 'FY30E']
revenue = [4675, 5237, 5811, 6391, 6964, 7519]
pat = [1315, 1214, 1403, 1606, 1803, 2006]
ebitda_margin = [32.9, 33.4, 34.8, 36.1, 37.2, 38.3]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("FY30 Revenue", "₹7,519 Cr", "+61% from FY25")
with col2:
    st.metric("FY30 PAT", "₹2,006 Cr", "+53% from FY25")
with col3:
    st.metric("EBITDA Margin (FY30)", "38.3%", "+5.4 pp expansion")
with col4:
    st.metric("5-Year Cumulative FCF", "₹7,200 Cr", "Strong cash generation")

st.divider()

# Main Charts
tab1, tab2, tab3 = st.tabs(["📈 Revenue & Profit Trends", "🧩 Segment Performance", "📊 Scenario Analysis"])

with tab1:
    col_left, col_right = st.columns(2)
    
    with col_left:
        fig1 = px.bar(x=years, y=revenue, title="Revenue Growth (10% CAGR)", 
                      labels={'x': 'Year', 'y': 'Revenue (₹ Cr)'}, color_discrete_sequence=['#1F4E79'])
        fig1.add_trace(go.Scatter(x=years, y=revenue, mode='lines+markers', 
                                  line=dict(color='#2E7D32', width=3), name='Trend'))
        st.plotly_chart(fig1, use_container_width=True)
    
    with col_right:
        fig2 = px.line(x=years, y=pat, title="Profit After Tax (PAT) Growth", 
                       labels={'x': 'Year', 'y': 'PAT (₹ Cr)'}, markers=True)
        fig2.update_traces(line_color='#2E7D32', line_width=3)
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    segments = ['Ticketing', 'Catering + Rail Neer', 'Tourism']
    fy25_share = [30.5, 53.5, 16.0]
    fy30_share = [27.3, 53.6, 19.1]
    
    col1, col2 = st.columns(2)
    with col1:
        fig_pie1 = px.pie(values=fy25_share, names=segments, title="FY25 Revenue Mix",
                          color_discrete_sequence=['#1F4E79', '#2E7D32', '#FF6B35'])
        st.plotly_chart(fig_pie1, use_container_width=True)
    
    with col2:
        fig_pie2 = px.pie(values=fy30_share, names=segments, title="FY30 Revenue Mix (Projected)",
                          color_discrete_sequence=['#1F4E79', '#2E7D32', '#FF6B35'])
        st.plotly_chart(fig_pie2, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>Key Insight:</b> Tourism share is expected to grow from 16% → 19.1% by FY30 — 
    the main growth driver. Ticketing remains the profit engine despite lower revenue share.
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.subheader("Scenario Analysis: FY30 PAT Impact")
    
    scenarios = pd.DataFrame({
        'Scenario': ['Base Case', 'Bull Case', 'Bear Case'],
        'FY30 PAT (₹ Cr)': [2006, 2350, 1650],
        'EBITDA Margin': ['38.3%', '41.0%', '34.5%'],
        '5-Year FCF (₹ Cr)': [7200, 8100, 6100]
    })
    
    st.dataframe(scenarios, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <b>Investment Thesis:</b> Even in the Bear Case, IRCTC delivers 8%+ PAT CAGR and positive free cash flow every year. 
    The business has a strong moat in Ticketing and significant upside from Tourism execution.
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.caption("**Prepared by:** Kartik Rao | MBA Finance, Class of 2026 | Portfolio Project | April 2026")
st.caption("This is a dummy interactive version created for demonstration. Real model built in Excel + Power BI.")

# Run instructions
if __name__ == "__main__":
    pass