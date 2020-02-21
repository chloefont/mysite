def get_rank(score_percentage):
    ranks = [
        [100,"Impessionnant", "Wow! Y a de la triche dans l'air (ou dans l'eau je dirais)."],
        [75, "Bravo!", "Tu en sais plus que la plupart des poissons (et j'en ai connu)!"],
        [50, "Pas mal!", "Une sur deux, c'est pas encore ça. On va dire que tu est un expert d'eau douce."],
        [25, "Y a du boulot...", "C'est mieux que rien, mais tu patauges dans l'eau de mer."],
        [0, "Pas bravo!", "Tu déçois tous les poissons là (surtout Philippe le poisson lion)..."],
    ]

    for rank in ranks:
        if rank[0] <= score_percentage:
            return {'title': rank[1], 'description': rank[2]}

    raise ValueError("Invalid score %s" %score_percentage)
