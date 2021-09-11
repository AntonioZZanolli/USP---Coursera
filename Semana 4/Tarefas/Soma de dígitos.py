n = int(input("Insira um número inteiro: "))

resto = n%10
x = 0

while n > 0:
        if n > 0:
            resto = n%10
            n = n//10
        x = x + resto
print (x)
