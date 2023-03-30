import random

print("Seja Bem Vido!")


numero_random = random.randrange(1 , 101)
numero_secreto = numero_random
total_tentativas = 0
pontos = int(1000)
print(numero_secreto)


print("Qual nível de dificuldade?")
print("1 - facil")
print("2 - medio")
print("3 - dificil")

nivel = int(input("Digite o nível 1 - 3 "))
if (nivel == 1):
    total_tentativas = 20
elif (nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodada in range (1, total_tentativas + 1):
    print(f"Tentativa: {rodada} de {total_tentativas} pontos")
    chute_str = input("Digite um número entre 1 e 100 chute: ")
    print("Você digitou" , chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print(f"Você acertou e fez {pontos}]")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("O seu chute foi menor do que o numero secreto")
        pontos_perdidos = abs(numero_random - chute)
        pontos = pontos - pontos_perdidos

print("fim do jogo!!")
print(numero_secreto)