# %%
# 1) Crie uma lista com 5 números inteiros.
# Mostre o primeiro e o último elemento da lista.
lista = [1, 2, 3, 4, 5]
print(lista[0], lista[4])
print(lista[-5], lista[-1]) # forma alternativa

# %%
# 2) Crie uma lista com 4 nomes.
# Altere o terceiro nome da lista e mostre a lista atualizada.
lista = ['Alberto', 'Juliana', 'Nathan', 'Eliézer']
lista.pop(2)
lista.insert(2, "Alex")
print(lista)

# %%
# 3) Crie uma lista com 3 números.
# Adicione dois novos números ao final da lista.
# Mostre o resultado final.
lista = [25, 28, 34]
novos_numeros = [37, 41]
lista = lista + novos_numeros
print(lista)

# %%
# 4) Crie uma lista com 6 números.
# Remova o segundo elemento da lista.
# Depois remova o último elemento.
# Mostre a lista final
lista = [111, 222, 333, 444, 555, 666]
lista.pop(-5)
lista.pop(-1)
print(lista)

# %%
# 5) Crie uma lista com 5 números fora de ordem.
# Ordene a lista em ordem crescente e mostre o resultado
lista = [100, 7, 2, 9, 1]
lista.sort()
print(lista)

# %%
# 6) Crie uma lista com 5 números.
# Percorra a lista e mostre cada número multiplicado por 3.
lista = [1, 2, 3, 4, 5]
numeros_multiplicados = [i*3 for i in lista]
print(numeros_multiplicados)