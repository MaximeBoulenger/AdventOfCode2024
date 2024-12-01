Liste1 = []
Liste2 = []

with open('Exo1.csv', 'r') as data:
    for ligne in data:
        colonnes = ligne.strip().split('   ')
        Liste1.append(int(colonnes[0]))
        Liste2.append(int(colonnes[1]))

Liste1.sort()
Liste2.sort()

# Partie 1
Liste3 = []
Distance = 0

for i in range(len(Liste1)):
    Liste3.append(abs(Liste2[i] - Liste1[i]))
    Distance += Liste3[i]

print("Distance Totale :", Distance)

# Partie 2

Compteur = 0
Distance = 0

for i in range(len(Liste1)):
    for j in range(len(Liste2)):
        if Liste1[i] == Liste2[j]:
            Compteur += 1
    Distance += Compteur * Liste1[i]
    Compteur = 0

print("Similarité :", Distance)