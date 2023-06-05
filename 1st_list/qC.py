a = int(input()) # Arthur
l = int(input()) # Luiz
p = int(input()) # Pedro
h = int(input()) # Duração da competição (em horas)

# Calculando o valor máximo
x = (a + l + abs(a - l))/2
y = (x + p + abs(x - p))/2

# Determinando o valor máximo obtido por um participante no intervalo da competição
maximo = y * h

# Imprime o valor máximo
print(int(maximo))