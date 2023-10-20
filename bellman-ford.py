def bellmanFord(matriz, vOrigem, vDestino):
    n = len(matriz)
    custo = [float('inf')] * n
    rota = [None] * n
    custo[vOrigem] = 0

    for _ in range(n-1):
        for vAtual in range(n):
            for vAdjacente, peso in enumerate(matriz[vAtual]):
                if peso != 0 and custo[vAdjacente] > custo[vAtual] + peso:
                    custo[vAdjacente] = custo[vAtual] + peso
                    rota[vAdjacente] = vAtual

    for vAtual in range(n):
        for vAdjacente, peso in enumerate(matriz[vAtual]):
            if peso != 0 and custo[vAdjacente] > custo[vAtual] + peso:
                return False  # Ciclo de custo negativo encontrado

    caminho = []
    i = vDestino
    while i is not None:
        caminho.append(i)
        i = rota[i]
    caminho.reverse()

    print(caminho, custo[vDestino])
