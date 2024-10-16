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
