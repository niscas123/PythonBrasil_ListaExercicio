# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input("Tamanho do arquivo em Megabyte: "));
velocidade = float(input("Velocidade de internet por Megabyte: "));

tamanhoMb = tamanho * 1024;
velocidadeMb = velocidade * 1024;
tempo = tamanhoMb / velocidadeMb;
minutos = tempo / 60;

print("Tempo aproximado de download\n - Velocidade: %.0f MB\n - Minutos: %.2f min " %(velocidade, tempo));