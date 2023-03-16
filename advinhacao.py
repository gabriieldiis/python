print("Seja Bem Vido!")

numero_secreto = 42
total_tentativas = 3

#enquanto ainda há tentativas disponiveis
for rodada in range (1, total_tentativas + 1):
    print(f"Tentativa: {rodada} de {total_tentativas}")
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
        print("Você acertou")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("O seu chute foi menor do que o numero secreto")

print("fim do jogo!!")