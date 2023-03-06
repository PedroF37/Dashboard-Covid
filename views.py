# -------------------------------------------------------------------------- #
# IMPORTAÇÕES


import requests
import pandas as pd
import numpy as np


# -------------------------------------------------------------------------- #
# CONSULTA/RESPOSTA DA API


url = "https://covid-193.p.rapidapi.com/statistics"

# Sua chave da API aqui.
headers = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

response_list = [
    [
        info['continent'], info['country'], info['cases']['total'],
        info['cases']['active'], info['cases']['recovered'],
        info['deaths']['total'], info['day']
    ] for info in response['response']
]


# -------------------------------------------------------------------------- #
# DATAFRAME


df = pd.DataFrame(
    response_list, columns=[
        'Continente', 'País', 'Casos',
        'Recuperados', 'Casos Ativos', 'Mortes', 'Data'
    ]
)


# -------------------------------------------------------------------------- #
# DADOS PARA GRÁFICO PIE


# Organizando dados por Continente
total_df = df.groupby(['Continente']).sum()

# Adicionando index
total_df['Nome'] = total_df.index

# Convertendo DataFrame em dicionario
total_dict = total_df.to_dict('recorde')

# Lista que contem os dados
totals = [item for item in total_dict]


# Dados dos Continentes (para o gráfico pie)
values_continent_list = [
     totals[0]['Casos'], totals[2]['Casos'],
     totals[3]['Casos'], totals[4]['Casos'],
     totals[5]['Casos'], totals[6]['Casos']
]

names_continent_list = [
     totals[0]['Nome'], totals[2]['Nome'],
     totals[3]['Nome'], totals[4]['Nome'],
     totals[5]['Nome'], totals[6]['Nome']
]


# -------------------------------------------------------------------------- #
# DADOS PARA TABELA (Treeview)


# Organizando por país
country_df = df.groupby(['País', 'Data']).sum()


# Adicionando index
country_df['Nome'] = country_df.index.get_level_values('País')
country_df['Data'] = country_df.index.get_level_values('Data')

country_df = country_df[['Nome', 'Casos', 'Recuperados', 'Mortes', 'Data']]


# Por algumna razão, os continentes aparecem
# como países. Excluimos.
exclude = [
    'All', 'Africa', 'Asia',
    'Europe', 'Oceania', 'South-America',
    'North-America'
]

country_list = [
    [
        item[0], f'{item[1]:,.0f}', f'{item[2]:,.0f}',
        f'{item[3]:,.0f}', item[4]
    ] for item in country_df.values.tolist()
    if item[0] not in exclude
]


# -------------------------------------------------------------------------- #
# DADOS PARA GRÁFICO DE BARRA

top_countries_df = country_df[['Nome', 'Casos']]
top_countries_df = top_countries_df.sort_values(
    by=['Casos'],
    ascending=False
)

top_countries = [
    [
        country[0], country[1]
    ] for country in top_countries_df.head(10).values.tolist()
    if country[0] not in exclude
]


top_countries = sorted(top_countries, key=lambda x: x[1])


# -------------------------------------------------------------------------- #
