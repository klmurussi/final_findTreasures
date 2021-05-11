def knapsack(capacidade, node, qtd):
    capacidade = int(capactidade)
    K = [[0 for x in range(capacidade+1)] for x in range(qtd+1)]
    for nodeAtual in range(1, qtd+1):
        for volumeAtual in range(1, capacidade+1):
            if volumeAtual >= node[nodeAtual-1].volume:
                """ caso o volume atual da iteração seja maior do que o volume do objeto atual """
                """ realiza o calculo da equação de Bellman, selecionando o maior entre o """
                """ o valor para o objeto anterior naquele volume, ou a adição do novo objeto """
                """ removendo o seu volume do volume atual """
                K[nodeAtual][volumeAtual] = max(node[nodeAtual-1].valor
                                                  + K[nodeAtual-1][volumeAtual -
                                                                     node[nodeAtual-1].volume],
                                                  K[nodeAtual-1][volumeAtual])
            else:
                """ caso o volume atual da iteração seja menor do que o volume do objeto atual """
                """ seleciona o valor do objeto anterior para aquele volume pois não é """
                """ possível adicionar outro objeto"""
                K[nodeAtual][volumeAtual] = K[nodeAtual-1][volumeAtual]
    res = findSolution(node, K, qtd, capacidade)
    return (K[qtd][capacidade], res[0], res[1])


def findSolution(objetos, K, qtdObj, capacidade):
    res = K[qtdObj][capacidade]
    print(res)
     
    cap = capacidade
    resObjs = Objetos()
    for i in range(qtdObj, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][cap]:
            continue
        else:
            resObjs.add(objetos[i-1])
            res = res - objetos[i-1].valor
            cap = cap - objetos[i-1].volume
    return (resObjs, cap)