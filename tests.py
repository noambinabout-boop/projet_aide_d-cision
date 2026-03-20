from src.creation.approbation import creation_vote_appro
from src.creation.ordre_totaux import creation_vote_ordre_totaux
from src.mesures.paire_a_paire import distances_pp_appro, distance_pp_ordre_totaux
from src.mesures.phi2 import phi_2_appro


vote = creation_vote_appro(100, 4, 0)
dist = distances_pp_appro(vote)
print(dist)
print(phi_2_appro(vote, dist))


vote = creation_vote_ordre_totaux(100, 4, 0)
dist = distance_pp_ordre_totaux(vote)
print(dist)
print(phi_2_appro(vote, dist))


