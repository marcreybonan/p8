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







