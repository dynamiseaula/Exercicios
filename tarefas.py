
tarefas = []

def desenhar_menu():
    print("Menu:")
    print("[1] - Listar tarefas")
    print("[2] - Adicionar tarefa")
    print("[3] - Excluir tarefa")


def adicionar_tarefa():
    tarefa = input("Qual a sua tarefa? ")
    tarefas.append(tarefa)
    print("Sua tarefa foi adicionada com sucesso!")

def listar_tarefas():

    if len(tarefas) > 0:
        print("Estou listando suas tarefas:")
        for posicao, tarefa in enumerate(tarefas):
            print(f"{posicao} - {tarefa}")
    else:
        print("Não tem tarefas disponiveis!")

def excluir_tarefas():

    if len(tarefas) > 0:
        listar_tarefas()
        tarefa_para_excluir = int(input("Qual tarefa você deseja excluir?"))
        tarefas.pop(tarefa_para_excluir)
    else:
        print("Não tem tarefas disponiveis!")


while True:

    desenhar_menu()
    opcao = input("Qual comando você quer executar? ")

    print("=========================================")

    if opcao == "1":
        listar_tarefas()
    elif opcao == "2":
        adicionar_tarefa()
    elif opcao == "3":
        excluir_tarefas()
    elif opcao == "4":
        print("Saindo do sistema... obrigado!")
        break
    else:
        print("Não conheço esse comando")

    print("=========================================")