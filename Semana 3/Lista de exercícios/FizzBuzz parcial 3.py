numero_int = int(input("Digite o número: "))

calculo3 = numero_int % 3
calculo5 = numero_int % 5

if calculo3 == 0 and calculo5 == 0:
    print("FizzBuzz")
else:
    print(numero_int)
