largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

h = 1
l = 1

while h <= altura:
    while l <= largura:
        if h == 1 or h == altura or l == 1 or l == largura:
            print("#", end = "")
        else:
            print(" ", end = "")
        l = l + 1
    h = h + 1
    print()
    l = 1


if h > 1 and h < altura and l > 1 and l < 1:
    print(" ", end = "")    
