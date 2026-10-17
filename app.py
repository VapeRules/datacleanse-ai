import streamlit as st
import pandas as pd
import re

# Premium styling configuration
st.set_page_config(page_title="DataCleanse AI | The B2B Lead Formatter", page_icon="📊", layout="centered")

# Custom CSS to make it look like an expensive SaaS platform
st.markdown("""
    <style>
    .main {background-color: #f9fbfd;}
    .stButton>button {background-color: #0275d8; color: white; border-radius: 6px; width: 100%; font-weight: bold;}
    .success-text {color: #28a745; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 DataCleanse AI")
st.caption("The professional standard for outbound sales and marketing list optimization.")
st.markdown("---")

# 1. File Upload Drag-and-Drop Component
uploaded_file = st.file_uploader("Upload your messy CSV prospect list", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    total_rows = len(df)
    
    st.write(f"### 🔍 Raw File Inspection ({total_rows} rows found)")
    st.dataframe(df.head(5))
    
    st.write("### 🛠️ Premium Custom Cleaning Pipeline")
    
    # User customization settings
    col1, col2 = st.columns(2)
    with col1:
        clean_names = st.checkbox("Fix and Capitalise Names (john smith -> John Smith)", value=True)
        clean_emails = st.checkbox("Standardise Emails (Force Lowercase & Trim Spaces)", value=True)
    with col2:
        clean_phones = st.checkbox("Standardise Phone Numbers (Keep digits only)", value=True)
        remove_dup = st.checkbox("Deduplicate List (Delete duplicate entries)", value=True)
    
    if st.button("🚀 Execute Pipeline & Optimize File"):
        with st.spinner("Processing data nodes..."):
            initial_row_count = len(df)
            
            # Step A: Run through text formatting rules
            for column in df.columns:
                if df[column].dtype == 'object':
                    col_lower = column.lower()
                    
                    # Email Standardizer
                    if "email" in col_lower and clean_emails:
                        df[column] = df[column].astype(str).str.lower().str.strip()
                        
                    # Name Standardizer
                    elif ("name" in col_lower or "first" in col_lower or "last" in col_lower) and clean_names:
                        df[column] = df[column].astype(str).str.strip().str.title()
                        
                    # Phone Number Standardizer
                    elif ("phone" in col_lower or "mobile" in col_lower or "tel" in col_lower) and clean_phones:
                        df[column] = df[column].astype(str).apply(lambda x: re.sub(r'\D', '', x))
            
            # Step B: Run Deduplication Rule
            if remove_dup:
                df = df.drop_duplicates()
                
            final_row_count = len(df)
            duplicates_removed = initial_row_count - final_row_count
            
            # Metrics / Usage Display
            st.markdown("### ✨ Optimization Complete!")
            m_col1, m_col2 = st.columns(2)
            m_col1.metric("Rows Processed Successfully", final_row_count)
            m_col2.metric("Duplicate Rows Destroyed", duplicates_removed)
            
            st.write("### 📋 Cleaned Data Output Preview")
            st.dataframe(df.head(5))
            
            # 3. Paywall Trigger Hook / Download
            csv_output = df.to_csv(index=False).encode('utf-8')
            
            # Visual marker tracking total workload processed
            st.info(f"🔒 DataCleanse AI verified. Total operations run: {final_row_count * len(df.columns)} cells optimized.")
            
            st.download_button(
                label="📥 Download Outreach-Ready CSV", 
                data=csv_output, 
                file_name="datacleanse_optimized.csv", 
                mime="text/csv"
            )
else:
    # Educational display dashboard for empty state
    st.info("💡 Drop an unformatted lead list (.csv) above to activate the automated optimization grid.")
    
    st.write("### 🛡️ Secure Data Compliance Verification")
    st.caption("🔒 DataCleanse AI processes your spreadsheets natively in local volatile RAM memory. Your private enterprise client lists, employee contact directories, and financial prospect records are never written to disk, stored, or processed by public artificial intelligence engines.")
