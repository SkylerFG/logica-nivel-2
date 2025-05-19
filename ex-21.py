#21) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

horas_trabalhadas = int(input("Digite quantas horas trabalho no mês: "))
salario_hora= float(input("Digite seu salário por hora: "))
if horas_trabalhadas >= 160:
    horas_extras=horas_trabalhadas - 160
    salario=(horas_trabalhadas-horas_extras)*salario_hora+horas_extras*salario_hora*1.5
    print(salario)
else:
    salario = horas_trabalhadas*salario_hora
    print(salario)
