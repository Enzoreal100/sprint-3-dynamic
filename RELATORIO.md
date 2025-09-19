# Sistema de Controle de Insumos para Unidades de Diagnóstico

**Versão:** 1.0

## 1. Descrição do Projeto

Este projeto é uma simulação de um sistema de back-end para controle de insumos em unidades de diagnóstico. O objetivo é demonstrar o uso de estruturas de dados e algoritmos clássicos para registrar, consultar e organizar dados de consumo diário de materiais de laboratório, conforme especificado no arquivo `specs.md`.

A implementação foi consolidada em um único arquivo Python (`main.py`) e utiliza estruturas de dados nativas para uma abordagem minimalista e focada nos algoritmos.

## 2. Como Executar

### Pré-requisitos
- Python 3.x

### Execução

Todo o código está no arquivo `main.py`. Para executar uma demonstração específica, siga os passos:

1.  Abra o arquivo `main.py`.
2.  Navegue até o final do arquivo, onde se encontram as chamadas de exemplo comentadas.
3.  Descomente a linha da função que você deseja executar (ex: `demonstrar_fila()`).
4.  Salve o arquivo e execute o script a partir do seu terminal:

    ```bash
    python main.py
    ```

O resultado da simulação escolhida será exibido no console.

## 3. Lógica das Funções e Análise de Complexidade

### Estruturas de Dados

#### Fila (Queue) - `demonstrar_fila()`
- **Lógica:** Simula o registro cronológico de consumo (FIFO - First-In, First-Out). Foi implementada usando uma lista (`list`) do Python, onde novos itens são adicionados ao final (`append`) e os itens mais antigos são removidos do início (`pop(0)`).
- **Uso:** Garante que o primeiro insumo a entrar no estoque seja o primeiro a ser processado, essencial para controle de lotes e validades.
- **Complexidade:**
    - `append()` (enfileirar): **O(1)**.
    - `pop(0)` (desenfileirar): **O(n)**, pois todos os elementos subsequentes da lista precisam ser deslocados.

#### Pilha (Stack) - `demonstrar_pilha()`
- **Lógica:** Simula a consulta dos últimos eventos registrados (LIFO - Last-In, First-Out). Foi implementada usando uma lista (`list`), onde os itens são adicionados (`append`) e removidos (`pop`) do final.
- **Uso:** Ideal para operações que precisam acessar o último item registrado, como a funcionalidade de "desfazer" um lançamento ou consultar rapidamente o consumo mais recente.
- **Complexidade:**
    - `append()` (push): **O(1)**.
    - `pop()` (pop): **O(1)**.

### Algoritmos de Busca

#### Busca Sequencial - `busca_sequencial()`
- **Lógica:** Percorre a coleção de dados do início ao fim, comparando cada item com o valor buscado. Retorna todas as ocorrências encontradas.
- **Uso:** É uma busca simples e eficaz para encontrar todos os registros de um tipo de insumo em uma lista não ordenada. Útil para relatórios completos de consumo por item.
- **Complexidade:** **O(n)**, pois no pior caso, precisa percorrer toda a lista.

#### Busca Binária - `busca_binaria()`
- **Lógica:** Opera sobre uma **lista ordenada**. A cada passo, compara o valor buscado com o elemento no meio da coleção. Se não for o elemento, descarta metade da coleção e repete o processo na metade restante.
- **Uso:** Extremamente eficiente para encontrar um item em uma lista grande. Foi usada para localizar um insumo por seu ID após a ordenação da lista, demonstrando uma otimização significativa.
- **Complexidade:** **O(log n)**, pois o espaço de busca é dividido pela metade a cada iteração.

### Algoritmos de Ordenação

#### Merge Sort - `merge_sort()`
- **Lógica:** É um algoritmo de "dividir para conquistar". Ele divide recursivamente a lista pela metade até que cada sublista contenha um único elemento. Em seguida, combina (mescla) as sublistas, ordenando-as durante o processo.
- **Uso:** Garante uma ordenação estável e eficiente. Foi usado para ordenar os insumos por `quantidade`.
- **Complexidade:** **O(n log n)** em todos os casos (pior, médio e melhor), pois a lista é sempre dividida da mesma maneira.

#### Quick Sort - `quick_sort()`
- **Lógica:** Também usa "dividir para conquistar". Escolhe um elemento como pivô e particiona os outros elementos em dois grupos: os menores que o pivô e os maiores que o pivô. O processo é repetido recursivamente para os dois grupos.
- **Uso:** Geralmente mais rápido na prática que o Merge Sort (devido a constantes e cache), mas seu desempenho no pior caso é inferior. Foi usado para ordenar os insumos por `validade`.
- **Complexidade:**
    - **Caso Médio:** **O(n log n)**.
    - **Pior Caso:** **O(n^2)**, que ocorre quando o pivô escolhido é consistentemente o menor ou o maior elemento da lista/sublista (ex: em uma lista já ordenada ou inversamente ordenada).