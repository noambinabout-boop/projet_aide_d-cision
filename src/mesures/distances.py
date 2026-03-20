import numpy as np
from itertools import combinations
from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux

"""Question 8"""


def hamming_distance(avk, avl):
    dist = np.sum(avk != avl)
    return dist


def r(v, i):
    return np.where(v == i)[0][0]


def spearman_distance(rvk, rvl):
    dist = 0
    m = rvk.shape[0]
    for i in range(m):
        dist += np.abs(r(rvk, i) - r(rvl, i))
    return dist
