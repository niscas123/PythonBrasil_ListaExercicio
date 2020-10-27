# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o tamanho do lado do quadrado: "));

area = lado * lado;
dobro_area = area * 2;

print("\nA área do quadrado é: %2.f\nO dobro da área do quadrado é: %2.f" %(area, dobro_area));