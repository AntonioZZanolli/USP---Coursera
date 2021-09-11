numero = int(input("Digite um número inteiro: "))

n = 2

while numero % n !=0:
    sobra = numero % n
    n = n + 1
if n == numero:
    print("primo")
else:
    print("não primo")
