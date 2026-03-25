import numpy as np
from src.mesures.consensus import u1_appro_calcul, u1_totaux_calcul
from src.mesures.kmeans import kmeans_appro, kmeans_totaux


def phi_dh(vote):
    n, m = vote.shape
    u1 = u1_appro_calcul(vote)[0]
    u2 = kmeans_appro(vote)
    return(2 * (u1 - u2))/(n * m)


def phi_ds(vote):
    n, m = vote.shape
    u1 = u1_totaux_calcul(vote)[0]
    u2 = kmeans_totaux(vote)
    return(4 * (u1 - u2))/(n * (m**2))

