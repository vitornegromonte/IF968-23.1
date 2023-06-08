import math
x = int(input())
z = int(input())

# distancia euclidiana = (x1 - x2) ^ 2 + (z1 - z2)^2

# Coordenadas:
## Hogsmeade: x = 34, z = 220
## Kakariko: x= 0, z = 0
## Solitude: x = 140, z = 456

#Calculando as distâncias para as vilas:
h = math.sqrt((x - 34)**2 + (z - 220)**2)
k = math.sqrt((x - 0)**2 + (z - 0)**2)
s = math.sqrt((x - 140)**2 + (z - 456)**2)

print(f'Distancia para Hogsmeade: {h:.2f}')
print(f'Distancia para Kakariko: {k:.2f}')
print(f'Distancia para Solitude: {s:.2f}')