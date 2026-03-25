import numpy as np
from src.mesures.distances import hamming_distance, spearman_distance
from src.mesures.consensus import u1_appro_calcul, u1_totaux_calcul


def kmeans_appro(vote):
    n, m = vote.shape
    a1_tilde = vote[np.random.randint(0, n), :]
    a2_tilde = vote[np.random.randint(0, n), :]

    ancien_group = np.zeros(n)

    max_iterations = 100  # au cas où la polarisation est 0
    while True:

        max_iterations -= 1
        if max_iterations < 0:
            return 0

        centroid_group = np.zeros(n)
        for v in range(n):
            vote_actuel = vote[v, :]
            dist1 = hamming_distance(vote_actuel, a1_tilde)
            dist2 = hamming_distance(vote_actuel, a2_tilde)

            if dist2 > dist1:
                centroid_group[v] = 0
            else:
                centroid_group[v] = 1

        if len(centroid_group[centroid_group == 0]) == 0 or len(centroid_group[centroid_group == 1]) == 0:
            # On réinitialise les centroïdes aléatoirement et on recommence
            a1_tilde = vote[np.random.randint(0, n), :]
            a2_tilde = vote[np.random.randint(0, n), :]
            ancien_group = np.zeros(n)
            continue

        # Condition d'arrêt

        if np.array_equal(ancien_group, centroid_group):
            vote_c1 = vote[centroid_group == 0, :]
            vote_c2 = vote[centroid_group == 1, :]
            dist_c1 = [hamming_distance(a1_tilde, vote_c1[v, :]) for v in range(vote_c1.shape[0])]
            dist_c2 = [hamming_distance(a2_tilde, vote_c2[v, :]) for v in range(vote_c2.shape[0])]
            return sum(dist_c1) + sum(dist_c2)

        ancien_group = centroid_group.copy()

        a1_tilde = u1_appro_calcul(vote[centroid_group == 0, :])[1]
        a2_tilde = u1_appro_calcul(vote[centroid_group == 1, :])[1]


def kmeans_totaux(vote):
    n, m = vote.shape
    a1_tilde = vote[np.random.randint(0, n), :]
    a2_tilde = vote[np.random.randint(0, n), :]

    ancien_group = np.zeros(n)

    max_iterations = 100  # au cas où la polarisation est 0
    while True:

        max_iterations -= 1
        if max_iterations < 0:
            return 0

        centroid_group = np.zeros(n)
        for v in range(n):
            vote_actuel = vote[v, :]
            dist1 = spearman_distance(vote_actuel, a1_tilde)
            dist2 = spearman_distance(vote_actuel, a2_tilde)

            if dist2 > dist1:
                centroid_group[v] = 0
            else:
                centroid_group[v] = 1

        if len(centroid_group[centroid_group == 0]) == 0 or len(centroid_group[centroid_group == 1]) == 0:
            # On réinitialise les centroïdes aléatoirement et on recommence
            a1_tilde = vote[np.random.randint(0, n), :]
            a2_tilde = vote[np.random.randint(0, n), :]
            ancien_group = np.zeros(n)
            continue

        # Condition d'arrêt
        if np.array_equal(ancien_group, centroid_group):
            vote_c1 = vote[centroid_group == 0, :]
            vote_c2 = vote[centroid_group == 1, :]
            dist_c1 = [spearman_distance(a1_tilde, vote_c1[v, :]) for v in range(vote_c1.shape[0])]
            dist_c2 = [spearman_distance(a2_tilde, vote_c2[v, :]) for v in range(vote_c2.shape[0])]
            return sum(dist_c1) + sum(dist_c2)

        ancien_group = centroid_group.copy()

        a1_tilde = u1_totaux_calcul(vote[centroid_group == 0, :])[1]
        a2_tilde = u1_totaux_calcul(vote[centroid_group == 1, :])[1]
