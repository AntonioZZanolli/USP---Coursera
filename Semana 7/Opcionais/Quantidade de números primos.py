def n_primos(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input("Limite máximo: "))

n = 2
while n< limite:
    if n_primos(n):
        print(n, end=", ")
    n = n+1
