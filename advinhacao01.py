print("Seja Bem Vido!")

numero_secreto = 42
total_tentativas = 3
rodada = 1

#enquanto ainda há tentativas disponiveis
while (rodada <= total_tentativas):
    print("Tentativa:", rodada ," de ", total_tentativas)
    chute_str = input("Digite o seu chute: ")
    print("Você digitou" , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if(maior):
            print("O seu chute foi maior do que o numero secreto")
        elif (menor):
            print("O seu chute foi menor do que o numero secreto")
    rodada = rodada + 1
print("fim do jogo!!")