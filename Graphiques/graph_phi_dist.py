import matplotlib.pyplot as plt
import numpy as np
from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux
from src.mesures.phi_distances import phi_dh, phi_ds
from src.mesures.kmeans import kmeans_appro, kmeans_totaux

nb_votante = 100
nb_candidate = 10
epsilone = 0.1

y_appro = []
y_totaux = []

for i in np.arange(0, 1+epsilone, epsilone):
    vote_appro = creation_vote_appro(nb_votante, nb_candidate, i)
    y_appro.append(phi_dh(vote_appro))

    vote_totaux = creation_vote_ordre_totaux(nb_votante, nb_candidate, i)
    y_totaux.append(phi_ds(vote_totaux))

y_appro = np.array(y_appro)
y_totaux = np.array(y_totaux)

plt.plot(np.arange(0, 1+epsilone, epsilone), y_appro, label="phi dist appro")
plt.plot(np.arange(0, 1+epsilone, epsilone), y_totaux, label="phi dist totaux")
plt.plot(np.arange(0, 1+epsilone, epsilone), np.arange(0, 1+epsilone, epsilone), label="y=x")
plt.legend()
plt.show()
