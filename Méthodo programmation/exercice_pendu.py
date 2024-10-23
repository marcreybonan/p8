import random
#Génère l'aléatoire

#On crée une liste puis on génère un mot aléatoire à retourner 
def choix():
    mots = ["difffent", "mot", "pour", "jouer", "jeu"]
    return random.choice(mots)

#On affiche au joueur que le jeu va commencer
#On commence une boucle qui continuera tant qu'il reste une tentative au joueur
#On affiche l'état du mot actuel avec une chaîne de caractère, que ce soit les lettres trouvées ou des _ si le joueur n'a pas encore trouvé
#On affiche le nombre de chances restantes

def jeu():
    mot_a_trouver = choix()
    lettres_devinees = []
    chances = 6  

    print("Bonjour, essayer de deviner le mot")

    while chances > 0:
        
        mot_affiche = ''.join([lettre if lettre in lettres_devinees else '_' for lettre in mot_a_trouver])
        print("\nMot a deviner :", mot_affiche)
        print("Chances restantes :", chances)
