def minDistance(str1: str, str2:str) -> int:
    m = len(str1)
    n = len(str2)
    
    # Inicializando a matriz de distância
    dist = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Inicializando a primeira coluna
    for i in range(1, m + 1):
        dist[i][0] = i
    
    # Inicializando a primeira linha
    for j in range(1, n + 1):
        dist[0][j] = j
    
    # Preenchendo a matriz de distância
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dist[i][j] = min(dist[i - 1][j] + 1,      # Deleção
                             dist[i][j - 1] + 1,      # Inserção
                             dist[i - 1][j - 1] + cost)  # Substituição ou match
    
    return dist[m][n]

print(minDistance("trinitrophenylmethylnitramine", "dinitrophenylhydrazine"))