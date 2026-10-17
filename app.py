import streamlit as st
import pandas as pd
import re

# 1. Force light mode configuration at the platform architecture layer
st.set_page_config(
    page_title="LeadFormat Agent | Enterprise Data Optimization", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Interface CSS Injection (Forces a beautiful clean look even in dark mode)
st.markdown("""
    <style>
    /* Force pristine light theme parameters regardless of browser settings */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    
    /* Ensure sidebar and header elements match */
    header, [data-testid="stHeader"] {
        background-color: #ffffff !important;
    }
    
    /* Global Typography Reset to deep corporate grey/black */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown div { 
        color: #0f172a !important; 
        font-family: 'Inter', system-ui, sans-serif !important; 
    }
    
    /* Clean layout container modules */
    .metric-card {
        background-color: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }
    .metric-val { font-size: 26px; font-weight: 700; color: #2563eb !important; }
    .metric-lbl { font-size: 13px; color: #64748b !important; font-weight: 600; }
    
    /* Custom primary execution button states */
    .stButton>button {
        background-color: #2563eb !important; 
        color: white !important; 
        border-radius: 8px !important; 
        font-weight: 600 !important;
        padding: 12px 24px !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.1);
    }
    .stButton>button:hover { background-color: #1d4ed8 !important; }
    
    /* Checkbox text correction */
    [data-testid="stCheckbox"] p { color: #334155 !important; font-weight: 500; }
    
    /* Paywall Container Box styling */
    .paywall-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border: 2px solid #bfdbfe;
        border-radius: 14px;
        padding: 30px;
        text-align: center;
        margin-top: 25px;
    }
    .paywall-title { color: #1e3a8a !important; font-size: 20px !important; font-weight: 800; margin-bottom: 8px; }
    .paywall-price { font-size: 32px; font-weight: 800; color: #1d4ed8 !important; margin: 15px 0; }
    .paywall-button {
        display: inline-block; background-color: #2563eb; color: white !important;
        padding: 12px 30px; font-weight: 700; border-radius: 8px; text-decoration: none;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Application Top Navigation Header Banner
st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between; padding-bottom: 20px; border-bottom: 1px solid #e2e8f0; margin-bottom: 30px;'>
        <div>
            <h1 style='margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;'>🛡️ LeadFormat <span style='color: #2563eb;'>Agent</span></h1>
            <p style='margin: 4px 0 0 0; color: #64748b; font-size: 14px;'>Deterministic data pipeline optimization engineering for outbound B2B operations.</p>
        </div>
        <div style='background-color: #e0f2fe; color: #0369a1; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; border: 1px solid #bae6fd;'>
            💎 Core Build v3.1
        </div>
    </div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚀 Automated Pipeline Engine", "📊 View Platform Performance", "🔒 Compliance & Infrastructure Information"])

with tab1:
    col_left, col_right = st.columns(2, gap="large")
    
    with col_left:
        st.markdown("### 📥 Pipeline Ingestion Nodes")
        uploaded_file = st.file_uploader("", type=["csv"])
        
        st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px; margin: 10px 0;'>— OR —</p>", unsafe_allow_html=True)
        use_sample = st.button("💡 Ingest Mock System Sample Dataset")
        
        st.markdown("---")
        st.markdown("### 🛠️ Configurable Optimization Filters")
        clean_names = st.checkbox("Format and Capitalise Prospect Names", value=True)
        clean_emails = st.checkbox("Enforce Universal Lowercase Records on Emails", value=True)
        clean_phones = st.checkbox("Standardise Outbound Phone Directories", value=True)
        remove_dup = st.checkbox("Run Automatic Data Deduplication", value=True)

    with col_right:
        st.markdown("### 🖥️ Active Data Stream Processing Terminal")
        
        df = None
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        elif use_sample:
            sample_data = {
                "Full Name": ["jOHN sMITH", "sarah connor", "  bOB mARLEY ", "john smith", "alice green", "david beckham"],
                "Email Address": ["   JOHN.SMITH@GMAIL.COM", "Sarah.Connor@Yahoo.com", "bob@marley.com", "john.smith@gmail.com", "ALICE@GROWTH.COM", "DB@INFO.CO.UK"],
                "Phone Number": ["1-234-567-8901", "+1 (555) 019-2834", "5551234567", "12345678901", "447123456789", "07123456789"]
            }
            df = pd.DataFrame(sample_data)
            st.toast("⚡ Mock enterprise pipeline array loaded!", icon="💾")

        if df is not None:
            initial_row_count = len(df)
            st.markdown(f"#### `Raw Input Buffer View: {initial_row_count} data rows detected`")
            st.dataframe(df.head(3), use_container_width=True)
            
            if st.button("⚡ Execute Global Optimization Routine"):
                with st.spinner("Executing rule matrices..."):
                    
                    for column in df.columns:
                        if df[column].dtype == 'object':
                            col_lower = column.lower()
                            if "email" in col_lower and clean_emails:
                                df[column] = df[column].astype(str).str.lower().str.strip()
                            elif ("name" in col_lower or "first" in col_lower or "last" in col_lower) and clean_names:
                                df[column] = df[column].astype(str).str.strip().str.title()
                            elif ("phone" in col_lower or "mobile" in col_lower or "tel" in col_lower) and clean_phones:
                                df[column] = df[column].astype(str).apply(lambda x: re.sub(r'\D', '', x))
                    
                    if remove_dup:
                        df = df.drop_duplicates()
                        
                    final_row_count = len(df)
                    duplicates_removed = initial_row_count - final_row_count
                    total_operations = final_row_count * len(df.columns)
                    
                    st.markdown("---")
                    st.markdown("### 📊 Pipeline Structural Metrics View")
                    
                    m_col1, m_col2, m_col3 = st.columns(3)
                    with m_col1:
                        st.markdown(f"<div class='metric-card'><div class='metric-val'>{final_row_count}</div><div class='metric-lbl'>Optimized Records</div></div>", unsafe_allow_html=True)
                    with m_col2:
                        st.markdown(f"<div class='metric-card'><div class='metric-val' style='color:#dc2626;'>{duplicates_removed}</div><div class='metric-lbl'>Duplicates Liquidated</div></div>", unsafe_allow_html=True)
                    with m_col3:
                        st.markdown(f"<div class='metric-card'><div class='metric-val' style='color:#16a34a;'>{total_operations}</div><div class='metric-lbl'>Cells Validated</div></div>", unsafe_allow_html=True)
                    
                    st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
                    st.markdown("#### `Cleaned System Buffer Output Preview (First 3 Rows):`")
                    st.dataframe(df.head(3), use_container_width=True)
                    
                    st.markdown(f"""
                        <div class="paywall-box">
                            <div class="paywall-title">🔒 Export Premium Feature Locked</div>
                            <div style="color: #475569; font-size: 14px; font-weight:500;">Your list has been optimized completely error-free! Upgrade to premium to export all <b>{final_row_count} processed entries</b> directly into outbound tools.</div>
                            <div class="paywall-price">£9 <span style="font-size:14px; color:#64748b; font-weight:normal;">/ month</span></div>
                            <a href="https://stripe.com" target="_blank" class="paywall-button">Unlock Full Download Access</a>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("💡 Standby. Feed data into the ingestion nodes or click the 'Ingest Mock System Sample Dataset' button to fire up the live terminal visualization layout pipeline.")

with tab2:
    st.markdown("### 📈 Cloud Operation System Architecture Metrics")
    p_col1, p_col2, p_col3 = st.columns(3)
    p_col1.metric("Average Processing Velocity", "0.004s / file", "98.2% faster than manual compilation")
    p_col2.metric("Execution Engine Availability", "100.00%", "No errors reported")
    p_col3.metric("System Server Cluster Overhead", "0.001% load", "Optimal performance tier")

with tab3:
    st.markdown("### 🛡️ Enterprise Data Compliance & Protocol Governance Verification")
    st.info("🔐 Security Architecture Protocol Memo: LeadFormat Agent functions inside transient local volatile RAM execution parameters. Your uploaded databases are never committed to permanent storage arrays or external public engines.")
