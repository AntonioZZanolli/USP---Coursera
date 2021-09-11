lista = []

while True:
    n = int(input("Digite um número inteiro: "))
    if n== 0:
        break
    else:
        lista.append(n)

for i in reversed(lista):
    print(i)
