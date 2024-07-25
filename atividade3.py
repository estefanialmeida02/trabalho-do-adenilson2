print("-------------------------")
print("É positivo ou negativo")
print("-------------------------")
N= float(input(" Digite o primeiro número para a verificação: "))

if N > 0:
    print("O numero é positivo")
    print("-----------")
    print(" FIM DA VERIFICAÇÃO ")
    print("-----------")
elif N < 0:
    print("O numero é negativo")
    print("-----------")
    print(" FIM DA VERIFICAÇÃO ")
    print("-----------")

elif N == 0:
    print("O numero é igual a zero")
    print("-----------")
    print(" FIM DA VERIFICAÇÃO ")
    print("-----------")
else:
    print("apenas numero")
    print("-----------")
    print("  FIM DA VERIFICAÇÃO ")
    print("-----------")