#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.


brancos=int(input("Quantidade de votos brancos: "))
nulos=int(input("Quantidade de votos nulos: "))
validos=int(input("Quantidade de votos válidos: "))
total=brancos+nulos+validos
percbrancos=brancos/total*100
percnulos=nulos/total*100
percvalidos=validos/total*100
print ("Total de votos:", total)
print ("Percentual de votos brancos: %",percbrancos)
print ("Percentual de votos nulos: %",percnulos)
print ("Percentual de votos válidos: %",percvalidos)
