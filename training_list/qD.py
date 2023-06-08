# dm = dia do minecraft | dr = dia real

# dm = 10 minutos = 12000 ticks, considerando apenas o tempo jogado por Tantan
# dr = 3 horas = 180 minutos = 9 dm

d = int(input())  # input da quantidade de dias na vida real
c = int(input())  # input da quantidade de casas construídas

ticks_dia = 12000  # metade do ciclo de dia do minecraft

# total de ticks = número de ticks por dia * input D * número de ciclos de dia no intervalo dado (180 minutos)
ticks_total = ticks_dia * d * 9

ticks_por_casa = ticks_total // c  # média de ticks por casa = total de ticks / número de casas construídas

print(ticks_por_casa)
