partida = input("Partida: ").strip().title() #Aceitará prompts com espaço após e com mistura de letras maiúsculas e minúsculas
chegada = input("Chegada: ").strip().title()
if partida== "Sp":
    partida = "São Paulo"
elif chegada == "Sp":
    chegada = "São Paulo"

class Grafo_SP:
    def __init__(self, lines, points):
        self.l = lines #Arestas, conexões informadas
        self.p = points #Vértices informados, municipios
        self.size = len(points) #Quantidade de municipios

    def adjacentes(self, x):
        return self.l[x]

def min_heapify(lista, index):
    n = len(lista)
    # Aqui eu obtenho o que seria na árvore o filho do último nó com filhos, logo esse não tem filhos
    left, right, small = 2 * i + 1, 2 * i + 2, i # "Fórmula" p/conseguir o indice do filho à direita e "fórmula" p/conseguir o indice do filho à esquerda
    #Já a small armazena o último pai da árvore e será substituida, caso um de seus filhos seja menor(representando desordem)
    small = left if left < n and lista[left] < lista[small] else small #Condicionais para caminhar a "árvore" e armazenar o menor
    small = right if right < n and lista[right] < lista[small] else small
    if small != i: #Se o menor foi alterado é porquê um dos filhos foi menor e agora essa variável tem seu index
        lista[i], lista[small] = lista[small], lista[i] #Troco suas posições
        min_heapify(lista, small)
    return small

#Abaixo uso as propriedades da estrutura para ter encontrar antecedentes e descendentes de um nó
def parent(i):
    return (i - 1) // 2

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]

def inserir(heap, item):
    heap.append(item) #Percorro toda a árvore e mantenho as comparações a fim de adicionar no nivel certo para manter as propriedades
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[parent(i)]:
        swap(heap, i, parent(i))
        i = parent(i)

def deletar(heap):
    if len(heap) == 0:
        raise ValueError("Heap vazia!")
    min_item = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    i = 0
    while True:
        smallest = i
        if left_child(i) < len(heap) and heap[left_child(i)] < heap[smallest]:
            smallest = left_child(i)
        if right_child(i) < len(heap) and heap[right_child(i)] < heap[smallest]:
            smallest = right_child(i)
        if smallest == i:
            break
        swap(heap, i, smallest)
        i = smallest
    return min_item


def dijkastra(grafo, fim, retorno, inicio=0):
    global partida
    global chegada
    set_rotas, fila = [], []
    pai = [float('inf')] * grafo.size
    trajeto = [float('inf')] * grafo.size
    trajeto[inicio] = 0
    inserir(fila, [inicio, trajeto[inicio]])
    while len(fila):
        municipio = deletar(fila)
        v1, v2 = municipio[0], municipio[1]
        if v2 <= trajeto[v1]:
            for j in grafo.adjacentes(v1):
                f, s = j[0], j[1]
                if trajeto[f] > trajeto[v1] + s:
                    trajeto[f] = trajeto[v1] + s
                    inserir(fila, [f, trajeto[v1] + s])
                    pai[f] = v1

    caminho(grafo, inicio, fim, pai, retorno, set_rotas)
    print(f"O gasto minimo de uma viagem de {partida} até {chegada} é em cerca de R$ {trajeto[fim]:.2f}")
    return set_rotas


def caminho(grafo, partida, chegada, pai, resposta, set_rotas):
    if partida == chegada:
        set_rotas.append(resposta[chegada])
    else:
        caminho(grafo, partida, pai[chegada], pai, resposta, set_rotas)
        set_rotas.append(resposta[chegada])

txt = open('InterMunicipal_SP.txt', 'r', encoding="utf8")
with txt:
    list, list_r, dict_r, c = [], [], {}, -1
    for i in txt:
        list_r.append(i[0:-1])
    for i in list_r:
        cmd = i.split(",")
        if cmd[0] not in list:
            c += 1
            list.append(cmd[0])
        if cmd[2] not in list:
            c += 1
            list.append(cmd[2])
    dict = {}
    c = -1
    for i in list:
        c += 1
        dict[i] = c
    c = -1
    for i in list:
        c += 1
        dict_r[c] = i

sp = []
for i in range(len(dict_r)):
    sp.append([])

txt = open('InterMunicipal_SP.txt', 'r', encoding="utf8")
with txt:
    list_r = []
    for i in txt:
        list_r.append(i[0:-1])
for i in list_r:
    cmd = i.split(',')
    chave = dict[cmd[0]]
    key = dict[cmd[2]]
    v = float(cmd[1])
    sp[chave].append([key, v])
    sp[key].append([chave, v])

lines = sp
points = []
for i in range(len(lines)):
    points.append(i)

grafo = Grafo_SP(lines, points)


termo = dict[partida]
index = dict[chegada]

v = dijkastra(grafo, termo, dict_r, index)

for x in reversed(v):
    if not x == v[0]:
        print(f"{x}", end="---> ")
    else:
        print(x, end= " ")
