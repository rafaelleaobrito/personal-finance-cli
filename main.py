import json 

ARQUIVO_DADOS = "transacoes.json"

def carregar_transacoes():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)  
    except FileNotFoundError:
        return []  


def salvar_transacoes(transacoes):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(transacoes, f, indent=4, ensure_ascii=False)  



def adicionar_transacao(transacoes, tipo, descricao, valor):
    transacao = {
        "tipo": tipo,  
        "descricao": descricao,  
        "valor": valor  
    }
    transacoes.append(transacao)  


def listar_transacoes(transacoes):
    if not transacoes:  
        print("\nNenhuma transação registrada.\n")
        return
    print("\n--- Lista de Transações ---")
    for i, t in enumerate(transacoes, start=1):
        print(f"{i}. {t['tipo']} - {t['descricao']} : R$ {t['valor']:.2f}")
    print("---------------------------\n")


def calcular_saldo(transacoes):
    saldo = 0
    for t in transacoes:
        if t["tipo"] == "Receita":
            saldo += t["valor"]  
        else:
            saldo -= t["valor"]  
    return saldo

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

def main():
    transacoes = carregar_transacoes()  

    while True:
        print("==== Controle Financeiro ====")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Transações")
        print("4 - Mostrar Saldo")
        print("5 - Salvar e Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da Receita: ")
            valor = float(input("Valor: "))
            adicionar_transacao(transacoes, "Receita", descricao, valor)

        elif opcao == "2":
            descricao = input("Descrição da Despesa: ")
            valor = float(input("Valor: "))
            adicionar_transacao(transacoes, "Despesa", descricao, valor)

        elif opcao == "3":
            listar_transacoes(transacoes)

        elif opcao == "4":
            saldo = calcular_saldo(transacoes)
            print(f"\nSaldo atual: R$ {saldo:.2f}\n")

        elif opcao == "5":
            salvar_transacoes(transacoes)
            print("Dados salvos. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()
