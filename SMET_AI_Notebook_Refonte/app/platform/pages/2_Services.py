"""Services"""
import streamlit as st
from pathlib import Path
from PIL import Image

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ip = ASSETS / "protection.png"
page_icon = Image.open(ip) if ip.exists() else "🤝"

st.set_page_config(page_title="SMET-AI · Services", page_icon=page_icon,
                   layout="centered", initial_sidebar_state="expanded")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"], .stApp { font-family: 'Inter', system-ui, sans-serif !important; }
.stApp {
  background: radial-gradient(ellipse at 15% 0%, #132337 0%, #0B1220 50%, #070B14 100%) !important;
  color: #E2E8F0 !important;
}
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0F172A 0%, #0B1220 100%) !important;
  border-right: 1px solid #1E293B !important;
}
section[data-testid="stSidebar"] * { color: #CBD5E1 !important; }
h1, h2, h3, h4 { color: #F1F5F9 !important; letter-spacing: -0.02em; }
p, label, .stCaption, .stMarkdown p { color: #94A3B8 !important; }
.smet-hero {
  position: relative; overflow: hidden;
  background: linear-gradient(135deg, #0EA5E9 0%, #0369A1 45%, #0F766E 100%);
  background-size: 200% 200%;
  animation: gradientMove 12s ease infinite, fadeUp 0.7s ease both;
  border-radius: 18px; padding: 1.5rem 1.4rem; color: white !important;
  margin-bottom: 1.3rem; box-shadow: 0 16px 40px rgba(14,165,233,0.15);
}
.smet-hero h1 { color: white !important; margin: 0; font-size: 1.8rem; font-weight: 700; }
.smet-hero p { color: rgba(255,255,255,0.9) !important; margin: 0.35rem 0 0 0; font-size: 0.92rem; }
.smet-hero::after {
  content: ''; position: absolute; width: 160px; height: 160px;
  right: -40px; top: -40px; background: rgba(255,255,255,0.08);
  border-radius: 50%; animation: floatOrb 8s ease-in-out infinite;
}
@keyframes gradientMove {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes floatOrb {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(12px); }
}
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes pulseSoft {
  0%, 100% { box-shadow: 0 0 0 0 rgba(14,165,233,0.2); }
  50% { box-shadow: 0 0 0 8px rgba(14,165,233,0); }
}
.smet-stat {
  background: rgba(15,23,42,0.9); border: 1px solid #1E293B;
  border-radius: 16px; padding: 1.1rem 0.8rem; text-align: center;
  animation: fadeUp 0.6s ease both;
  transition: transform 0.2s ease, border-color 0.2s ease;
}
.smet-stat:hover { transform: translateY(-3px); border-color: #0EA5E9; }
.smet-stat h3 { color: #38BDF8 !important; font-size: 1.7rem; margin: 0; font-weight: 700; }
.smet-stat span { color: #94A3B8 !important; font-size: 0.78rem; }
.smet-service {
  background: rgba(15,23,42,0.92); border: 1px solid #1E293B;
  border-radius: 14px; padding: 0; margin-bottom: 10px; overflow: hidden;
  animation: fadeUp 0.5s ease both;
  transition: border-color 0.2s ease, transform 0.2s ease;
}
.smet-service:hover { border-color: #0EA5E9; transform: translateX(3px); }
.smet-service summary {
  list-style: none; cursor: pointer; padding: 0.9rem 1.05rem;
  color: #F1F5F9 !important; font-weight: 600;
  display: flex; justify-content: space-between; align-items: center;
}
.smet-service summary::-webkit-details-marker { display: none; }
.smet-service summary::after {
  content: '›'; color: #38BDF8; font-size: 1.3rem;
  transition: transform 0.25s ease;
}
.smet-service[open] summary::after { transform: rotate(90deg); }
.smet-service .body {
  padding: 0 1.05rem 0.95rem 1.05rem; color: #94A3B8 !important;
  border-top: 1px solid #1E293B; animation: fadeUp 0.3s ease both;
  font-size: 0.9rem;
}
.smet-result {
  background: rgba(15,23,42,0.95); border-radius: 16px;
  padding: 1.35rem 1.25rem; border: 1px solid #1E293B;
  animation: fadeUp 0.4s ease both, pulseSoft 2.2s ease 1;
  margin: 1rem 0; text-align: center;
}
.smet-result .proba {
  font-size: 2.7rem; font-weight: 700; color: #38BDF8 !important; margin: 0.1rem 0;
  letter-spacing: -0.03em;
}
.badge-high { color: #FCA5A5 !important; }
.badge-mod { color: #FCD34D !important; }
.badge-low { color: #86EFAC !important; }
div.stButton > button[kind="primary"] {
  background: linear-gradient(90deg, #0369A1, #0EA5E9) !important;
  border: none !important; border-radius: 12px !important;
  font-weight: 600 !important; color: white !important;
  box-shadow: 0 8px 22px rgba(14,165,233,0.22) !important;
}
hr { border-color: #1E293B !important; }
div[data-testid="stAlert"] {
  background: rgba(15,23,42,0.9) !important;
  border: 1px solid #334155 !important; color: #CBD5E1 !important;
}
a[data-testid="stPageLink-NavLink"] {
  background: rgba(15,23,42,0.9) !important;
  border: 1px solid #1E293B !important; border-radius: 12px !important;
  padding: 0.8rem 1rem !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="smet-hero">
  <h1>Services</h1>
  <p>Trois bras d'estimation du risque</p>
</div>
""", unsafe_allow_html=True)

services = [
    ("A — Evaluation clinique seule",
     "Age, sexe, tension, tour de taille. Utile quand le bilan n'est pas disponible."),
    ("B — Clinique + rapport TG/HDL-C",
     "Ajoute le biomarqueur etudie dans le memoire. Mesure le gain predictif du ratio."),
    ("C — Clinique + bilan complet",
     "Glycemie et lipides complets. Performance plus haute, circularite partielle a discuter."),
    ("Score interpretable",
     "Probabilite + profil FAIBLE / MODERE / ELEVE."),
    ("Aide a la decision",
     "Ne remplace pas l'avis d'un professionnel de sante."),
]
for i, (t, d) in enumerate(services):
    st.markdown(
        f'<details class="smet-service" style="animation-delay:{0.07*i}s">'
        f'<summary>{t}</summary><div class="body">{d}</div></details>',
        unsafe_allow_html=True,
    )
st.write("")
st.page_link("pages/1_Diagnostic.py", label="Aller au diagnostic", icon="🩺")
