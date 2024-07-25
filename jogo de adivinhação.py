import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Eu escolhi um número aleatório entre 1 e 100.")

    while True:
        try:
            chute = int(input("Por favor, insira seu chute: "))
            tentativas += 1

            if chute < numero_secreto:
                print("O número que você inseriu é menor que o número secreto.")
            elif chute > numero_secreto:
                print("O número que você inseriu é maior que o número secreto.")
            else:
                print(f"Parabéns! Você adivinhou o número secreto em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número inteiro.")

jogo_de_adivinhacao()