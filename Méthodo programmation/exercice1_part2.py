#EXERCICES AVEC DIFFERENTS TYPES DE DONNEES 

#EXERCICE 1 

#On crée notre tuple avec les différentes données 
tuple = (42, "Obi-wan Kenobi au KOD", 92,8, True)

#On cherche à afficher leur index 
for ix, donnee in enumerate(tuple):
     print(f"{ix} : {donnee}")

#EXERCICE 2

#Impossible de changer un éléménent des tuples du fait de leur caractère immutable
#Cette différence avec les listes notamment a plusieurs avantages
#Moins de bug ?
#Plus de securité 
#Perfomance (+ rapides) ?

#EXERCICES 3 et 4

# Création de la liste association nom et note  
etudiants = [("Alice", 20), ("Anna", 20), ("Pablo", 20)]

# Conversion des tuples en dictionnaire avant de l'afficher 
dictionnaire = dict(etudiants)
print("Dictionnaire :" dictionnaire)

# On ajoute un nouvel étudiant "Sven" avec une note  
dictionnaire["Sven"] = 20 

#On affiche le dictionnaire après l'ajout de la note de Sven
print("Dictionnaire :", dictionnaire)

#On souhaite supprimer de notre dictionnaire l'étudiante Alice
etudiante_partante = "Alice"
dictionnaire_notes.pop(etudiante_partante)
 
# On affiche le dictionnaire avec les étudiants restants 
print("Eleves restants:", dictionnaire)


#EXERCICE 5

#Création de notre liste  
amis = (("Marco", 27), ("Andra", 28), ("Bugsy", 28), ("Alexis", 28), ("Gaby", 10), ("Polo", 29))
#Gaby a en fait 30 ans 

#On affiche les personnes dont l'age est sup à 20 ans
print("Qui a plus de 20 ans ? :")
for prenom, age in amis:
    if age > 20:
        print(prenom)

#EXERCICE 6

#Créations des listes 
gundam = [("Providence"),("Duel"),("Legend"),("Astray")]
prix = [(30), (20), (25), (15)]

#Fusionner les listes à l'aide de zip puis affichage de la liste
liste_unique = list(zip(gundam, prix))
print("liste unique :")
for gundam, prix in liste_fusionnee:
    print(f"{gundam[0]} : {prix[0]}")

#Sympa comme exercice


#EXERCICE 7

#Création des deux listes de nombres
liste_un = (2, 4, 6, 8, 10)
liste_deux = (1, 3, 5, 7, 9)

#On s'aide de l'opérateur set() utilisé en mathématiques afin de convertir les tuples en ensemble qu'on pourra comparer et trouver les unions et intersections
eun = set(liste_un)
edeux = set(liste_deux)

intersection = eun.intersection(edeux)
union = eun.union(edeux)

#On affiche les résultats
print("Union", union)
print("Intersection", intersection)


#EXERCICE 8 
#Comme dans l'exercice précédent on utilisera set()

#Création liste
liste =[(0, 0, 1, 1 0, 1, 1, 0, 0]

#Comme dans l'exercice précédent on a recours a set() : 
same = set(liste)

#On affiche les résultats 
print("liste sans modif", liste)
print("liste apres modif", same)


