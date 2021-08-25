print("-----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("-----------------------------------")
print()

numeroSecreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou", chute)

if numeroSecreto == chute:
    print("você acertou!")
else:
    print("você errou!")
