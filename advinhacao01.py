print("Seja bem vindo!")

numero_secreto = 42
chute = int(input("Digite o seu chute: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
total_tentativas = 3

while (total_tentativas > 0 ):
    print(total_tentativas)
    chute = int(input("Digite o seu chute: "))
    if (acertou):
        print("Parabéns você acertou o numero secreto")
    else:
        if (maior):
            print("seu número chutado é maior do que o número secreto")
        elif (menor):
            print("Seu número chutado é menor do que o número secreto")
total_tentativas = total_tentativas - 1
