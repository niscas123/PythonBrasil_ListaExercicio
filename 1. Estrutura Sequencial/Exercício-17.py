""" 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    º comprar apenas latas de 18 litros;
    º comprar apenas galões de 3,6 litros;
    º misturar latas e galões, de forma que o desperdício de tinta seja menor. 
      Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""

metros = float(input("Digite o tamanho da área a ser pintado, em metros: "));

litros = int(metros / 6);

preco_litros = 80.0;
capacidade_litros = 18;

preco_galao = 25.0;
capacidade_galao = 3.6;

latas = litros / capacidade_litros;
preco_latas = latas * preco_litros;

galao = litros / capacidade_galao;
preco_galao = galao * preco_galao;

resto_latas = litros % 18;
resto_galao = litros % 3.6;

print("\n -- PREÇO DAS TINTAS SEM DESPERDÍCIO -- \nLatas: %.0f \nValor: R$%.2f \nGalão: %.0f \nValor: R$%.2f" %(latas, preco_latas, galao, preco_galao));

if(resto_latas != 0 or resto_galao != 0):
  latas += 1;
  galao += 1;
  acrescimo_latas = preco_latas * 0.10;
  acrescimo_galao = preco_galao * 0.10;
  preco_latas_acrescimo = preco_latas + acrescimo_latas;
  preco_galao_acrescimo = preco_galao + acrescimo_galao;

print("\n -- DESPERDÍCIO DE TINTA -- \nResto de litros nas latas: %.2fL \nResto de litros no galão: %.2fL" %(resto_latas, resto_galao));
print("\nAcrescimo de desperdício das latas: R$ %.2f \nAcrescimo de desperdício dos galões: R$ %.2f" %(acrescimo_latas, acrescimo_galao));
print("\n -- PREÇOS DAS TINTAS COM DESPERDÍCIO -- \nLatas: %.0f \nValor: R$%.2f \nGalão: %.0f \nValor: R$%.2f" %(latas, preco_latas_acrescimo, galao, preco_galao_acrescimo));

