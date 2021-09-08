import random


def jogar():

    imprimeApresentacao()
    palavraSecreta = selecionaPalavraSecreta()

    letrasCertas = inicializaLetrasCertas(palavraSecreta)
    print(letrasCertas)

    enforcou = False
    acertou = False
    tentativas = 7

    while (not enforcou and not acertou):

        chute = pedeChute()

        if chute in palavraSecreta:
            mostraChuteCerto(palavraSecreta, letrasCertas, chute)
        else:
            tentativas -= 1
            desenhaForca(tentativas)
            print("Restam {} tentativas".format(tentativas))

        print(letrasCertas)

        if tentativas == 0:
            enforcou = True
            mensagemDerrota(palavraSecreta)

        elif "_" not in letrasCertas:
            acertou = True
            mensagemVitoria()

    print("Fim de Jogo!")


def imprimeApresentacao():
    print("-----------------------------------")
    print("Bem vindo ao jogo da Forca!")
    print("-----------------------------------")
    print()


def selecionaPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()

    return palavraSecreta


def inicializaLetrasCertas(palavra):
    letrasCertas = ["_" for letra in palavra]

    return letrasCertas


def pedeChute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def mostraChuteCerto(palavra, letras, chute):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
        index += 1


def mensagemVitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagemDerrota(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenhaForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    jogar()
