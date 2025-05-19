#17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual=int(input("Digite o ano atual: "))
ano_nasc=int(input("Digite seu ano de nascimento: "))
idade=ano_atual - ano_nasc
if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")
