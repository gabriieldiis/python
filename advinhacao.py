print("--------------------------------------")
print("Seja bem vindo ao jogo de adivinhação!")
print("--------------------------------------")

numero_secreto = int(42)
total_tentativas = 3
chute_str = input("Digite seu número : ")
print("Você digitou", chute_str)
print("Tentatntiva nº ", total_tentativas)
while (total_tentativas  0):
    #   variaveis   #
chute = int(chute_str)
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou o número secreto")
else:
    if (maior):
        print("Voce errou, o seu chute foi maior que o número secreto")
    elif  (menor):
        print("Voce errou, o seu chute foi menor que o número secreto")

    total_tentativas = total_tentativas - 1
print("Fim do jogo!")

