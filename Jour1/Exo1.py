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

"""Distance = 0
for i in range(len(Liste1)):
    Distance += abs(Liste1[i] - Liste2[i])"""

Distance = sum(abs(Liste1[i] - Liste2[i]) for i in range(len(Liste1)))

print("Distance Totale :", Distance)

# Partie 2

Distance = 0

for i in range(len(Liste1)):
    Compteur = 0
    for j in range(len(Liste2)):
        if Liste1[i] == Liste2[j]:
            Compteur += 1
    Distance += Compteur * Liste1[i]

print("Similarité :", Distance)