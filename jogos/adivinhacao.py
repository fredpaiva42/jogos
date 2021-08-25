print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("-----------------------------------")
print()

numeroSecreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

acertou = chute == numeroSecreto
foiMaior = chute > numeroSecreto
foiMenor = chute < numeroSecreto

if acertou:
    print("você acertou!")
else:
    if foiMaior:
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif foiMenor:
        print("Você errou! O seu chute foi menor do que um número secreto")
