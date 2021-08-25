print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("-----------------------------------")
print()

numeroSecreto = 42
totalDeTentativas = 3
rodada = 1

while rodada <= totalDeTentativas:
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))

    chute = int(input("Digite o seu número: "))
    print("Você digitou", chute)
    print()

    acertou = chute == numeroSecreto
    foiMaior = chute > numeroSecreto
    foiMenor = chute < numeroSecreto

    if acertou:
        print("você acertou!")
        print()
    else:
        if foiMaior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
            print()
        elif foiMenor:
            print("Você errou! O seu chute foi menor do que um número secreto")
            print()

    rodada += 1

print("Fim de Jogo!")
