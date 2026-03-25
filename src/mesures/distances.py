import numpy as np
from itertools import combinations
from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux

"""Question 8"""


def hamming_distance(avk, avl):
    dist = np.sum(avk != avl)
    return dist


def spearman_distance(rvk, rvl):
    dist = np.abs(np.argsort(rvk) - np.argsort(rvl))
    return np.sum(dist)
