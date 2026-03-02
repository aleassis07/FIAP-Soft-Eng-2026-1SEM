# %% - Exercício 1 — Dicionário com distâncias (saindo de São Paulo)
# Crie um dicionário chamado distancia_sp contendo apenas as distâncias dos voos diretos que saem de São Paulo, de acordo com o mapa:
# 1) Mostre a distância de São Paulo até Curitiba
# 2) Some todas as distâncias do dicionário
# 3) Mostre qual cidade tem a maior distância saindo de São Paulo

distancia_sp = {
    "Belo Horizonte": 490,
    "Salvador": 1454,
    "Curitiba": 339,
    "Porto Alegre": 852
}

if "Curitiba" in distancia_sp:
    distancia_ate_curitiba = distancia_sp["Curitiba"]
distancia_soma = 0
maior_distancia = 0
for i in distancia_sp:
    distancia_soma += distancia_sp[i]
    if distancia_sp[i] > maior_distancia:
        maior_distancia = distancia_sp[i]
        maior_cidade = i

print(f"Distância de São Paulo até Curitiba: {distancia_ate_curitiba}km")
print(f"Soma total das distâncias dentro das rotas com origem em São Paulo: {distancia_soma}km")
print(f"Maior distância dentro das rotas com origem em São Paulo: {maior_distancia}km (rota até {maior_cidade})")

# %% - Exercício 2: Crie um dicionário chamado conexões onde cada cidade guarda uma lista com as cidades conectadas diretamente
# 1) Mostre apenas as conexões de Curitiba
# 2) Verifique se Rio de Janeiro está conectado diretamente a Curitiba

conexoes = {
    "Porto Alegre":  ["Florianópolis", "São Paulo"],
    "Florianópolis": ["Porto Alegre", "Curitiba"],
    "Curitiba": ["Florianópolis", "São Paulo", "Rio de Janeiro"],
    "São Paulo": ["Porto Alegre", "Curitiba", "Salvador", "Belo Horizonte"],
    "Rio de Janeiro": ["Curitiba", "Belo Horizonte", "Cuiabá"],
    "Belo Horizonte": ["São Paulo", "Brasília", "Rio de Janeiro", "Cuiabá"],
    "Brasília": ["Belo Horizonte", "Fortaleza"],
    "Cuiabá": ["Belo Horizonte", "Rio de Janeiro", "Manaus"],
    "Salvador": ["São Paulo", "Fortaleza"],
    "Fortaleza": ["Salvador", "Brasília", "Manaus"],
    "Manaus": ["Fortaleza", "Cuiabá"]
}

if "Curitiba" in conexoes:
    conexoes_Curitiba = conexoes["Curitiba"]
    verificar_RioDeJaneiro = "Rio de Janeiro" in conexoes["Curitiba"]
    if verificar_RioDeJaneiro == True:
        verificar_RioDeJaneiro = "Rio de Janeiro está conectado diretamente à Curitiba."
    else:
        verificar_RioDeJaneiro = "Rio de Janeiro não está conectado à Curitiba."

print("Cidades que fazem conexão com Curitiba: ", *conexoes_Curitiba) # * desempacota a lista, exibindo só os elementos
print(verificar_RioDeJaneiro)

# %% - Exercício 3: Estrutura de grafo simples (parte do mapa)
# Crie um dicionário chamado grafo representando parte do mapa (cidades → lista de vizinhos), usando os dados.
# 1) Mostre as cidades vizinhas de Brasília.
# 2) Conte quantas conexões São Paulo possui.
# 3) Verifique se Porto Alegre está diretamente conectado a Curitiba.

grafo = {
    "Manaus": ["Cuiabá", "Fortaleza"],
    "Fortaleza": ["Manaus", "Salvador", "Brasília"],
    "Salvador": ["Fortaleza", "São Paulo"],
    "Brasília": ["Belo Horizonte", "Fortaleza"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"],
    "Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
    "Rio de Janeiro": ["Belo Horizonte", "Cuiabá", "Curitiba"],
    "São Paulo": ["Belo Horizonte", "Curitiba", "Porto Alegre", "Salvador"],
    "Curitiba": ["Florianópolis", "Rio de Janeiro", "São Paulo"],
    "Florianópolis": ["Curitiba", "Porto Alegre"],
    "Porto Alegre": ["Florianópolis", "São Paulo"]
}

for cidades in grafo:
    if cidades == "Brasília":
        vizinhos_Brasilia = grafo[cidades]
    if cidades == "São Paulo":
        qtde_conexoes_SaoPaulo = len(grafo[cidades])
    verificar_PortoAlegre = "Curitiba" in grafo["Porto Alegre"]
    if verificar_PortoAlegre == True:
        verificar_PortoAlegre = "Porto Alegre está diretamente conectado a Curitiba"
    else:
        verificar_PortoAlegre = "Porto Alegre não está conectado a Curitiba"

print("As cidades vizinhas de Brasílias são:", *vizinhos_Brasilia)
print("São Paulo se conecta com", qtde_conexoes_SaoPaulo, "cidades")
print(verificar_PortoAlegre)