import numpy as np
import random


def creation_vote_appro(n, m, polarisation):
    if n % 2 == 1 or m % 2 == 1:
        print("n et m doivent être pairs !")
        return

    # On choisit deux camps dominants aléatoirement
    camp_1 = np.random.randint(0, 2, m)
    camp_2 = 1 - camp_1

    vote = np.zeros((n, m), dtype=int)

    if polarisation == 0:
        vote[:] = camp_1  # tout le monde vote pareil

    elif polarisation == 1:
        # La moitié vote camp_1 et l'autre camp_2
        vote[:n//2] = camp_1
        vote[n//2:] = camp_2

    else:
        # Il n'y a plus seulement deux camps qui s'opposent : plus le bruit est élevé plus les votes sont disparates
        for i in range(n):
            # Plus polarisation est grand, plus on risque de tomber dans camp_2
            camp = np.random.choice([0, 1], p=[1 - polarisation/2, polarisation/2]) # On divise par deux pour avoir une polarisation totale seulement en 1 et pas en 0.5
            if camp == 0:
                vote[i] = camp_1
            else:
                vote[i] = camp_2

    return vote

