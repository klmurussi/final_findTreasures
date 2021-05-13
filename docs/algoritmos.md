# Algoritmos utilizados

## Grafos

Foi utilizado grafos como os nós do labirinto da parte de fuga. As arestas do grafo possuiam peso.
	
```python
class Graph:
	def __init__(self):
			self.graph = {}
			self.weights = {}
			self.qtd = 0
			self.treasures = []
			self.total = 0
```

```python
class Node(pygame.sprite.Sprite):
	def __init__(self, num, x, y):
		super().__init__()
		self.image = Images.node
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.num = num
		Sprites.node_list.add(self)
		Sprites.all_sprites_list.add(self)
```

```python
def add_node(self, num, x, y):
		empty_node = Node.Node(num, x, y)
		self.graph[empty_node] = []
		return empty_node
```

```python
def add_edge(self, src, dest, weight):
		if (dest in self.graph[src]):
				return
		self.graph[src].append(dest)
		self.graph[dest].append(src)
		self.weights[(src.num, dest.num)] = weight
		self.weights[(dest.num, src.num)] = weight
		edge = Connection.Connection(
				(src.rect.x+16, src.rect.y+16), (dest.rect.x+16, dest.rect.y+16), weight)
```



## Algoritmos ambiciosos e Grafos (Dijkstra)				

Além disso, foi utilizado o algoritmo de Dijkstra para o menor caminho que além de um algorimo para grafos é um algoritmo ambicioso.

```python
def dijkstra_end(self, start, end):
			distance = {node: inf for node in self.graph}
			visited = {node: False for node in self.graph}
			pq = PriorityQueue()
			distance[start] = 0
			pq.add((0, start))
			for next_node in self.graph[start]:
					initial_weight = self.weights[(start.num, next_node.num)]
					pq.add((initial_weight, next_node))
			while not pq.isEmpty():
					currentVert = pq.delMin()
					visited[currentVert] = True
					if (visited[end]):
							break
					for nextVert in self.graph[currentVert]:
							newDist = distance[currentVert] \
									+ self.weights[(currentVert.num, nextVert.num)]
							if newDist < distance[nextVert]:
									distance[nextVert] = newDist
									pq.decreaseKey(nextVert, newDist)
									pq.add((newDist, nextVert))
			return distance[end]
```

## Programação Dinâmica (Knapsack)

Por último foi utilizado o algoritmo Knapsack de programação dinâmica.

```python
	def k(capacidade, node, qtd):
			#capacidade = int(capatidade)
			K = [[0 for x in range(capacidade+1)] for x in range(qtd+1)]
			for nodeAtual in range(1, qtd+1):
					for pesoAtual in range(1, capacidade+1):
							if pesoAtual >= node[nodeAtual-1].peso:
									K[nodeAtual][pesoAtual] = max(node[nodeAtual-1].premio
																										+ K[nodeAtual-1][pesoAtual -
																																			node[nodeAtual-1].peso],
																										K[nodeAtual-1][pesoAtual])
							else:
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
```


