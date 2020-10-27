# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do círculo: "));

pi = 3.14;

area = pi * (raio * raio);

print("\nO raio do círculo é: %.2fm²" %(area));