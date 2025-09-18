import random
import datetime
import collections

def gerar_dados(n):
    insumos = []
    nomes_insumos = ["Tubo de coleta a vácuo (tampa vermelha)", "Tubo de coleta a vácuo (tampa roxa)", "Agulha de coleta a vácuo", "Álcool 70%", "Algodão", "Curativo adesivo", "Luvas de procedimento"]
    for i in range(n):
        insumo = {
            "id_insumo": f"REAG-{random.randint(1, 10):03d}",
            "nome_insumo": random.choice(nomes_insumos),
            "quantidade": random.randint(1, 100),
            "timestamp_consumo": datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30)),
            "validade": datetime.date.today() + datetime.timedelta(days=random.randint(30, 365))
        }
        insumos.append(insumo)
    return sorted(insumos, key=lambda x: x["timestamp_consumo"])

def busca_sequencial(lista, id_insumo):
    encontrados = []
    for insumo in lista:
        if insumo["id_insumo"] == id_insumo:
            encontrados.append(insumo)
    return encontrados

def busca_binaria(lista_ordenada, valor, chave="id_insumo"):
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio][chave] == valor:
            return lista_ordenada[meio]
        elif lista_ordenada[meio][chave] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

def merge_sort(lista, criterio):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda, criterio)
        merge_sort(direita, criterio)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i][criterio] < direita[j][criterio]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

def quick_sort(lista, criterio):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        menores = [x for x in lista if x[criterio] < pivo[criterio]]
        iguais = [x for x in lista if x[criterio] == pivo[criterio]]
        maiores = [x for x in lista if x[criterio] > pivo[criterio]]
        return quick_sort(menores, criterio) + iguais + quick_sort(maiores, criterio)

def demonstrar_fila():
    print("\n--- Demonstração de Fila (FIFO) ---")
    dados = gerar_dados(5)
    fila = collections.deque(dados)
    print("Fila inicial (5 insumos):")
    for item in fila:
        print(f"  - {item['nome_insumo']} (Consumido em: {item['timestamp_consumo']})")

    print("\nProcessando 2 insumos (os mais antigos)...")
    primeiro = fila.popleft()
    segundo = fila.popleft()
    print(f"Processado: {primeiro['nome_insumo']}")
    print(f"Processado: {segundo['nome_insumo']}")

    print("\nAdicionando 1 novo insumo...")
    novo_insumo = gerar_dados(1)[0]
    fila.append(novo_insumo)
    print(f"Adicionado: {novo_insumo['nome_insumo']}")

    print("\nFila final:")
    for item in fila:
        print(f"  - {item['nome_insumo']} (Consumido em: {item['timestamp_consumo']})")

def demonstrar_pilha():
    print("\n--- Demonstração de Pilha (LIFO) ---")
    dados = gerar_dados(5)
    pilha = dados
    print("Pilha inicial (5 insumos):")
    for item in pilha:
        print(f"  - {item['nome_insumo']} (Consumido em: {item['timestamp_consumo']})")

    print("\nConsultando os 2 últimos insumos registrados...")
    ultimo = pilha.pop()
    penultimo = pilha.pop()
    print(f"Consultado: {ultimo['nome_insumo']} (o mais recente)")
    print(f"Consultado: {penultimo['nome_insumo']}")

    print("\nPilha final:")
    for item in pilha:
        print(f"  - {item['nome_insumo']} (Consumido em: {item['timestamp_consumo']})")

def demonstrar_buscas():
    print("\n--- Demonstração de Buscas ---")
    dados = gerar_dados(15)
    id_para_buscar = "REAG-005"
    print(f"Gerados 15 registros. Buscando todas as ocorrências do ID: {id_para_buscar}\n")

    # Busca Sequencial
    print("1. Busca Sequencial:")
    resultados_sequencial = busca_sequencial(dados, id_para_buscar)
    if resultados_sequencial:
        print(f"  Encontrados {len(resultados_sequencial)} registros para o ID {id_para_buscar}:")
        for item in resultados_sequencial:
            print(f"    - {item['nome_insumo']}, Quantidade: {item['quantidade']}")
    else:
        print(f"  Nenhum registro encontrado para o ID {id_para_buscar}.")

    # Busca Binária
    print("\n2. Busca Binária:")
    # A busca binária requer uma lista ordenada pela chave de busca
    dados_ordenados_por_id = sorted(dados, key=lambda x: x['id_insumo'])
    print(f"  Dados ordenados por 'id_insumo'. Buscando pelo ID: {id_para_buscar}")
    resultado_binaria = busca_binaria(dados_ordenados_por_id, id_para_buscar, chave="id_insumo")
    if resultado_binaria:
        print("  Encontrado:")
        print(f"    - {resultado_binaria['nome_insumo']}, Quantidade: {resultado_binaria['quantidade']}")
    else:
        print(f"  Nenhum registro encontrado para o ID {id_para_buscar}.")

def demonstrar_ordenacao():
    print("\n--- Demonstração de Ordenação ---")
    dados = gerar_dados(10)
    print("Dados originais (10 registros):")
    for item in dados:
        print(f"  - {item['nome_insumo']}, Quantidade: {item['quantidade']}, Validade: {item['validade']}")

    # Merge Sort por Quantidade
    print("\n1. Merge Sort por 'quantidade' (crescente):")
    dados_merge_qtde = merge_sort(dados[:], 'quantidade')
    for item in dados_merge_qtde:
        print(f"  - Quantidade: {item['quantidade']}, Nome: {item['nome_insumo']}")

    # Quick Sort por Validade
    print("\n2. Quick Sort por 'validade' (crescente):")
    dados_quick_validade = quick_sort(dados[:], 'validade')
    for item in dados_quick_validade:
        print(f"  - Validade: {item['validade']}, Nome: {item['nome_insumo']}")

# Descomente a linha da função que deseja executar

# demonstrar_fila()
# demonstrar_pilha()
# demonstrar_buscas()
# demonstrar_ordenacao()