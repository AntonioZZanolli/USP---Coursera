largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

h = 1
l = 1

while h <= altura:
    while l <= largura:
        print("#", end = "")
        l = l + 1
    h = h + 1
    print()
    l = 1
