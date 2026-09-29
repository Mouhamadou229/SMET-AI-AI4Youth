# SMET-AI — Refonte scientifique (AI4Youth 2026)

## Message central
Dans une cohorte hospitalière béninoise (n=102, prévalence IDF 62,7 %),
l'ajout du **rapport TG/HDL-C** aux variables cliniques améliore la discrimination
du syndrome métabolique. Preuve de concept pour un biomarqueur accessible de
**profilage / dépistage potentiel** — pas un dispositif médical validé.

## Résultats clés (notebook Colab exécuté)
| Bras | AUC-CV5 |
|------|---------|
| A Clinical only | 0.810 ± 0.054 |
| B Clinical + TG/HDL | 0.871 ± 0.056 |
| C Clinical + Lab | 0.924 ± 0.069 |

ΔAUC (B−A) ≈ +0.062

Sur B : Logistic Regression ≈ 0.885 · GB ≈ 0.871 · RF ≈ 0.852

## Fichier principal
`SMET_AI_Notebook_Refonte.ipynb`

## Exécution Colab
1. Upload `smet_benin_102patients_clean.csv`
2. Runtime → Run all
3. Télécharger le .ipynb + figures

## Ce qui a changé vs version précédente
- Narratif dépistage / santé publique (pas « meilleur modèle »)
- Section biomarqueur univarié
- Retrait de pression_pulsee (redondance)
- Bootstrap ΔAUC, calibration, Brier, Youden exploratoire
- Coefficients LR + permutation importance
- Roadmap de validation + limites renforcées
