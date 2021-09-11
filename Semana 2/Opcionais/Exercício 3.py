inteiro = input("Digita um número inteiro: ")
int_int = int(inteiro)

unidade = int_int % 10
dezena = (int_int - unidade) // 10
dezena_resultado = dezena % 10

print("O dígito das dezenas é ", dezena_resultado)
