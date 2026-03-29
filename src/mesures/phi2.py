import numpy as np
from itertools import combinations
from math import comb

"""Question 5"""


def phi_2_appro(vote, distances):
    n, m = vote.shape
    indices = np.arange(m)
    phi2 = 0

    # Formule donnée dans l'énoncé
    for ck, cl in combinations(indices, 2):
        calc = (n - distances[ck][cl])/(n * comb(m, 2))
        phi2 += calc

    return phi2


def phi_2_ordre_totaux(vote, distances):
    n, m = vote.shape
    indices = np.arange(m)
    phi2 = 0

    # Formule donnée dans l'énoncé
    for ck, cl in combinations(indices, 2):
        calc = (n - distances[ck][cl])/(n * comb(m, 2))
        phi2 += calc

    return phi2

