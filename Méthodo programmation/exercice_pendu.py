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
        
#On demande au joueur d'entrer une lettre
#.lower() afin d'éviter tout probleme de casse
       lettre = input("Trouvez une lettre : ").lower()


#Si la lettre a déjà été trouvée on l'indique au joueur 
#Si la lettre est bonne on l'ajoute grâce à .append et on le signifie l'utilisateur
#Si la lettre entrée est mauvaise alors le nombre de chanches baisse 
       if lettre in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_devinees.append(lettre)
  
        if lettre not in mot_a_trouver:
            chances -= 1  
            print("Faux !")
        else:
            print("Trouvée !")

#On vérifie si le mot a été trouvé, si c'est le cas alors on l'indique (victoire/défaite)
       if all(l in lettres_devinees for l in mot_a_trouver):
            print("Bravo ! Vous avez trouvé :", mot_a_trouver)
            break  
    else:
        print("\nVous n'avez plus de tentative. Le mot à trouver était :", mot_a_trouver)

#On crée une fonction qui gère le flux de jeu en permettant si elle est vraie (while True) à jouer encore 
#Si le joueur ne veut plus joueur(jouer_encore != 0) on le remercie 
def main():
    while True:
        jouer()
        jouer_encore = input("\nUne autre partie (o ou n) ? : ").lower()
        if jouer_encore != 'o':
            print("Merci d'avoir joué !")
            break
#Condition qui vérifie si le programme est executé de façon directe ou importée 
#Permet de lancer le jeu
if __name__ == "__main__":
    main()
