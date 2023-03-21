import csv
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

    print(pokedex)


"""
B) Após armazenar no dicionário, pedir para que o usuário selecione um desses 3 atributos:
    - base_experience (xp)
    - weight (peso)
    - height (altura)

C) Após selecionar o atributo, pedir para que ele digite um valor mínimo para esse atributo.

EXEMPLO: se ele selecionar o atributo "peso" e o valor "50".

O programa deverá então percorrer o dicionário e:

D) Deverá imprimir na tela o identifier (nome) de todos os pokemons que tem o valor do atributo selecionado (peso) igual ou maior do que o que foi informado pelo usuário (50).

E) Gravar um arquivo CSV com todos os pokemons que tem o valor do atributo (peso) igual ou maior do que o que foi informado pelo usuário (50). O arquivo CSV deve ter as seguintes colunas:
    - id
    - identifier (nome)
    - base_experience (xp)
    - weight (peso)
    - height (altura)

F) Mostrar uma mensagem para o usuário (usando o comando print) o caminho completo para o arquivo CSV que foi gravado.
"""
