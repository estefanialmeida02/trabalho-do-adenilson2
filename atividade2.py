nota1 = float(input("Insira a primeira nota bimestral: "))
nota2 = float(input("Insira a segunda nota bimestral: "))
nota3 = float(input("Insira a terceira nota bimestral: "))
nota4 = float(input("Insira a quarta nota bimestral: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 60:
    print("O aluno foi aprovado com média:", media)
elif media < 60:
    print("O aluno foi reprovado com média:", media)
else:
    print("ERRO")