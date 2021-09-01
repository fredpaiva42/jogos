import random


def jogar():
    print("-----------------------------------")
    print("Bem vindo ao jogo da Forca!")
    print("-----------------------------------")
    print()

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()

    letrasCertas = ["_" for letra in palavraSecreta]

    enforcou = False
    acertou = False
    tentativas = 6

    print(letrasCertas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavraSecreta:
            index = 0
            for letra in palavraSecreta:
                if chute == letra:
                    letrasCertas[index] = letra
                index += 1
        else:
            tentativas -= 1
            print("Restam {} tentativas".format(tentativas))

        print(letrasCertas)

        if tentativas == 0:
            enforcou = True
            print()
            print("Você Perdeu!")
            print()

        elif "_" not in letrasCertas:
            acertou = True
            print()
            print("Você Ganhou!")
            print()

    print("Fim de Jogo!")


if __name__ == "__main__":
    jogar()
