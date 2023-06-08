# Arthur 10
# Luiz 30
# Pedro 100
# Input D, o número de diamantes requeridos por Tantan
# Output o nome da oferta aceita

# Case 1:
# Input: 20, Output: Luiz
# Case 2:
# Input: 120, Output: Nenhum
# Case 3:
# Input: 5, Output: Arthur

# Input de diamantes requeridos por Tantan
d = int(input())

if d > 100:
    print('Nenhum')
elif 30 < d <= 100:
    print('Pedro')
elif 10 < d <= 30:
    print('Luiz')
else:
    print('Arthur')

