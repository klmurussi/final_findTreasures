import random
from tools import Sprites


def edges(graph, start, end):
    all_nodes_non_connected = Sprites.node_list.sprites()
    for i in Sprites.node_list:
        edge_qtt = random.randint(1, 8)
        if edge_qtt == 1:
            edge_qtt = random.randint(1, 8)
        if edge_qtt == 1:
            edge_qtt = random.randint(1, 8)
        #print("source = " + str(i.num))
        for j in range(edge_qtt):
            if not all_nodes_non_connected:
                return
            if possibleToCreate(all_nodes_non_connected, [i, end, start]):
                return
            dest = random.choice(all_nodes_non_connected)
            while dest == i or (i == start and dest == end) or (i == end and dest == start):
                dest = random.choice(all_nodes_non_connected)
            all_nodes_non_connected.remove(dest)
            graph.add_edge(i, dest, random.randint(1, 10))


def possibleToCreate(list, items):
    sA = set(list)
    size = len(list)
    if size > 3:
        return False
    if size == 3:
        sE = set(items)
        return sA.issubset(sE)
    elif size == 2:
        sE1 = set([items[0], items[1]])
        sE2 = set([items[0], items[2]])
        sE3 = set([items[1], items[2]])
        if sA.issubset(sE1):
            return True
        elif sA.issubset(sE2):
            return True
        else:
            return sA.issubset(sE3)
    elif size == 1:
        return list[0] in items