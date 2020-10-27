""" 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        a. o produto do dobro do primeiro com metade do segundo .
        b. a soma do triplo do primeiro com o terceiro.
        c. o terceiro elevado ao cubo. """

numero_int1 = int(input("Digite o {0}º inteiro: ".format(1)));
numero_int2 = int(input("Digite o {0}º inteiro: ".format(2)));
numero_real = float(input("Digite o número real: "));

a = numero_int1 * 2 * (numero_int2 / 2);
b = numero_int1 * 3 + numero_real;
c = numero_real ** 3;

print("\n - a. O produto do dobro do primeiro com a metade do seundo é:", a,
"\n - b. A soma do triplo do primeiro com o terceiro é:", b,
"\n - c. O terceiro elevado ao cubo é:", c);