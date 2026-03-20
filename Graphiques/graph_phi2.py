import matplotlib.pyplot as plt
import numpy as np
from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux
from src.mesures.phi2 import phi_2_appro, phi_2_ordre_totaux
from src.mesures.paire_a_paire import distances_pp_appro, distance_pp_ordre_totaux


"""Question 6"""

nb_votante = 100
nb_candidate = 10
epsilone = 0.1

y_appro = []
y_totaux = []

for i in np.arange(0, 1+epsilone, epsilone):
    vote_appro = creation_vote_appro(nb_votante, nb_candidate, i)
    dist_appro = distances_pp_appro(vote_appro)
    y_appro.append(phi_2_appro(vote_appro, dist_appro))

    vote_totaux = creation_vote_ordre_totaux(nb_votante, nb_candidate, i)
    dist_totaux = distance_pp_ordre_totaux(vote_totaux)
    y_totaux.append(phi_2_ordre_totaux(vote_totaux, dist_totaux))

y_appro = np.array(y_appro)
y_totaux = np.array(y_totaux)

plt.plot(np.arange(0, 1+epsilone, epsilone), y_appro, label="appro")
plt.plot(np.arange(0, 1+epsilone, epsilone), y_totaux, label="totaux")
plt.plot(np.arange(0, 1+epsilone, epsilone), np.arange(0, 1+epsilone, epsilone), label="y=x")
plt.legend()
plt.show()
