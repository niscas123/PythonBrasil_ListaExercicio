""" 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
        a. Para homens: (72.7*h) - 58
        b. Para mulheres: (62.1*h) - 44.7"""


genero = str(input("Qual o seu genero? "));
h = float(input("Digite sua altura em metros: "));

if(genero == "M") or (genero == "Masculino") or (genero == "masculino"):
    a = (72.7 * h) - 58;
    print("\n - Peso ideal para homens: %.2f kg" %(a));
elif(genero == "F") or (genero == "Feminino") or (genero == "feminino"):
    b = (62.1 * h) - 44.7;
    print("\n - Peso ideal para mulheres: %.2f kg" %(b));
else:
    print("Opção Inválida!");