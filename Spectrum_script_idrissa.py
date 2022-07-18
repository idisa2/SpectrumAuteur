
# Fonction de saisi
from glob import glob
from itertools import count


def saisirTexte(nom_auteur):
    # création de fichier en mode mise à jour
    fichier=open("nom_auteur.txt", "w", encoding='utf8')

    # On demande à l'utilisateur de saisir une phrase
    phrase= input("veuiilez entrer une phrase: ")
    fichier.write(phrase+ '\n')
    #On vérifie tant que la phrase est différent de #FIN#
    while phrase != "#Fin#":
        phrase =input("Saisi une autre phrase: ")
        fichier.write(phrase + '\n')

    if phrase == "#Fin#":    
        fichier.close()

# Fonction de lecture
def motsUnique(nom_auteur):
    global liste
    with open("nom_auteur.txt", "r", encoding='utf8') as fichier: # ouvrir le fichier en mode lecture
        contenu= fichier.read() # lire le contenu du fichier
        liste = contenu.split()

    return liste


# Fonction de nombre par mot
def nombreParMots(L,nom_auteur):

    fichier=open("nom_auteur.txt", "r", encoding='utf8' ) # ouvrir le fichier en mode lecture
    contenu= fichier.read() # lire le contenu du fichier
    MyDict ={}
    
    contenuSplit= contenu.split()

    for ch in L:
        MyDict[ch] = contenuSplit.count(ch)

    return MyDict

# Fonction nombre total
def nombreTotal(nom_auteur):
    fichier = open("nom_auteur.txt", "r")
    contenu= fichier.read() # lire le contenu du fichier
    
    somme = len(contenu.split())

    return somme

# Fonction spectrum auteur
def spectrumAuthor(D,S):
    dic = {}

    for cle in D:
        dic[cle]=round(D[cle]/S,1)
   
    with open("spectrum_store.txt", "w", encoding='utf8') as fichier:

        fichier.write('« #NEW_AUTHOR# »\n')
        fichier.write(nom_auteur + "\n")
        
        for c, v in dic.items():

            ligne = c+ ' ' +str(v)
            fichier.write(ligne+ '\n')
        
        fichier.write("« #END_AUTHOR# »")

    return dic

def spectrumCompare(D1, D2):
    Distance = 0

    for m in D1:
        if m in D2:
             Distance = Distance + abs(D1[m]/len(D1)-D2[m]/len(D2))
    return Distance
# Fonction perttant d'acceder en mode apprentissage
def modeApprentissage(nom_auteur):
    saisirTexte(nom_auteur)
    nombreTotal(nom_auteur)
    D={'un':len('un'),'deux':len('deux'), 'trois':len('trois')}
    S = len(D)
    spectrumAuthor(D,S) 

# Fonction perttant d'acceder en mode identification
def modeIdentify():
    
    saisirTexte(nom_auteur)

    L= ['azerty', 'bonjour', 'bien', 'hello', 'super']
    nombreParMots(L,nom_auteur)
        
    d1={'Bon':len('Bon'),'jour':len('jour'), 'hello':len('hello'),'world':len('world'),'Thanks':len('Thanks'),'Hello':len('Hello')}
    d2={'Hello':len('Hello'), 'world':len('world'),'Okay':len('Okay'),'super':len('super'),'Merci':len('Merci')}
    S1=len(d1)
    S2=len(d2)

    D1=spectrumAuthor(d1,S1)
    D2=spectrumAuthor(d2,S2)   
    spectrumCompare(D1, D2)


#global nom_auteur
menu = {}
print('')
print('*************MENU PRINCIPAL**************')
menu['1']="Entrer en mode apprentissage----:1  ***" 
menu['2']="Entrer en mode identification---:2  ***"
menu['3']="Quitter le programme------------:3  ***"

while True: 
    options=menu.keys()

    for entry in options:
        print(entry, menu[entry])
    print('*************Faites votre choix***********')
    selection=input("Please Select: ") 
    if selection =='1': 
        #nom_auteur = input("veillez entrer le nom d'auteur :")
        modeApprentissage()
    elif selection == '2':
        nom_auteur = input("veillez entrer le nom d'auteur :")
        modeIdentify()
    elif selection == '3': 
        break
    else: 
        print ("Unknown Option Selected!")


