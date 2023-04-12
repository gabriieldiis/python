valor_codigo = 0.7

numero_solicitacoes = int(input("Quantas solicitações de pin via sms foram solicitadas pelo usuário: "))

valor_total = numero_solicitacoes * valor_codigo

if (valor_total > 0.25):
    print("O Whatsapp seria mais em conta")
    print(f"Valor total é de {valor_total:.2f}")
else:
    print("Otimo, que bom que esse cliente conseguiu logar no site")
    print(f"Valor total é de {valor_total:.2f}")

produto_venda = 0
produto_venda = int(input("Você deseja fechar o serviço com o Whatsapp: 1 - SIM 2 - NÃO"))

while(produto_venda != 1):
    produto_venda = int(input("Você deseja fechar o serviço com o Whatsapp: 1 - SIM 2 - NÃO"))
    if (produto_venda == 1):
        print("Que ótimo ficamos felizes em fechar negócio com você: ")
        print("Vamos testar com um novo cliente: ")
        solicitacao_whatsapp = int(input("O cliente solicitou o pin via WhatsApp ele recebeu? 1 - SIM | 2 - NÃO"))
        solicitacao_whatsapp = 0
        while(solicitacao_whatsapp != 1):
            print("Eita, poderia verifciar se não o recebeu mesmo: "),
            solicitacao_whatsapp = int(input("O cliente solicitou o pin via WhatsApp ele recebeu? 1 - SIM | 2 - NÃO"))
            if(solicitacao_whatsapp == 1):
                print("Ótimo ficamos  à disposição:")
            else:
                print("Solicite de novo, ou verifique com a loja prestadora do serviço desejado")
    else:
        print("Voce tem certeza que não quer fechar esse negocio, rs: ")
        print("Cada Whatsapp custa R$0.25 centavos por mensagem:")