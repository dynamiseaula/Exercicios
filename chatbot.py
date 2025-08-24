print("===========Bem vindo ao Chatbot Dynamis===========")
print("O que você quer conversar hoje?")

respostas = {
    "oi": "Olá, tudo bem?",
    "como vai?": "Vou bem e você?"
}

while True:
    pergunta = input("Você: ")

    if pergunta == "sair":
        print("Obrigado pela conversa!")
        break

    if pergunta in respostas:
        print("Chat: ", respostas[pergunta])
    else:
        print("Opa, eu não consigo responder isso ainda!")