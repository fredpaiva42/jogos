import random

print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("-----------------------------------")
print()

# poderia usar o randrange também random.randrange(1,101)
numeroSecreto = random.randint(1, 101)
totalDeTentativas = 0
rodada = 1

print("Níveis de dificuldade:")
print("(1) Fácil \n(2) Médio \n(3) Difícil")
print()

nivel = int(input("Qual o nível de dificuldade você deseja? "))

if nivel == 1:
    totalDeTentativas = 20
elif nivel == 2:
    totalDeTentativas = 10
else:
    totalDeTentativas = 5

while rodada <= totalDeTentativas:
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou", chute)
    print()

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        print()
        rodada += 1
        continue

    acertou = chute == numeroSecreto
    foiMaior = chute > numeroSecreto
    foiMenor = chute < numeroSecreto

    if acertou:
        print("você acertou!")
        print()
        break
    else:
        if foiMaior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
            print()
        elif foiMenor:
            print("Você errou! O seu chute foi menor do que um número secreto")
            print()

    rodada += 1

print("Fim de Jogo!")
print()
print("O número secreto era: {}".format(numeroSecreto))
