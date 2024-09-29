alunos = {}


def add_aluno():
    nome = input("nome do aluno: ")
    if nome not in alunos:
        alunos[nome] = {'notas': [], 'frequencia': 0}
    else:
        print("erro: aluno já existe!")


def remover_aluno():
    nome = input("nome do aluno para remover: ")
    if nome in alunos:
        del alunos[nome]
    else:
        print("erro: aluno não encontrado!")


def add_notas():
    nome = input("nome do aluno: ")
    if nome in alunos:
        while len(alunos[nome]['notas']) < 4:
            nota = float(input(f"digite a nota {len(alunos[nome]['notas']) + 1}: "))
            alunos[nome]['notas'].append(nota)
            if len(alunos[nome]['notas']) == 4:
                print("notas inseridas com sucesso.")
                break
    else:
        print("erro: aluno não encontrado!")


def add_frequencia():
    nome = input("nome do aluno: ")
    if nome in alunos:
        alunos[nome]['frequencia'] = int(input("digite a frequência (número de aulas): "))
    else:
        print("erro: aluno não encontrado!")


def editar_aluno():
    nome = input("nome do aluno para editar: ")
    if nome in alunos:
        opcao_edicao = input("deseja editar o nome (1), as notas (2) ou a frequência (3)? ")

        if opcao_edicao == '1':
            novo_nome = input("Novo nome: ")
            alunos[novo_nome] = alunos.pop(nome)
            print(f"nome alterado para {novo_nome}.")

        elif opcao_edicao == '2':
            alunos[nome]['notas'] = []
            while len(alunos[nome]['notas']) < 4:
                nota = float(input(f"digite a nota {len(alunos[nome]['notas']) + 1}: "))
                alunos[nome]['notas'].append(nota)
            print("notas atualizadas.")

        elif opcao_edicao == '3':
            alunos[nome]['frequencia'] = int(input("digite a nova frequência (número de aulas): "))
            print("frequência atualizada.")

        else:
            print("erro: opção inválida.")
    else:
        print("erro: aluno não encontrado!")


def imprimir_notas(notas):
    i = 0
    while i < len(notas):
        if i == len(notas) - 1:
            print(notas[i], end=" ")
        else:
            print(notas[i], end=" / ")
        i += 1


def calcular_situacao(aluno, carga_horaria):
    media = sum(aluno['notas']) / 4
    presenca = aluno['frequencia'] / carga_horaria * 100

    if presenca < 75:
        return "reprovado por falta"
    return "aprovado" if media >= 7 else "reprovado por Nota"


def imprimir_relatorio(carga_horaria):
    i = 1
    while i <= len(alunos):
        nome, info = list(alunos.items())[i - 1]
        situacao = calcular_situacao(info, carga_horaria)
        print(f"{i}. {nome} - nota(s): ", end="")
        imprimir_notas(info['notas'])
        print(f"/ frequência: {info['frequencia']} aulas - ({situacao})")
        i += 1


def imprimir_relatorio_filtrado(carga_horaria):
    filtro = input("Filtrar por (Aprovado, Reprovado por Falta, Reprovado por Nota): ").lower()

    if filtro not in ["aprovado", "reprovado por falta", "reprovado por nota"]:
        print("erro: opção inválida!")
        return

    i = 1
    while i <= len(alunos):
        nome, info = list(alunos.items())[i - 1]
        situacao = calcular_situacao(info, carga_horaria).lower()
        if situacao == filtro:
            print(f"{i}. {nome} - nota(s): ", end="")
            imprimir_notas(info['notas'])
            print(f"/ frequência: {info['frequencia']} aulas - ({situacao.capitalize()})")
        i += 1


def sistema_academico():
    carga_horaria = int(input("carga horaria da disciplina: "))

    while True:
        opcao = input(
            "\n1. adicionar aluno\n2. editar aluno\n3. remover aluno\n4. adicionar notas\n5. adicionar frequencia\n6. relatório geral\n7. relatório filtrado\n0. sair\nescolha: ")

        if opcao == '1':
            add_aluno()
        elif opcao == '2':
            editar_aluno()
        elif opcao == '3':
            remover_aluno()
        elif opcao == '4':
            add_notas()
        elif opcao == '5':
            add_frequencia()
        elif opcao == '6':
            imprimir_relatorio(carga_horaria)
        elif opcao == '7':
            imprimir_relatorio_filtrado(carga_horaria)
        elif opcao == '0':
            break
        else:
            print("erro: opção invalida")


sistema_academico()