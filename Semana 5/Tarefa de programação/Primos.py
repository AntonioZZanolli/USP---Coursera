def maior_primo(n):
    contador = 0
    divisor = 2
    while divisor <= n:
        if n % divisor != 0:
            divisor = divisor + 1
        else:
            if n% divisor == 0:
                contador = contador + 1
                divisor = divisor + 1
    if divisor > n and contador > 1:
        n = n - 1
        contador = 0
        divisor = 2
        return maior_primo(n)
    else:
        return(n)
