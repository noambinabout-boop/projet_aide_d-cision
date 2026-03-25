from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux
from src.mesures.paire_a_paire import distances_pp_appro, distance_pp_ordre_totaux
from src.mesures.phi2 import phi_2_appro, phi_2_ordre_totaux
from src.mesures.consensus import u1_totaux_calcul, u1_appro_calcul
from src.mesures.kmeans import kmeans_appro, kmeans_totaux
from src.mesures.phi_distances import phi_dh, phi_ds

vote = creation_vote_ordre_totaux(10, 4, 1)
print(vote)
print(kmeans_totaux(vote), u1_totaux_calcul(vote), phi_ds(vote))

vote = creation_vote_appro(10, 4, 1)
print(vote)
print(kmeans_appro(vote), u1_appro_calcul(vote), phi_dh(vote))

