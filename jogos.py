import forca
import adivinhacao

print("-----------------------------------")
print("Escolha o seu jogo!")
print("-----------------------------------")
print()

print("(1) Forca (2) Adivinhação")

jogoEscolhido = int(input("Qual jogo você deseja? "))

if jogoEscolhido == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogoEscolhido == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()
