
# Lista de triplas com nome, peso e altura de pessoas
pessoas = [
    ("João", 70.5, 1.75),
    ("Maria", 60.0, 1.65),
    ("Carlos", 85.0, 1.80),
    ("Ana", 55.0, 1.60),
    ("Pedro", 90.0, 1.85)
]
f = lambda x,y : (x / (y**2))

for nome, peso, altura in pessoas:
    imc = f(peso, altura)  
    print(f"{nome}: IMC = {imc:.2f}")