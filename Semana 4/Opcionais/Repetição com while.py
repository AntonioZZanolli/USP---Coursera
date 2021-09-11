num = int(input("Digite um número inteiro: "))
adjacente = False
resto2 = 1
resto1 = num % 10
while num != 0 or not adjacente:
    numb2 = num // 10
    num = numb2//10
    resto2 = numb2 % 10
    if resto2 == 0 and num == 0:
        break
    if resto1 == resto2:
        adjacente = True
    resto1 = num % 10
    if resto1 == resto2:
        adjacente = True
if adjacente == True:
    print("SIM")
else:
    print("NÃO")
