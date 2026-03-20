import numpy as np
from scipy.optimize import linear_sum_assignment
from distances import hamming_distance, spearman_distance, r
from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux


def u1_appro_calcul(vote):
    n, m = vote.shape
    approuvee = np.sum(vote, axis=0)
    # On prend le minimum entre le nombre de personne désapprouvant et approuvant une candidate
    mini = np.minimum(approuvee, n-approuvee)
    return np.sum(mini)


def u1_totaux_calcul(vote):
    # Matrice de coûts (m x m)
    # cout[i][j] = coût d'assigner le rang j+1 à la candidate i
    n, m = vote.shape
    couts = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            for k in range(n):
                couts[i][j] += np.abs(j - r(vote[k, :], i))

    row_ind, col_ind = linear_sum_assignment(couts)
    print(col_ind)  # [0, 1, 2] → c1→rang1, c2→rang2, c3→rang3
    return couts[row_ind, col_ind].sum()  # u1* = 1


vote = creation_vote_ordre_totaux(8, 6, 1)
print(vote)
print(u1_totaux_calcul(vote))
