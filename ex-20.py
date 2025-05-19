#20) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

inicio=int(input("Qual é a hora do inicio do jogo? "))
final=int(input("Qual é a hora do fim do jogo? "))
if inicio > final:
    duracao= 24 - (inicio - final)
else:
    duracao= final - inicio
print ("A duração do jogo foi de", duracao, "horas")
