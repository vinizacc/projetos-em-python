a = "Escrita de strings em Python"
tamanhoDaString = len(a)
primeiraletraMaiuscula = a.capitalize()

b = "String em Python"
#b.count(escrito) = quantas vezes a palavra "escrito" aparece na string "b"
b.count("Escrito")

c = "Outra string em Python"
#c retorna True pois existe em Outra em c
c.startswith("Outra")

d = "ESPADA LARGA DE FOGO + 15"
input(d.lower())

e = "espada gêmea de gelo e caos"
input(e.upper())

f = " Nome Sobre Nome "
input(f.strip())

g = "Souls like games são melhores que  jogos de luta"
parte = g.split()
input(parte)

h = "Jogos são hobbies interessantes"
frase = ', '.join(h)
input(frase)

i = "Darksouls 1 é o melhor soulslike game"
j = "Bloodborne"
nova = i.replace("Darksouls 1", j)
input(nova)
