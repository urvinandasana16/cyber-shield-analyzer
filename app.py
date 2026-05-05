import streamlit as st
import whois
import socket
import requests
from datetime import datetime
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Cyber Shield Analyzer", page_icon="🛡️", layout="wide")

# --- PROFESSIONAL DARK THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@400;600&display=swap');
    
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Neon Header */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: #00d4ff;
        text-align: center;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        font-size: 2.8rem !important;
        margin-bottom: 0px;
    }

    /* Professional Cards */
    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        transition: 0.3s ease;
    }
    .metric-card:hover {
        border-color: #58a6ff;
        transform: translateY(-5px);
    }

    /* Status Row Style (Table Fix) */
    .status-row {
        display: flex;
        justify-content: space-between;
        padding: 12px 15px;
        background: #1c2128;
        border: 1px solid #30363d;
        border-radius: 8px;
        margin-bottom: 8px;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #30363d;
    }

    /* Glowing Button */
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff, #0056b3);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px;
        font-weight: bold;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Clean & Professional) ---
with st.sidebar:
    st.markdown("<h2 style='color: #00d4ff;'>🛡️ CyberShield</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### **Developer Profile**")
    st.info("**Name:** Urvi\n\n**Expertise:** Cybersecurity & IT")
    st.markdown("---")
    st.markdown("#### 🎯 **Focus**")
    st.write("Vulnerability Assessment & Network Intelligence.")
    st.markdown("---")
    st.success("Scanner Engine: v3.0 Active")

# --- MAIN UI ---
st.markdown("<h1 class='main-title'>CYBER SHIELD ANALYZER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-bottom: 40px;'>Professional Infrastructure Security Diagnostics</p>", unsafe_allow_html=True)

target_url = st.text_input("🌐 Enter Target URL for Analysis", placeholder="https://example.com")

if st.button("RUN SECURITY AUDIT"):
    if target_url:
        with st.spinner("Analyzing target infrastructure..."):
            domain = target_url.replace("https://", "").replace("http://", "").split('/')[0]
            
            try:
                ip_addr = socket.gethostbyname(domain)
                res = requests.get(target_url, timeout=5)
                is_secure = target_url.startswith("https://")
                
                # --- EXECUTIVE METRICS ---
                st.markdown("### 📊 Executive Telemetry")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Security</p><h2 style="color:{"#238636" if is_secure else "#da3633"}; margin:0;">{"ENCRYPTED" if is_secure else "UNSECURE"}</h2></div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Target IP</p><h2 style="color:#58a6ff; margin:0;">{ip_addr}</h2></div>', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'<div class="metric-card"><p style="color:#8b949e; margin:0;">Latency</p><h2 style="color:#f2cc60; margin:0;">{res.elapsed.total_seconds():.3f}s</h2></div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # --- SCAN ANALYSIS ---
                left, right = st.columns(2)
                
                with left:
                    st.markdown("### 🔍 Risk Profile")
                    try:
                        w = whois.whois(domain)
                        creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
                        years = (datetime.now() - creation).days // 365
                        st.markdown(f'<div class="status-row"><span>Domain Longevity</span><span style="color:#238636;">{years} Years</span></div>', unsafe_allow_html=True)
                    except:
                        st.markdown('<div class="status-row"><span>Domain Data</span><span style="color:#da3633;">Privacy Protected</span></div>', unsafe_allow_html=True)
                    
                    status_text = "Secure Connection" if is_secure else "Insecure HTTP"
                    status_color = "#238636" if is_secure else "#da3633"
                    st.markdown(f'<div class="status-row"><span>Protocol Check</span><span style="color:{status_color};">{status_text}</span></div>', unsafe_allow_html=True)

                with right:
                    st.markdown("### 🕸️ Network Entry Points")
                    ports = {21: "FTP", 22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "Proxy"}
                    for p, n in ports.items():
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.5)
                        is_open = s.connect_ex((ip_addr, p)) == 0
                        s.close()
                        
                        color = "#da3633" if is_open else "#238636"
                        status_label = "OPEN 🚨" if is_open else "Secure ✅"
                        
                        st.markdown(f"""
                            <div class="status-row">
                                <span><b>{n}</b> (Port {p})</span>
                                <span style="color:{color}; font-weight:bold;">{status_label}</span>
                            </div>
                        """, unsafe_allow_html=True)

                st.markdown("---")
                st.markdown("### 📝 Conclusion")
                if not is_secure:
                    st.error("Action Required: Targeted infrastructure lacks SSL encryption. High risk of MITM attacks.")
                else:
                    st.success("Audit Complete: No critical surface-level protocol vulnerabilities detected.")

            except Exception as e:
                st.error(f"Critical System Failure: Target host unreachable.")
    else:
        st.warning("Please input a URL for intelligence gathering.")

st.markdown("<p style='text-align: center; opacity: 0.3; margin-top: 50px;'>Cyber Shield Analyzer | Enterprise Edition</p>", unsafe_allow_html=True)