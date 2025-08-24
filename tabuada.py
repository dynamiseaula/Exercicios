import random

numero1 = random.randint(0, 10)
numero2 = random.randint(0, 10)

resposta = int(input(f"Quanto é {numero1} x {numero2}? "))

resultado = numero1 * numero2

if resposta == resultado:
    print("Ebaa, você acertou!")
else:
    print("Oh não, você errou!")