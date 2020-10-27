# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a {0}º nota do aluno: ".format(1)));
nota2 = float(input("Digite a {0}º nota do aluno: ".format(2)));
nota3 = float(input("Digite a {0}º nota do aluno: ".format(3)));
nota4 = float(input("Digite a {0}º nota do aluno: ".format(4)));

media = (nota1 + nota2 + nota3 + nota4) / 4;

print("\nA média do aluno é: %.2f" %(media));