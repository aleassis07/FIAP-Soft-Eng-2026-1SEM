# %% - Dados
dados_rotas = {"Cuiabá-Manaus": 1753, "Belo Horizonte-Cuiabá": 1373}
dados_km = {1753: ["Cuiabá-Manaus"], 1373: ["Belo Horizonte-Cuiabá"]}

print("ROTAS: DISTÂNCIA:")
for rota in dados_rotas:
    print(rota, dados_rotas.get(rota))
print("\n")

print("DISTÂNCIA (KM): ROTAS")
for km in dados_km:
    print(km, dados_km.get(km))

# %% - Exemplo 1: Dicionário de Rotas (cidade => lista de conexões)
# As conexões (rotas) que cada cidade possui.

dados_rotas = {
    "Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"]
}

for cidade in dados_rotas:
    print("Cidade:", cidade)
    print("Conexões:", dados_rotas[cidade])

# %% - Exemplo 2: Dicionário de Distâncias a partir de Cuiabá
# Destinos possíveis pra quem sai de Cuiabá e as distâncias

dados_km_cuiaba = {
    "Manaus": 1453,
    "Belo Horizonte": 1373
}

for destino in dados_km_cuiaba:
    print(f"DESTINO: {destino}, DISTÂNCIA: {dados_km_cuiaba[destino]}km")

# %% - Exemplo 3: Verificando se uma cidade existe em rotas
# Usado "in" para verificar se a chave "Cuiabá" está presente no dicionário "dados_rotas"

dados_rotas = {
    "Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"]
}

cidades = [i for i in dados_rotas] # praticando list comprehension
if "Cuiabá" in cidades:
    print(f"As rotas de Cuiabá estão presentes nos dados:\n {dados_rotas['Cuiabá']}")

# %% - Exemplo 4: Verificando se um destino existe em dados_km_cuiaba

dados_km_cuiaba = {
    "Manaus": 1453,
    "Belo Horizonte": 1373
}

print("Manaus" in dados_km_cuiaba)

# %% - Exemplo 5: Verificando quantas cidades existe no grafo
# Grafo é a estrutura formada a partir das conexões existentes entre as cidades, através das rotas.
# Ao usar len() com dicionários, é retornado a quantidade de índices (par chave:valor) do dicionário
# Nesse contexto, cada índice = 1 cidade = 1 vértice do grafo
# Ou seja, cada ponto do grafo é um vértice que, por sua vez, corresponde a 1 cidade.

dados_rotas =  {
    "Cuiabá": ["Belo Horizonte", "Manaus", "Rio de Janeiro"],
    "Belo Horizonte": ["Brasília", "Cuiabá", "São Paulo", "Rio de Janeiro"]
}

print(len(dados_rotas))

# %% - Exemplo 6: Contando destinos a partir de Cuiabá
# Ao rodar o len() em um dicionário que mostra as cidades e suas respectivas distâncias a partir de Cuiabá, vamos saber quantos destinos possíveis existem a partir de Cuiabá

dados_km_cuiaba = {
    "Manaus": 1453,
    "Belo Horizonte": 1373,
    "Rio de Janeiro": 1576
}

print(len(dados_km_cuiaba))