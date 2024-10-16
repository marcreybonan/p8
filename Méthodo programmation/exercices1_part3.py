#EXERCICE 11

#Création du dictionnaire 
eleves=
{
    "Harry Potter": 15,
    "Hermione Granger": 20,
    "Ron Weasley": 12,
    "Draco Malfoy": 19,
    "Luna Lovegood": 16,
    "Neville Longbottom": 13  
}

# On va trier les élèves
# sorted() nous est utile pour le tri et items() renvoie une paire (valeur/clé)
#reverse = True afin de trier les élèves par ordre de notes croissantes
tri = sorted(eleves.items(), key=lambda x: x[1], reverse=True)

# Affichage des résultats  
print("Étudiants triés par note (du meilleur au plus faible) :")
for nom, note in tri:
    print(f"{nom} : {note}")
