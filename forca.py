def jogar():
    print("-----------------------------------")
    print("Bem vindo ao jogo da Forca!")
    print("-----------------------------------")
    print()

    palavraSecreta = "banana"
    letrasCertas = ["_"] * len(palavraSecreta)

    enforcou = False
    acertou = False

    print(letrasCertas)

    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavraSecreta:
            if chute.upper() == letra.upper():
                letrasCertas[index] = letra
            index += 1
        print(letrasCertas)

    print("Fim de Jogo!")


if __name__ == "__main__":
    jogar()
