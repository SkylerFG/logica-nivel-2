# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

carro=int(input("Digite o valor do carro: "))
distribuidora=carro*0.28
imposto=carro*0.48
carrofinal=carro+distribuidora+imposto
print("=====Aditivos=====")
print("Distribuidora: R$",distribuidora)
print("Impostos: R$",imposto)
print("Valor final do carro: R$",carrofinal)
