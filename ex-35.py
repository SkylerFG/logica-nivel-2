#35) Um posto está vendendo combustíveis com a seguinte tabela de descontos: 


#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90. 

combustível=input("Álcool ou Gasolina? ")
if combustível == "Álcool":
    preço= 2.90
    litros=float(input("Quantos litros de álcool vai colocar? "))
    if litros > 20:
        bruto= litros*preço
        desconto= bruto*0.05
        valor_final= bruto-desconto
        print("O valor será:R$ ",f"{valor_final:.2f}")
    else:
        bruto= litros*preço
        desconto= bruto*0.03
        valor_final= bruto-desconto
        print("O valor será:R$ "f"{valor_final:.2f}")
elif combustível == "Gasolina":
    preço= 3.30
    litros=float(input("Quantos litros de gasolina vai colocar? "))
    if litros > 20:
        bruto= litros*preço
        desconto= bruto*0.06
        valor_final= bruto-desconto
        print("O valor será:R$ ",f"{valor_final:.2f}")
    else:
        bruto= litros*preço
        desconto= bruto*0.04
        valor_final= bruto-desconto
        print("O valor será:R$ ",f"{valor_final:.2f}")
