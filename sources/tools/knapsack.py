from classes import Graph

def k(capacidade, node, qtd):
    #capacidade = int(capatidade)
    K = [[0 for x in range(capacidade+1)] for x in range(qtd+1)]
    for nodeAtual in range(1, qtd+1):
        for pesoAtual in range(1, capacidade+1):
            if pesoAtual >= node[nodeAtual-1].peso:
                """ caso o peso atual da iteração seja maior do que o peso do objeto atual """
                """ realiza o calculo da equação de Bellman, selecionando o maior entre o """
                """ o premio para o objeto anterior naquele peso, ou a adição do novo objeto """
                """ removendo o seu peso do peso atual """
                K[nodeAtual][pesoAtual] = max(node[nodeAtual-1].premio
                                                  + K[nodeAtual-1][pesoAtual -
                                                                     node[nodeAtual-1].peso],
                                                  K[nodeAtual-1][pesoAtual])
            else:
                """ caso o peso atual da iteração seja menor do que o peso do objeto atual """
                """ seleciona o premio do objeto anterior para aquele peso pois não é """
                """ possível adicionar outro objeto"""
                K[nodeAtual][pesoAtual] = K[nodeAtual-1][pesoAtual]
    res = findSolution(node, K, qtd, capacidade)
    return (res)


def findSolution(treasures, K, qtdObj, capacidade):
    res = K[qtdObj][capacidade]
    #print(res)
     
    cap = capacidade
    resObjs = Graph.Graph()
    for i in range(qtdObj, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][cap]:
            continue
        else:
            resObjs.add(treasures[i-1])
            res = res - treasures[i-1].premio
            cap = cap - treasures[i-1].peso
    return (resObjs)