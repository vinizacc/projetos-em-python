entrada = input("Digite a operação desejada: ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if( entrada == "+"):
    resultado  = n1 + n2
elif( entrada == "-"):
    resultado  = n1 - n2
elif( entrada == "*"):
    resultado  = n1 * n2
elif( entrada == "/"):
    resultado  = n1 / n2
elif( entrada == "%"):
    resultado  = n1 % n2
elif( entrada == "**"):
    resultado  = n1 ** n2

if(entrada == "%"):
    entrada = "modulo"
elif( entrada == "**"):
    entrada = "exponencial"

print(f"{n1} {entrada} {n2} = {resultado}")