# dm = dia do minecraft/2 | dr = dia real

# dm = 10 minutos = 12000 ticks
# dr = 3 horas = 180 minutos = 9 dm

d = int(input()) # input da quantidade de dias na vida real
c = int(input()) # input da quantidade de casas construídas

ticks_dia = 12000 # considerando apenas metade do dia

# ticks totais = número de ticks por dia X número de dias jogados * quantos dias do jogo em um dia real (180 minutos)
ticks_total = ticks_dia * d * 9

ticks_por_casa = ticks_total // c

print(ticks_por_casa)