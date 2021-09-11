import math

x1 = int(input("Digite o x do primeiro ponto: "))
y1 = int(input("Digite o y do primeiro ponto: "))
x2 = int(input("Digite o x do segundo ponto: "))
y2 = int(input("Digite o y do segundo ponto: "))

Distancia = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if Distancia >= 10:
    print("longe")
else:
    print("perto")
