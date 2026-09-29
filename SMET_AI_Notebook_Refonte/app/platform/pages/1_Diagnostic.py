"""SMET-AI Diagnostic — 3 modes A/B/C (labels corrigees 62.7%)"""
import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
from PIL import Image

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ip = ASSETS / "protection.png"
page_icon = Image.open(ip) if ip.exists() else "🩺"

st.set_page_config(page_title="SMET-AI · Diagnostic", page_icon=page_icon,
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
  <h1>Diagnostic</h1>
  <p>3 modeles · Clinical · Clinical+TG/HDL · Clinical+Lab · prevalence 62,7 %</p>
</div>
""", unsafe_allow_html=True)

MODEL_DIR = Path(__file__).resolve().parent.parent.parent / "models"
if not MODEL_DIR.exists():
    MODEL_DIR = Path(__file__).resolve().parent.parent / "models"

@st.cache_resource
def load_models():
    out = {}
    for key, fname in [
        ("A", "model_clinical.pkl"),
        ("B", "model_tg_hdl.pkl"),
        ("C", "model_full.pkl"),
    ]:
        with open(MODEL_DIR / fname, "rb") as f:
            out[key] = pickle.load(f)
    return out

try:
    models = load_models()
except Exception as e:
    st.error("Modeles manquants. Lance : python train_models.py")
    st.code(str(e))
    st.stop()

st.sidebar.header("Modele")
mode_label = st.sidebar.radio(
    "Choix du bras",
    [
        "A — Clinique uniquement",
        "B — Clinique + TG/HDL (memoire)",
        "C — Clinique + Lab complet",
    ],
)
code = mode_label[0]
st.sidebar.info(
    "A = sans labo\n"
    "B = biomarqueur TG/HDL\n"
    "C = bilan complet (circularite partielle)\n"
    "Prevalence corrigee 62,7 % (64/38)"
)

st.subheader("Parametres patient")
c1, c2 = st.columns(2)
with c1:
    age = st.number_input("Age (annees)", 18, 100, 52)
    sexe = st.selectbox("Sexe", ["Homme", "Femme"])
    tour_taille = st.number_input("Tour de taille (cm)", 50.0, 180.0, 98.0, 0.5)
    pas = st.number_input("PAS (mmHg)", 80, 250, 136)
    pad = st.number_input("PAD (mmHg)", 40, 150, 88)
with c2:
    if code == "A":
        st.info("Mode A : aucun bilan requis.")
        tg = hdl = glycemie = ct = ldl = None
    elif code == "B":
        st.caption("Mode B — biomarqueur memoire")
        tg = st.number_input("Triglycerides (mmol/L)", 0.2, 15.0, 1.2, 0.1)
        hdl = st.number_input("HDL-C (mmol/L)", 0.2, 4.0, 1.1, 0.05)
        glycemie = ct = ldl = None
        if hdl and hdl > 0:
            st.metric("Rapport TG/HDL-C", f"{tg/hdl:.2f}")
    else:
        st.caption("Mode C — bilan complet")
        glycemie = st.number_input("Glycemie (mmol/L)", 2.0, 30.0, 5.1, 0.1)
        tg = st.number_input("Triglycerides (mmol/L)", 0.2, 15.0, 1.2, 0.1)
        hdl = st.number_input("HDL-C (mmol/L)", 0.2, 4.0, 1.1, 0.05)
        ldl = st.number_input("LDL-C (mmol/L)", 0.5, 8.0, 3.8, 0.1)
        ct = st.number_input("Cholesterol total (mmol/L)", 2.0, 12.0, 5.4, 0.1)
        if hdl and hdl > 0:
            st.metric("Rapport TG/HDL-C", f"{tg/hdl:.2f}")

sexe_num = 1 if sexe == "Femme" else 0
pression_pulsee = pas - pad

if st.button("Estimer le profil de risque", type="primary", use_container_width=True):
    m = models[code]
    feats = m["features"]
    pipe = m["pipeline"]

    row = {
        "age": age, "sexe_num": sexe_num, "pas": pas, "pad": pad,
        "pression_pulsee": pression_pulsee, "tour_taille": tour_taille,
    }
    if code in ("B", "C"):
        if hdl is None or hdl <= 0:
            st.error("HDL-C invalide")
            st.stop()
        row["rapport_tg_hdl_mmol"] = tg / hdl
    if code == "C":
        row.update({
            "glycemie_mmol": glycemie,
            "cholesterol_total_mmol": ct,
            "hdl_c_mmol": hdl,
            "ldl_c_mmol": ldl,
            "triglycerides_mmol": tg,
        })

    X = pd.DataFrame([row])[feats]
    proba = float(pipe.predict_proba(X)[0, 1])

    if proba >= 0.70:
        risk, badge = "ELEVE", "badge-high"
    elif proba >= 0.40:
        risk, badge = "MODERE", "badge-mod"
    else:
        risk, badge = "FAIBLE", "badge-low"

    auc_txt = f"{m.get('auc_cv5', 0):.3f}" if m.get("auc_cv5") is not None else "—"
    st.markdown(f"""
    <div class="smet-result">
      <div style="color:#64748B;font-size:0.85rem;">{m['name']} · AUC-CV {auc_txt}</div>
      <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.25rem;">Probabilite estimee (SMet)</div>
      <div class="proba">{proba*100:.1f}%</div>
      <div class="{badge}"><strong>Profil · {risk}</strong></div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(min(max(proba, 0.0), 1.0))

    with st.expander("Valeurs saisies"):
        st.write(f"Age {age} · {sexe} · TT {tour_taille} · {pas}/{pad}")
        if code in ("B", "C"):
            st.write(f"TG/HDL = {row.get('rapport_tg_hdl_mmol', 0):.2f}")

st.divider()
st.warning(
    "Proof-of-concept AI4Youth 2026 — pas un diagnostic medical. "
    "Diagnostic IDF corrige (64/38, prevalence 62,7 %). "
    "Modele C : circularite partielle assumee."
)
