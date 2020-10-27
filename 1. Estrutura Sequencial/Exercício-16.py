# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input("Digite o tamanho da área em metros a ser pintada: "));
litros = metros / 3  # = 66,66666666666667  || int(metros / 3) = 65

preco_litros = 80.0;
capacidade_litros = 18;

latas = litros / capacidade_litros;  # = 3,703703703703704  || int(litros / capacidade_litros) = 3
preco_total = latas * preco_litros;  # = 296,2962962962963  || int(latas * preco_litros) = 240

print("\nVocê usará %.0f latas de tinta.\nO preço total é de: R$%.2f" %(latas, preco_total));

# OBS: O resultado em valor flutuante faz com que esses resultados sejam aredondados para o valor mais próximo do inteiro. 