# Fonction de saisi
def saisirTexte(nom_auteur):
    # création de fichier en mode mise à jour
    fichier=open("nom_auteur.txt", "w")

    # On demande à l'utilisateur de saisir une phrase
    phrase= input("veuiilez entrer une phrase: ")
    fichier.write(phrase)
    #On vérifie tant que la phrase est différent de #FIN#
    while phrase != "#Fin#":
        phrase =input("Saisi une autre phrase: ")
        fichier.write(phrase)

    if phrase == "#Fin#":    
        fichier.close()

# Fonction de lecture
def motsUnique(nom_auteur):
    global liste
    with open("nom_auteur.txt", "r") as fichier: # ouvrir le fichier en mode lecture
        contenu= fichier.readlines() # lire le contenu du fichier
        for ch in contenu:
            liste = ch.split()
    return liste


nom_auteur = input("veillez entrer le nom d'auteur :")
saisirTexte(nom_auteur)
L=motsUnique(nom_auteur)
#print(liste)
#nombreParMots(L,nom_auteur)