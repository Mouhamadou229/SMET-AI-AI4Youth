"""
SMET-AI — Entraînement 3 modèles (diagnostic IDF corrigé 64/38 = 62,7 %)
"""
from pathlib import Path
import pickle
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier

RANDOM_STATE = 42
BASE = Path(__file__).resolve().parent
DATA_PATH = BASE / "data" / "smet_benin_102patients_clean.csv"
MODEL_DIR = BASE / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
assert int((df["smet"] == 1).sum()) == 64, "Attendu 64 SMet+ (prévalence 62,7 %)"

FEATURES_A = ["age", "sexe_num", "pas", "pad", "pression_pulsee", "tour_taille"]
FEATURES_B = FEATURES_A + ["rapport_tg_hdl_mmol"]
FEATURES_C = FEATURES_A + [
    "glycemie_mmol", "cholesterol_total_mmol", "hdl_c_mmol", "ldl_c_mmol",
    "triglycerides_mmol", "rapport_tg_hdl_mmol",
]
y = df["smet"]

def make_pipe():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", GradientBoostingClassifier(
            n_estimators=100, max_depth=3, random_state=RANDOM_STATE
        )),
    ])

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
configs = [
    ("A", "Clinical-only", FEATURES_A, "model_clinical.pkl"),
    ("B", "Clinical + TG/HDL", FEATURES_B, "model_tg_hdl.pkl"),
    ("C", "Clinical + Lab complet", FEATURES_C, "model_full.pkl"),
]

print("SMET-AI | n=102 | SMet+=64 | SMet-=38 | prévalence 62,7 %")
print("-" * 56)
for code, name, feats, fname in configs:
    X = df[feats]
    pipe = make_pipe()
    auc = cross_val_score(pipe, X, y, cv=cv, scoring="roc_auc").mean()
    pipe.fit(X, y)
    with open(MODEL_DIR / fname, "wb") as f:
        pickle.dump({
            "pipeline": pipe, "features": feats, "name": name,
            "code": code, "auc_cv5": float(auc), "prevalence": 0.627,
        }, f)
    print(f"[{code}] {name:28s} AUC-CV5 = {auc:.3f}")
print("Modèles sauvegardés dans", MODEL_DIR)
