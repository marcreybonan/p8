#EXERCICE 1
#Creation d'une liste simple 
#On crée une liste simple qu'on affichera ensuite avant d'afficher un de ses éléments particulier

liste = ["L1", "L2", "L3", "M1", "M2"]
print(liste)

#J'affiche un élément de ma liste décrivant ma situation 
print = ("Je suis en" liste[0])

#EXERCICE 2
#Accès au contenu d'une liste
#On va créer une liste avec 6 éléments, chaque élément est un organe

listte = ["cerveau", "reins", "coeur", "foie", "poumons", "thyroide"]

#On demande à 3 étudiants en médecine lequel il préfère

print("Je préfère le", listte[0])  
print("Moi je préfère la", listte[5])
print("Je ne vous comprends pas car mon organe favori est le", listte[2])

#EXERCICE 3
#Modifier le contenu d'une liste en supprimant le deuxième élément de cette liste et en rajoutant un dernier élément

ma_liste = ["Un", "Deux", "Trois", "Quatre"]
ma_liste.remove("Deux")
ma_liste.append("Cinq") 

#On affiche le contenu de la liste avant de la supprimer

print(ma_liste)
ma_liste.clear()

#EXERCICE 4
#Ajouter un nouvel élément à la fin d'une liste puis supprimer le premier élément

lst = ["1", "2", "3"]
lst.append("4")
lst.remove("1")

#S'inspirer de l'exercice 11 pouur mes élèves


#EXERCICE 5
#On demande à nos élèves de saisir des nombres (pas trop non plus) afin d'en faire ensuite une liste
input_liste = input("Saisissez des nombres mais séparés d'un espace : ")

# Diviser la chaîne d'entrée et convertir chaque élément en entier  
#split() nous est utile afin de construire une liste et ce en exploitant les espaces laissés volontairement
liste_complete = input_liste.split()

# Afficher la liste  
print(liste_complete)

#Annoncer que l'on va inverser la liste
print("Cette liste sera inversée")

#Inverser les éléments de la liste avec reverse() et vérifier le résultat en affichant liste_complete
liste_complete.reverse()
print(liste_complete)

#On pourrait félicier ou non les élèves si le résultat est bon...


#EXERCICE 6  
#Solution de facilité, si un nombre est pair alors le reste de la division par 2 sera nul 
#Ainsi il est choisi d'utiliser le modulo % et, considérons une liste [x, y, z] si x,y,z%2 == 0 alors ces nombres seront pairs et il n'y aura plus qu'à les afficher 
#Ainsi on considère une liste quelconque

liste = [3, 45, 32, 54, 37, 5432, 9374, 2938, 28475]

for nombres in liste:
  if nombres%2 == 0:
    print("voici les nb paires", nombres)
    
#On pourrait écrire les nb n'étant pas paires via else 

#EXERCICE 7 
#On pourrait utiliser l'opérateur sum() mais il est demandé d'utiliser l'opérateur for

somme = 0
liste = [2, 3, 43, 56, 33]

#Après avoir initialisé la variable somme et avoir crée notre liste nous n'avons plus qu'à calculer la somme et l'afficher
for nb in liste:
  somme+=nb
print("La somme est de" somme)

#EXERCICE 8 

#AVEC LA FONCTION INTEGREE MAX()
liste = [323, 22, 33, 54, 75, 170, 7, 78, 65, 43]

# Trouver l'élément le plus grand  
maxx = max(liste)

print("L'élément le plus grand de la liste est :", maxx)

#AVEC L'OPERATEUR FOR
liste = [323, 22, 33, 54, 75, 170, 7, 78, 65, 43]

#On initialise notre variable qui est le max de la liste

max= 0
liste = [ 1, 2, 3]

#On parcourt notre liste à la recherche du plus grand nombre et on donnera sa valeur à la variable max
for nb in liste:
  if nb > max:
    max = nb
    
print(nb)

#EXERCICE 9
#On crée notre liste et on utilisera count() afin de voir le nb d'occurences au sein de notre liste
#On introduit une variable occurence

occurence = 0
liste = [1, 1, 0, 1, 0, 1, 0, 0, 0]
repetitions = liste.count(occurence)

#On affiche le résultat

print(f"Le chiffre {occurence} est contenu {repetitions} au sein de notre liste") 


#EXERCICE 10
#On cherche à créer une liste à partir d'une liste initiale
#Dans cet exemple on va se servir de l'exercice 6, on va chercher au sein d'une liste de nombres, combien de nombres paires sont présents

#On initie les deux listes 
liste_initiale = [9465, 45, 579, 4747, 427, 5643, 46473, 648, 274, 321]
liste_paire = []

#On parcourt la liste comme dans l'exercice 6 à la recherche de nombre pair
#On ajoutera ces nombres paires à notre liste_paire grâce à .append
for nombre in ma_liste:
    if nb %2 == 0:
         liste_paire.append(nb)

#On affiche le résultat
print("Voici les nombres paires", liste_paire)


