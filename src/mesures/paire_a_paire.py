from itertools import combinations
import numpy as np


def distances_pp_appro(vote):
    n, m = vote.shape
    indices = np.arange(m)
    distances = np.zeros((m, m), dtype=int)

    # Boucle pour chaque votante
    for votante in range(n):
        # On boucle sur toutes les paires possibles sans répétition
        votante_actuelle = vote[votante, :]

        for ck, cl in combinations(indices, 2):
            # votantes qui preferent ck à cl
            pref_ck_cl = (votante_actuelle[ck] == 1) & (votante_actuelle[cl] == 0)
            nb_pref_ck_cl = 1 if pref_ck_cl else 0

            # votantes qui preferent cl à ck
            pref_cl_ck = (votante_actuelle[cl] == 1) & (votante_actuelle[ck] == 0)
            nb_pref_cl_ck = 1 if pref_cl_ck else 0

            distances[ck][cl] += abs(nb_pref_ck_cl - nb_pref_cl_ck)
            distances[cl][ck] += abs(nb_pref_cl_ck - nb_pref_ck_cl)

    return distances


def distance_pp_ordre_totaux(vote):
    n, m = vote.shape
    indices = np.arange(m)
    distances = np.zeros((m, m), dtype=int)

    for votante in range(n):
        votante_actuelle = vote[votante, :]

        # On boucle sur toutes les paires possibles sans répétition
        for ck, cl in combinations(indices, 2):

            # Pour chaque bulletin, on regarde les emplacements des candidates
            indices_ck = np.where(votante_actuelle == ck)[0][0]
            indices_cl = np.where(votante_actuelle == cl)[0][0]

            # On regarde quelle candidate est mieux placée sur un bulletin précis
            if indices_ck < indices_cl:
                distances[ck][cl] += 1
                distances[cl][ck] -= 1
            elif indices_cl < indices_ck:
                distances[cl][ck] += 1
                distances[ck][cl] -= 1

    return np.abs(distances)
