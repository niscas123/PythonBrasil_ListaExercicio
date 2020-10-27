contador = 0;

print("A tabela abaixo está separando as colunas como:\ncontador | coisa | contador + coisa");
print("Antes", contador);
for coisa in [9, 41, 12, 3, 74, 15]:
    contador += 1;
    print("{0} | {1} | {2}".format(contador, coisa, contador + coisa));
print("Depois", contador);