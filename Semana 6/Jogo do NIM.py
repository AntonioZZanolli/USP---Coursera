Usuario = 0
Computador = 0

def usuario_escolhe_jogada(n, m):
        y = int(input("Quantas peças você vai tirar? "))
        while y > m or y > n or y <= 0:
                print ("Oops! Jogada inválida! Tente novamente")
                y = int(input("Quantas peças você vai tirar? "))
        if y <= m and y <= n and y == 1:
                print("Você tirou uma peça")
        if y <= m and y <= n and y > 1:
                print("Você tirou ", y, "peças")
        return int(y)

def computador_escolhe_jogada(n, m):
        x = n% (m+1)
        if n <= m:
                x = n
        if x > m:
                x = m
        if x == 0:
                x = 1
        if x == 1:
                print("O computador tirou uma peça")
        else:
                print("O computador tirou", x, "peças")
        return int(x)



def partida():
        global Usuario
        global Computador
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))
        if n % (m+1) == 0:
                print("\nVocê começa")
                while n != 0:
                        n = n - usuario_escolhe_jogada(n, m)
                        print("Agora restam", n, "peças no tabuleiro\n")
                        if n == 0:
                                print("Você ganhou!")
                                Usuario += 1
                                break
                        n = n - computador_escolhe_jogada(n, m)
                        print("Agora restam", n, "peças no tabuleiro\n")
                        if n == 0:
                                print("O computador ganhou")
                                Computador += 1
                                break
        else:
                print("\nComputador começa")
                while n != 0:
                        n = n - computador_escolhe_jogada(n, m)
                        print("Agora restam", n, "peças no tabuleiro\n")
                        if n == 0:
                                print("O computador ganhou")
                                Computador += 1
                                break
                        n = n - usuario_escolhe_jogada(n, m)
                        print("Agora restam", n, "peças no tabuleiro\n")
                        if n == 0:
                                print("Você ganhou!")
                                Usuario += 1
                                break

def campeonato():
        global Usuario
        global Computador
        print("\n**** Rodada 1 ****\n")
        partida()
        print("\n**** Rodada 2 ****\n")
        partida()
        print("\n**** Rodada 3 ****\n")
        partida()
        print("\n**** Final do campeonato! ****\n\nPlacar: Você", Usuario, "X", Computador, "Computador")
        Usuario = 0
        Computador = 0


Escolha = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if Escolha == 1:
        print("\nVocê escolheu partida uma isolada!\n")
        partida()
else:
        print("\nVocê escolheu um campeonato!")
        campeonato()
        


