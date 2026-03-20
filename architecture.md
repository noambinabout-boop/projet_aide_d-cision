# Architecture du Projet FMPAD — Analyse de la Polarisation

```
projet_fmpad/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── (profils générés sauvegardés si besoin)
│
├── src/
│   ├── __init__.py
│   │
│   ├── generation/
│   │   ├── __init__.py
│   │   ├── approval.py        # Q1 — génération profils An
│   │   └── ranking.py         # Q2 — génération profils Ln
│   │
│   ├── measures/
│   │   ├── __init__.py
│   │   ├── pairwise.py        # Q3 — calcul des d_{ck cl}(p)
│   │   ├── phi2.py            # Q5 — mesure phi2
│   │   ├── distances.py       # Q8 — dH et dS
│   │   ├── consensus.py       # Q10, Q11, Q12 — u*1 pour An et Ln
│   │   ├── kmeans.py          # Q13 — k-means adapté, ũ*2
│   │   └── phi_distance.py    # Q14 — phi_dH et phi_dS
│   │
│   └── utils/
│       ├── __init__.py
│       └── types.py           # types partagés : Profile, Ballot, etc.
│
├── plots/
│   ├── plot_phi2.py           # Q6  — courbes phi2
│   └── plot_phi_dist.py       # Q15 — courbes phi_dH et phi_dS
│
└── rapport/
    └── rapport.pdf            # rendu final
```

---

## Dependances entre fichiers

```
generation/approval.py  ──────────────────────────────────────┐
generation/ranking.py   ──────────────────────────────────────┤
                                                               ▼
measures/distances.py   ──────────────────────────────► measures/consensus.py
      │                                                        │
      │                                                        ▼
      │                                                 measures/kmeans.py
      │                                                        │
      └────────────────────────────────────────────────► measures/phi_distance.py
                                                               │
measures/pairwise.py ──► measures/phi2.py                      │
                              │                                │
                              ▼                                ▼
                         plots/plot_phi2.py        plots/plot_phi_dist.py
```

---

## Signatures principales

### src/generation/approval.py
```python
def generate_approval_profile(n: int, m: int, polarization: float) -> np.ndarray:
    # Retourne un tableau (n, m) de 0/1
    # polarization=0 -> tous identiques, polarization=1 -> moitié opposée
```

### src/generation/ranking.py
```python
def generate_ranking_profile(n: int, m: int, polarization: float) -> np.ndarray:
    # Retourne un tableau (n, m) de rangs (permutations de 1..m)
    # polarization=0 -> tous identiques, polarization=1 -> moitié miroir
```

### src/measures/pairwise.py
```python
def compute_pairwise_diffs_approval(profile: np.ndarray) -> dict:
    # Q3 — retourne {(ck, cl): d_ckcl} pour An

def compute_pairwise_diffs_ranking(profile: np.ndarray) -> dict:
    # Q3 — retourne {(ck, cl): d_ckcl} pour Ln
```

### src/measures/phi2.py
```python
def phi2_approval(profile: np.ndarray) -> float:
    # Q5 — calcule phi2(p) pour p dans An

def phi2_ranking(profile: np.ndarray) -> float:
    # Q5 — calcule phi2(p) pour p dans Ln
```

### src/measures/distances.py
```python
def hamming(a: np.ndarray, b: np.ndarray) -> int:
    # Q8 — distance de Hamming entre deux bulletins An

def spearman(r1: np.ndarray, r2: np.ndarray) -> int:
    # Q8 — distance de Spearman entre deux bulletins Ln
```

### src/measures/consensus.py
```python
def u1_approval(profile: np.ndarray) -> tuple[np.ndarray, float]:
    # Q10/Q12 — retourne (bulletin_consensus, valeur_u1)

def u1_ranking(profile: np.ndarray) -> tuple[np.ndarray, float]:
    # Q11/Q12 — via scipy.optimize.linear_sum_assignment
```

### src/measures/kmeans.py
```python
def kmeans_approval(profile: np.ndarray, n_restarts: int = 20) -> float:
    # Q13 — retourne u*2 estimé pour An

def kmeans_ranking(profile: np.ndarray, n_restarts: int = 20) -> float:
    # Q13 — retourne u*2 estimé pour Ln
```

### src/measures/phi_distance.py
```python
def phi_dH(profile: np.ndarray) -> float:
    # Q14 — phi_dH pour An

def phi_dS(profile: np.ndarray) -> float:
    # Q14 — phi_dS pour Ln
```

---

## requirements.txt
```
numpy
scipy
matplotlib
```

---

## Répartition en trinôme

| Membre   | Fichiers                                              | Questions rapport |
|----------|-------------------------------------------------------|-------------------|
| Membre 1 | generation/ + pairwise.py + phi2.py + plot_phi2.py   | Q1, Q2, Q4        |
| Membre 2 | distances.py + consensus.py                           | Q7, Q10, Q11      |
| Membre 3 | kmeans.py + phi_distance.py + plot_phi_dist.py        | Q9, Q15           |

README + section IA du rapport : a faire ensemble.
