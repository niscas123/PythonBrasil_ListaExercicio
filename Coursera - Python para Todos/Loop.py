contador = 0;
soma = 0;

print("A tabela abaixo está separando as colunas como:\ncontador | coisa | contador + coisa");
print("Antes", contador);
for valor in [9, 41, 12, 3, 74, 15]:
    contador += 1;
    soma += valor;
    print("{0} | {1} | {2}".format(contador, valor, soma));
print("Depois", contador, valor, soma, int(soma / contador));