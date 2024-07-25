idade = int(input("Digite sua idade: "))

if idade < 1:
    print("Bebê")
elif 1 <= idade < 12:
    print("Criança")
elif 12 <= idade < 18:
    print("Adolescente")
elif 18 <= idade < 30:
    print("Adulto jovem")
elif 30 <= idade < 60:
    print("Adulto")
elif 60<= idade < 122:
    print("Idoso")
else:
    print("Você morreu")