maior = -1;
print("Antes", maior);
for numero in [9, 41, 12, 3, 74, 15]:
    if(numero > maior):
        maior = numero;
    print(maior, numero);

print("Depois", maior)

pequeno = None;
print("\nAntes", pequeno);
for valor in [9, 41, 12, 3, 74, 15]:
    if(pequeno is None):
        pequeno = valor; # o 9 se torna o valor de pequeno
    elif(valor < pequeno):
        pequeno = valor;
    print(pequeno, " | ", valor);
print("Depois", pequeno);