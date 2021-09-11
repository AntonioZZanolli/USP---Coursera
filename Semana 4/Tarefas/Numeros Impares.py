numero = int(input("Quantos números impares você deseja?"))

i = 1
n = 1

while i <= numero:
    if n %2 !=0 and i <= numero:
        print(n)
        i += 1
        n += 1
    else:
        n += 1
