#9) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

carro=float(input("Qual é o custo de fábrica do carro? "))
carro_distribuidora = carro * 0.28
carro_imposto = carro * 0.45
carro_final = carro + carro_distribuidora + carro_imposto
print("O valor final do carro para o consumidor será de R$", f"{carro_final:.2f}")
