# Sistema de Controle de Insumos para Unidades de Diagnóstico

**Versão:** 1.0 (Implementação Simplificada)

## 1. Descrição do Projeto

Este projeto é uma simulação de um sistema de back-end para controle de insumos em unidades de diagnóstico. O objetivo é demonstrar o uso de estruturas de dados e algoritmos clássicos para registrar, consultar e organizar dados de consumo diário de materiais de laboratório.

A implementação foi consolidada em um único arquivo Python (`main.py`) e utiliza estruturas de dados nativas (listas e `collections.deque`) para uma abordagem minimalista e focada nos algoritmos.

## 2. Funcionalidades Implementadas

- **Geração de Dados:** Criação de uma massa de dados simulada de insumos consumidos.
- **Fila (Queue):** Simulação do registro cronológico de consumo (FIFO - First-In, First-Out) usando `collections.deque`.
- **Pilha (Stack):** Simulação da consulta de últimos eventos (LIFO - Last-In, First-Out) usando `list`.
- **Busca Sequencial:** Localização de todos os registros de um insumo específico.
- **Busca Binária:** Localização rápida de um registro em uma coleção ordenada.
- **Algoritmos de Ordenação:** Implementação de `Merge Sort` and `Quick Sort` para organizar os dados por diferentes critérios (quantidade e data de validade).

## 3. Como Executar

### Pré-requisitos
- Python 3.x

### Execução

Todo o código está no arquivo `main.py`. Dentro do arquivo, existem funções de demonstração para cada funcionalidade principal.

Para executar uma demonstração específica, siga os passos:

1. Abra o arquivo `main.py` em um editor de texto ou IDE.
2. Navegue até o final do arquivo, onde se encontra a seção `CHAMADAS DE EXEMPLO`.
3. Descomente a linha da função que você deseja executar (ex: `demonstrar_fila()`).
4. Salve o arquivo.
5. Execute o script a partir do seu terminal:

   ```bash
   python main.py
   ```

O resultado da simulação escolhida será exibido no console.

## 4. Análise e Justificativa de Uso

- **Fila (`collections.deque`):** Utilizada para simular a ordem de chegada e processamento dos insumos. Garante que o primeiro insumo a entrar no estoque seja o primeiro a ser registrado como consumido, o que é essencial para controle de lotes e validades.
- **Pilha (`list`):** Ideal para operações que precisam acessar o último item registrado, como a funcionalidade de "desfazer" um lançamento ou consultar rapidamente o consumo mais recente.
- **Busca Sequencial:** É uma busca simples e eficaz para encontrar todos os registros de um tipo de insumo em uma lista não ordenada. Útil para relatórios completos de consumo por item.
- **Busca Binária:** Extremamente eficiente para encontrar um item em uma lista grande, **desde que a lista esteja ordenada**. Foi usada para localizar um insumo por seu ID após a ordenação da lista, demonstrando uma otimização significativa em relação à busca sequencial.
- **Merge Sort e Quick Sort:** Ambos são algoritmos de ordenação eficientes. Foram implementados para demonstrar como organizar os dados por critérios de negócio, como `quantidade` (para encontrar os maiores ou menores consumos) ou `validade` (para gerenciar o vencimento de lotes).
