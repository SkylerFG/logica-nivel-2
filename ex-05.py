#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.=

anos=int(input("Digite idade em anos: "))
meses=int(input("Digite idade em meses: "))
dias=(anos*365)+(meses*30)
print("Sua idade em dias é:", dias)
