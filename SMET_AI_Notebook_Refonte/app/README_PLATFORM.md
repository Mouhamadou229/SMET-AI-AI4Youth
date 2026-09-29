# SMET-AI Platform (UI nuit)

## Lancer
Place les modeles a la racine du projet:
```
SMET_AI_Platform/
  models/model_clinical.pkl
  models/model_full.pkl
  app/app.py
  app/pages/...
```

```bash
cd SMET_AI_Platform
python -m streamlit run app/app.py
```

## Ameliorations vs version Anselme
- Theme bleu nuit / noir
- Hero anime (degrade + orb)
- Stats avec hover
- Services en cartes <details> (clic pour ouvrir, pas tout affiche d'un coup)
- Resultat diagnostic avec animation d'apparition
