# -*- coding: utf-8 -*-
idade = 30
if (idade >= 18):
    print("Muito nova")
elif (idade == 31 or idade == 32):
    print("Perfeita")
else:
    print("Menor de idade")

contador = 0
while(contador < 6):
    print("Contando WHILE...")
    contador += 1

for i in range(6):
    print("Contando FOR...")
    contador += 1

nomes = ["Ana", "Bia", "Carlos", "Dani"]
for nome in nomes:
    print(nome)