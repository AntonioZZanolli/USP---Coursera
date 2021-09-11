def fizzbuzz(x):
    calculo3 = x % 3
    calculo5 = x % 5

    if calculo3 == 0 and calculo5 == 0:
        return ("FizzBuzz")
    elif calculo3 == 0 and not calculo5 == 0:
        return ("Fizz")
    elif calculo5 == 0 and not calculo3 == 0:
        return ("Buzz")
    else:
        return(x)
