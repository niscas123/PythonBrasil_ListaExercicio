# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Quanto você ganha por hora? "));
hora_trabalhada = float(input("Quantas horas você trabalha? "));

salario_bruto = ganho_hora * hora_trabalhada;

print("\nO seu salário mensal é de: R$ {0}".format(salario_bruto));

