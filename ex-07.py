#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salario=int(input("Digite seu salário atual: "))
percentual=int(input("Digite o percentual de reajuste: "))
reajuste=salario+(salario*percentual/100)
print("Seu novo salário será de:", reajuste)
