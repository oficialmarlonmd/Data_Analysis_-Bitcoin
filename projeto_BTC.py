import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
arquivo = "C:\\Users\\Marlon\\Downloads\\data_science\\btcusd_1-min_data.csv"

def carregarDados(file):
    dados = pd.read_csv(file, sep=",")  # armazena o arquivo na memória
    return dados

dados = carregarDados(arquivo)

def tratarDados(dados):
    print(dados.head())  # apresenta as 5 primeiras linhas
    print(dados.info())  # informações das colunas

    dados['Date'] = pd.to_datetime(dados['Timestamp'], unit='s')
    print(dados.head())  # Exibir as 5 primeiras linhas após a conversão
    dados.set_index('Date', inplace=True)

    return dados

# Tratar os dados
dados = tratarDados(dados)

halving_dates = [
    pd.to_datetime('2012-11-28'),  # Primeiro halving
    pd.to_datetime('2016-07-09'),  # Segundo halving
    pd.to_datetime('2020-05-11'),  # Terceiro halving
    pd.to_datetime('2024-04-01')   # Estimativa do próximo halving
]

# Filtrando os dados para o ano de 2024
dados_2024 = dados.loc[dados.index.year == 2024]

# Reamostrando os dados para o fechamento mensal
dados_mensal = dados_2024.resample('M').last()  # Obtendo o preço de fechamento do último dia de cada mês

# Calculando o retorno mensal (variação percentual entre o primeiro e o último dia de cada mês)
dados_mensal['Retorno_Mensal'] = dados_mensal['Close'].pct_change()

# Definir o intervalo de datas para a amostragem trimestral
dados_trimestral_dates = [
    pd.to_datetime('2023-07-01'),  # Início do 3º trimestre de 2023
    pd.to_datetime('2023-10-01'),  # Início do 4º trimestre de 2023
    pd.to_datetime('2024-01-01'),  # Início do 1º trimestre de 2024
    pd.to_datetime('2024-04-01'),  # Início do 2º trimestre de 2024
    pd.to_datetime('2024-07-01')   # Início do 3º trimestre de 2024
]

# Seleção dos dados trimestrais para as datas fornecidas
dados_trimestral = dados[dados.index.isin(dados_trimestral_dates)]

# Cálculo do retorno trimestral
dados_trimestral['Retorno_Trimestral'] = dados_trimestral['Close'].pct_change()

# Definir o intervalo de datas para a amostragem semestral
dados_semestral_dates = [
    pd.to_datetime('2023-07-01'),  # Início do 2º semestre de 2023
    pd.to_datetime('2023-12-31'),  # Final do 2º semestre de 2023
    pd.to_datetime('2024-01-01'),  # Início do 1º semestre de 2024
    pd.to_datetime('2024-07-01')   # Início do 2º semestre de 2024
]

# Seleção dos dados semestrais para as datas fornecidas
dados_semestral = dados[dados.index.isin(dados_semestral_dates)]

# Cálculo do retorno semestral
dados_semestral['Retorno_Semestral'] = dados_semestral['Close'].pct_change()

# Halving
def plot1(dados):
    plt.figure(figsize=(12, 6))
    plt.plot(dados.index, dados['Close'], label='Preço de Fechamento')
    plt.title('Preço de Fechamento do BTC/USD com Halving')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (USD)')

    # Adicionando as linhas de Halving
    for i, halving_date in enumerate(halving_dates):
        if i == 0:
            plt.axvline(x=halving_date, color='r', linestyle='--', label=f'Halving {halving_date.year}')
        else:
            plt.axvline(x=halving_date, color='r', linestyle='--')  # Sem rótulo adicional para evitar duplicatas

    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

# Retorno Mensal
def plot2(dados_mensal):
    plt.figure(figsize=(10, 6))
    plt.plot(dados_mensal.index, dados_mensal['Retorno_Mensal'], marker='o', color='orange', linestyle='-', linewidth=2, markersize=6)
    plt.title("Retorno Mensal do Bitcoin (2024)", fontsize=14)
    plt.xlabel("Mês", fontsize=12)
    plt.ylabel("Retorno (%)", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Retorno Trimestral
def plot3(dados_trimestral):
    plt.figure(figsize=(12, 6))
    plt.plot(dados_trimestral.index, dados_trimestral['Retorno_Trimestral'], marker='o', linestyle='-', color='red')
    plt.title("Retorno Trimestral do Bitcoin (2º Semestre de 2023 e 1º Semestre de 2024)", fontsize=14)
    plt.xlabel("Trimestre", fontsize=12)
    plt.ylabel("Retorno (%)", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Retorno Semestral
def plot4(dados_semestral):
    plt.figure(figsize=(10, 6))
    plt.plot(dados_semestral.index, dados_semestral['Retorno_Semestral'], marker='o', linestyle='-', color='green')
    plt.title("Retorno Semestral do Bitcoin (2º Semestre de 2023 e 1º Semestre de 2024)", fontsize=14)
    plt.xlabel("Semestre", fontsize=12)
    plt.ylabel("Retorno (%)", fontsize=12)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Plotando 
plot1(dados)
plot2(dados_mensal)
plot3(dados_trimestral)
plot4(dados_semestral)