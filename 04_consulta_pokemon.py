import csv
import os
"""
CONSULTA POKEMON

1 - Baixar o seguinte arquivo CSV que contém dados dos pokemons existentes:
https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon.csv

2 - Criar um script python que :

A) Leia o arquivo CSV e armazene em um dicionário (python dict) os seguintes atributos:
    - id
    - identifier (nome)
    - base_experience (xp)
    - weight (peso)
    - height (altura)
(nesse dicionário, o "id" deverá ser a chave)
"""
#__import__('ipdb').set_trace()
with open('pokemon.csv', 'r') as pokemon:
    dados_pokemon = csv.reader(pokemon)
    next(dados_pokemon)
    pokedex = {}
    
    for atributos in dados_pokemon:
        id = int(atributos[0])
        nome = atributos[1]
        altura = float(atributos[3])
        peso = float(atributos[4])
        xp = int(atributos[5])


        pokedex[id] = {'nome': nome, 'altura': altura, 'peso': peso, 'xp': xp}

    # print(pokedex)


"""
B) Após armazenar no dicionário, pedir para que o usuário selecione um desses 3 atributos:
    - base_experience (xp)
    - weight (peso)
    - height (altura)
"""
opcoes = ['xp', 'peso', 'altura']
print('Escolha uma opção de atributo: 1-XP, 2-Peso ou 3-Altura')

for opcao in range(len(opcoes)):
    print(f'{opcao+1}.{opcoes[opcao]}')

opcao_selecionada = int(input('Selecione uma opção:'))

if opcao_selecionada < 1 or opcao_selecionada > len(opcoes):
    print('Opção inválida!')
else:
    opcao = opcoes[opcao_selecionada-1]
    print(f'Opção selecionada: {opcao}')

"""
C) Após selecionar o atributo, pedir para que ele digite um valor mínimo para esse atributo.
EXEMPLO: se ele selecionar o atributo "peso" e o valor "50".
"""
valor_minimo = float(input(f'Digite um valor mínimo para {opcao}: '))

print(f'Valor mínimo para {opcao}: {valor_minimo}')

"""
O programa deverá então percorrer o dicionário e:

D) Deverá imprimir na tela o identifier (nome) de todos os pokemons que tem o valor do atributo selecionado (peso) igual ou maior do que o que foi informado pelo usuário (50).
"""

pokemon_filtrados = []
for pokemon in pokedex.values():
    if pokemon[opcao] >= valor_minimo:
        print(pokemon['nome'], pokemon[opcao])
        pokemon_filtrados.append(pokemon)

if not pokemon_filtrados:
    print('Não foi encontrado Pokémon com o valor de atributo digitado.')

"""

E) Gravar um arquivo CSV com todos os pokemons que tem o valor do atributo (peso) igual ou maior do que o que foi informado pelo usuário (50). O arquivo CSV deve ter as seguintes colunas:
    - id
    - identifier (nome)
    - base_experience (xp)
    - weight (peso)
    - height (altura)
"""
nome_arquivo = f'pokemon_{opcao}_{valor_minimo}.csv'
with open(nome_arquivo, 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['id', 'identifier', 'base_experience', 'weight', 'height'])

    for pokemon in pokemon_filtrados:
        writer.writerow([list(pokedex.keys())[list(pokedex.values()).index(pokemon)],
                            pokemon['nome'], pokemon['xp'], pokemon['peso'], pokemon['altura']])
        
"""
F) Mostrar uma mensagem para o usuário (usando o comando print) o caminho completo para o arquivo CSV que foi gravado.

"""
print(f'O arquivo CSV foi salvo em: {os.path.abspath(nome_arquivo)}')
