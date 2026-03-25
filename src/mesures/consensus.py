import numpy as np
from scipy.optimize import linear_sum_assignment



def u1_appro_calcul(vote):
    n, m = vote.shape
    approuvee = np.sum(vote, axis=0)
    consensus = (approuvee > n/2).astype(int)
    # On prend le minimum entre le nombre de personne désapprouvant et approuvant une candidate
    mini = np.minimum(approuvee, n-approuvee)
    return np.sum(mini), consensus


def u1_totaux_calcul(vote):
    # Matrice de coûts (m x m)
    # cout[i][j] = coût d'assigner le rang j+1 à la candidate i
    n, m = vote.shape
    couts = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            for k in range(n):
                couts[i][j] += np.abs(j - np.argsort(vote[k, :])[i])

    row_ind, col_ind = linear_sum_assignment(couts)
    return couts[row_ind, col_ind].sum(), np.argsort(col_ind)


