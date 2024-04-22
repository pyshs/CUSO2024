def compter_mots_seuil(phrase, nombre_min_lettres = 4, sortie_fichier = False):
    """
    Compter les mots de plus de (seuil) lettres dans (phrase)
    """
    liste_mots = phrase.split(" ")
    nombre_mots = len(liste_mots)
    if len(phrase) == 0:
        return "Vous n'avez rien écrit"
    else:
        compteur = 0
        for i in liste_mots:
            if len(i) >= nombre_min_lettres:
                compteur+=1
        proportion = round(100*compteur/nombre_mots,2)
        informations = {"Total":compteur,"Proportion":proportion,
                       "Phrase":phrase,"Seuil":nombre_min_lettres}
        if sortie_fichier:
            with open("resultat.txt","w") as f:
                f.write(str(informations))
        return informations