""" 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
    1. salário bruto.
    2. quanto pagou ao INSS.
    3. quanto pagou ao sindicato.
    4. o salário líquido.
    5. calcule os descontos e o salário líquido, conforme a tabela abaixo:"""
ganho_hora = float(input("Você ganha quanto por hora? "));
hora_trabalhada = float(input("Quantas horas voê trabalhou por mês? "));

salario_bruto = ganho_hora * hora_trabalhada;
ir = salario_bruto * 0.11;
inss = salario_bruto * 0.08;
sindicato = salario_bruto * 0.05;
impostos = ir + inss + sindicato;
salario_liquido = salario_bruto - impostos;

print("\n + Salário Bruto: R${0} \n - IR (11%): R${1} \n - INSS (8%): R${2} \n - Sindicato (5%): R${3} \n = Salário Líquido: R${4}".format(salario_bruto, ir, inss, sindicato, salario_liquido));

