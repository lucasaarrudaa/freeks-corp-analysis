import random
import numpy as np
import pandas as pd
from IPython.display import display

# Dados históricos
campanhas = ['A', 'B', 'C', 'D']
cpc = [0.05, 0.1, 0.15, 0.1]
impressoes_por_dia = [12484395, 2884615, 6920415, 3885004]
ctr = [0.0089, 0.0120, 0.0102, 0.0198]
tx_conversao = [0.0090, 0.0260, 0.0170, 0.0130]
roi = [1.0, 1.5, 0.8, 0.03]
vendas_dia = [1000, 900, 1200, 1000]
cpa = [5.56, 3.85, 8.82, 7.69]
rpa = [11.11, 9.62, 15.88, 13.08]
lucro_mensal = [166666.67, 155769.21, 254117.64, 161538.47]

class Campanha:
    
    def __init__(self, nome, cpc, impressoes_por_dia, ctr, tx_conversao, roi, vendas_dia, cpa, rpa, lucro_mensal):
        self.nome = nome
        self.cpc = cpc
        self.impressoes_por_dia = impressoes_por_dia
        self.ctr = ctr
        self.tx_conversao = tx_conversao
        self.roi = roi
        self.vendas_dia = vendas_dia
        self.cpa = cpa
        self.rpa = rpa
        self.lucro_mensal = lucro_mensal

    def atualizar_dados_historicos(self):
        var_cpc = max(self.cpc * random.uniform(-0.03, 0.03), 0.01)  # Garante que o valor de CPC seja maior que 0.01
        var_impressoes_por_dia = self.impressoes_por_dia * random.uniform(-0.03, 0.03)
        var_ctr = max(self.ctr * random.uniform(-0.03, 0.03), 0.01)  # Garante que o valor de CTR seja maior que 0.01
        var_tx_conversao = self.tx_conversao * random.uniform(-0.03, 0.03)
        var_roi = max(self.roi * random.uniform(-0.03, 0.03), 0.1)  # Garante que o valor de ROI seja maior que 0.01
        var_vendas_dia = self.vendas_dia * random.uniform(-0.03, 0.03)
        var_cpa = self.cpa * random.uniform(-0.03, 0.03)
        var_rpa = self.rpa * random.uniform(-0.03, 0.03)
        var_lucro_mensal = self.lucro_mensal * random.uniform(-0.03, 0.03)

        self.cpc += var_cpc
        self.impressoes_por_dia += var_impressoes_por_dia
        self.ctr += var_ctr
        self.tx_conversao += var_tx_conversao
        self.roi += var_roi
        self.vendas_dia += var_vendas_dia
        self.cpa += var_cpa
        self.rpa += var_rpa
        self.lucro_mensal += var_lucro_mensal

def gerar_dados_mensais(campanhas, meses):
    dados_mensais = []
    for mes in range(1, meses + 1):
        dados_mensal = {}
        for campanha in campanhas:
            campanha.atualizar_dados_historicos()
            dados_mensal[campanha.nome] = {
                'cpc': round(campanha.cpc, 2),
                'impressoes_por_dia': round(campanha.impressoes_por_dia, 2),
                'ctr': round(campanha.ctr, 4),
                'tx_conversao': round(campanha.tx_conversao, 4),
                'roi': round(campanha.roi, 3),
                'vendas_dia': round(campanha.vendas_dia, 2),
                'cpa': round(campanha.cpa, 2),
                'rpa': round(campanha.rpa, 2),
                'lucro_mensal': round(campanha.lucro_mensal, 2)
            }
        dados_mensais.append(dados_mensal)
    return dados_mensais

# dados mensais para 12 meses
campanha_A = Campanha(campanhas[0], cpc[0], impressoes_por_dia[0], ctr[0], tx_conversao[0], roi[0], vendas_dia[0], cpa[0], rpa[0], lucro_mensal[0])
campanha_B = Campanha(campanhas[1], cpc[1], impressoes_por_dia[1], ctr[1], tx_conversao[1], roi[1], vendas_dia[1], cpa[1], rpa[1], lucro_mensal[1])
campanha_C = Campanha(campanhas[2], cpc[2], impressoes_por_dia[2], ctr[2], tx_conversao[2], roi[2], vendas_dia[2], cpa[2], rpa[2], lucro_mensal[2])
campanha_D = Campanha(campanhas[3], cpc[3], impressoes_por_dia[3], ctr[3], tx_conversao[3], roi[3], vendas_dia[3], cpa[3], rpa[3], lucro_mensal[3])

campanhas = [campanha_A, campanha_B, campanha_C, campanha_D] 

meses = 12

ano_2001 = gerar_dados_mensais(campanhas, meses)
ano_2002 = gerar_dados_mensais(campanhas, meses)
ano_2003 = gerar_dados_mensais(campanhas, meses)
ano_2004 = gerar_dados_mensais(campanhas, meses)
ano_2005 = gerar_dados_mensais(campanhas, meses)
ano_2006 = gerar_dados_mensais(campanhas, meses)
ano_2007 = gerar_dados_mensais(campanhas, meses)
ano_2008 = gerar_dados_mensais(campanhas, meses)
ano_2009 = gerar_dados_mensais(campanhas, meses)
ano_2010 = gerar_dados_mensais(campanhas, meses)
ano_2011 = gerar_dados_mensais(campanhas, meses)
ano_2012 = gerar_dados_mensais(campanhas, meses)
ano_2013 = gerar_dados_mensais(campanhas, meses)
ano_2014 = gerar_dados_mensais(campanhas, meses)
ano_2015 = gerar_dados_mensais(campanhas, meses)
ano_2016 = gerar_dados_mensais(campanhas, meses)
ano_2017 = gerar_dados_mensais(campanhas, meses)
ano_2018 = gerar_dados_mensais(campanhas, meses)
ano_2019 = gerar_dados_mensais(campanhas, meses)
ano_2020 = gerar_dados_mensais(campanhas, meses)
ano_2021 = gerar_dados_mensais(campanhas, meses)
ano_2022 = gerar_dados_mensais(campanhas, meses)
ano_2023 = gerar_dados_mensais(campanhas, meses)
ano_2023 = gerar_dados_mensais(campanhas, meses)
ano_2024 = gerar_dados_mensais(campanhas, meses)
ano_2025 = gerar_dados_mensais(campanhas, meses)
ano_2026 = gerar_dados_mensais(campanhas, meses)
ano_2027 = gerar_dados_mensais(campanhas, meses)
ano_2028 = gerar_dados_mensais(campanhas, meses)
ano_2029 = gerar_dados_mensais(campanhas, meses)
ano_2030 = gerar_dados_mensais(campanhas, meses)

def criar_meses(var_ano):
    '''
    Cria as variáveis mensais
    '''
    indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    mes_1 = var_ano[indices[0]]
    mes_2 = var_ano[indices[1]]
    mes_3 = var_ano[indices[2]]
    mes_4 = var_ano[indices[3]]
    mes_5 = var_ano[indices[4]]
    mes_6 = var_ano[indices[5]]
    mes_7 = var_ano[indices[6]]
    mes_8 = var_ano[indices[7]]
    mes_9 = var_ano[indices[8]]
    mes_10 = var_ano[indices[9]]
    mes_11 = var_ano[indices[10]]
    mes_12 = var_ano[indices[11]]
    return mes_1, mes_2, mes_3, mes_4, mes_5, mes_6, mes_7, mes_8, mes_9, mes_10, mes_11, mes_12

ano_2001_jan, ano_2001_fev, ano_2001_mar, ano_2001_abr, ano_2001_mai, ano_2001_jun, ano_2001_jul, ano_2001_ago, ano_2001_set, ano_2001_out, ano_2001_nov, ano_2001_dez = criar_meses(ano_2001)
ano_2002_jan, ano_2002_fev, ano_2002_mar, ano_2002_abr, ano_2002_mai, ano_2002_jun, ano_2002_jul, ano_2002_ago, ano_2002_set, ano_2002_out, ano_2002_nov, ano_2002_dez = criar_meses(ano_2002)
ano_2003_jan, ano_2003_fev, ano_2003_mar, ano_2003_abr, ano_2003_mai, ano_2003_jun, ano_2003_jul, ano_2003_ago, ano_2003_set, ano_2003_out, ano_2003_nov, ano_2003_dez = criar_meses(ano_2003)
ano_2004_jan, ano_2004_fev, ano_2004_mar, ano_2004_abr, ano_2004_mai, ano_2004_jun, ano_2004_jul, ano_2004_ago, ano_2004_set, ano_2004_out, ano_2004_nov, ano_2004_dez = criar_meses(ano_2004)
ano_2005_jan, ano_2005_fev, ano_2005_mar, ano_2005_abr, ano_2005_mai, ano_2005_jun, ano_2005_jul, ano_2005_ago, ano_2005_set, ano_2005_out, ano_2005_nov, ano_2005_dez = criar_meses(ano_2005)
ano_2006_jan, ano_2006_fev, ano_2006_mar, ano_2006_abr, ano_2006_mai, ano_2006_jun, ano_2006_jul, ano_2006_ago, ano_2006_set, ano_2006_out, ano_2006_nov, ano_2006_dez = criar_meses(ano_2006)
ano_2007_jan, ano_2007_fev, ano_2007_mar, ano_2007_abr, ano_2007_mai, ano_2007_jun, ano_2007_jul, ano_2007_ago, ano_2007_set, ano_2007_out, ano_2007_nov, ano_2007_dez = criar_meses(ano_2007)
ano_2008_jan, ano_2008_fev, ano_2008_mar, ano_2008_abr, ano_2008_mai, ano_2008_jun, ano_2008_jul, ano_2008_ago, ano_2008_set, ano_2008_out, ano_2008_nov, ano_2008_dez = criar_meses(ano_2008)
ano_2009_jan, ano_2009_fev, ano_2009_mar, ano_2009_abr, ano_2009_mai, ano_2009_jun, ano_2009_jul, ano_2009_ago, ano_2009_set, ano_2009_out, ano_2009_nov, ano_2009_dez = criar_meses(ano_2009)

ano_2010_jan, ano_2010_fev, ano_2010_mar, ano_2010_abr, ano_2010_mai, ano_2010_jun, ano_2010_jul, ano_2010_ago, ano_2010_set, ano_2010_out, ano_2010_nov, ano_2010_dez = criar_meses(ano_2010)
ano_2011_jan, ano_2011_fev, ano_2011_mar, ano_2011_abr, ano_2011_mai, ano_2011_jun, ano_2011_jul, ano_2011_ago, ano_2011_set, ano_2011_out, ano_2011_nov, ano_2011_dez = criar_meses(ano_2011)
ano_2012_jan, ano_2012_fev, ano_2012_mar, ano_2012_abr, ano_2012_mai, ano_2012_jun, ano_2012_jul, ano_2012_ago, ano_2012_set, ano_2012_out, ano_2012_nov, ano_2012_dez = criar_meses(ano_2012)
ano_2013_jan, ano_2013_fev, ano_2013_mar, ano_2013_abr, ano_2013_mai, ano_2013_jun, ano_2013_jul, ano_2013_ago, ano_2013_set, ano_2013_out, ano_2013_nov, ano_2013_dez = criar_meses(ano_2013)
ano_2014_jan, ano_2014_fev, ano_2014_mar, ano_2014_abr, ano_2014_mai, ano_2014_jun, ano_2014_jul, ano_2014_ago, ano_2014_set, ano_2014_out, ano_2014_nov, ano_2014_dez = criar_meses(ano_2014)
ano_2015_jan, ano_2015_fev, ano_2015_mar, ano_2015_abr, ano_2015_mai, ano_2015_jun, ano_2015_jul, ano_2015_ago, ano_2015_set, ano_2015_out, ano_2015_nov, ano_2015_dez = criar_meses(ano_2015)
ano_2016_jan, ano_2016_fev, ano_2016_mar, ano_2016_abr, ano_2016_mai, ano_2016_jun, ano_2016_jul, ano_2016_ago, ano_2016_set, ano_2016_out, ano_2016_nov, ano_2016_dez = criar_meses(ano_2016)
ano_2017_jan, ano_2017_fev, ano_2017_mar, ano_2017_abr, ano_2017_mai, ano_2017_jun, ano_2017_jul, ano_2017_ago, ano_2017_set, ano_2017_out, ano_2017_nov, ano_2017_dez = criar_meses(ano_2017)
ano_2018_jan, ano_2018_fev, ano_2018_mar, ano_2018_abr, ano_2018_mai, ano_2018_jun, ano_2018_jul, ano_2018_ago, ano_2018_set, ano_2018_out, ano_2018_nov, ano_2018_dez = criar_meses(ano_2018)
ano_2019_jan, ano_2019_fev, ano_2019_mar, ano_2019_abr, ano_2019_mai, ano_2019_jun, ano_2019_jul, ano_2019_ago, ano_2019_set, ano_2019_out, ano_2019_nov, ano_2019_dez = criar_meses(ano_2019)

ano_2020_jan, ano_2020_fev, ano_2020_mar, ano_2020_abr, ano_2020_mai, ano_2020_jun, ano_2020_jul, ano_2020_ago, ano_2020_set, ano_2020_out, ano_2020_nov, ano_2020_dez = criar_meses(ano_2020)
ano_2021_jan, ano_2021_fev, ano_2021_mar, ano_2021_abr, ano_2021_mai, ano_2021_jun, ano_2021_jul, ano_2021_ago, ano_2021_set, ano_2021_out, ano_2021_nov, ano_2021_dez = criar_meses(ano_2021)
ano_2022_jan, ano_2022_fev, ano_2022_mar, ano_2022_abr, ano_2022_mai, ano_2022_jun, ano_2022_jul, ano_2022_ago, ano_2022_set, ano_2022_out, ano_2022_nov, ano_2022_dez = criar_meses(ano_2022)
ano_2023_jan, ano_2023_fev, ano_2023_mar, ano_2023_abr, ano_2023_mai, ano_2023_jun, ano_2023_jul, ano_2023_ago, ano_2023_set, ano_2023_out, ano_2023_nov, ano_2023_dez = criar_meses(ano_2023)
ano_2024_jan, ano_2024_fev, ano_2024_mar, ano_2024_abr, ano_2024_mai, ano_2024_jun, ano_2024_jul, ano_2024_ago, ano_2024_set, ano_2024_out, ano_2024_nov, ano_2024_dez = criar_meses(ano_2024)
ano_2025_jan, ano_2025_fev, ano_2025_mar, ano_2025_abr, ano_2025_mai, ano_2025_jun, ano_2025_jul, ano_2025_ago, ano_2025_set, ano_2025_out, ano_2025_nov, ano_2025_dez = criar_meses(ano_2025)
ano_2026_jan, ano_2026_fev, ano_2026_mar, ano_2026_abr, ano_2026_mai, ano_2026_jun, ano_2026_jul, ano_2026_ago, ano_2026_set, ano_2026_out, ano_2026_nov, ano_2026_dez = criar_meses(ano_2026)
ano_2027_jan, ano_2027_fev, ano_2027_mar, ano_2027_abr, ano_2027_mai, ano_2027_jun, ano_2027_jul, ano_2027_ago, ano_2027_set, ano_2027_out, ano_2027_nov, ano_2027_dez = criar_meses(ano_2027)
ano_2028_jan, ano_2028_fev, ano_2028_mar, ano_2028_abr, ano_2028_mai, ano_2028_jun, ano_2028_jul, ano_2028_ago, ano_2028_set, ano_2028_out, ano_2028_nov, ano_2028_dez = criar_meses(ano_2028)
ano_2029_jan, ano_2029_fev, ano_2029_mar, ano_2029_abr, ano_2029_mai, ano_2029_jun, ano_2029_jul, ano_2029_ago, ano_2029_set, ano_2029_out, ano_2029_nov, ano_2029_dez = criar_meses(ano_2029)
ano_2030_jan, ano_2030_fev, ano_2030_mar, ano_2030_abr, ano_2030_mai, ano_2030_jun, ano_2030_jul, ano_2030_ago, ano_2030_set, ano_2030_out, ano_2030_nov, ano_2030_dez = criar_meses(ano_2030)

def cria_df_mes(var_mes, mes, ano):
    # Cria o DataFrame a partir do dicionário
    df = pd.DataFrame.from_dict(var_mes, orient='index')   

    # Adiciona a coluna 'mes' com os valores desejados
    df['mes'] = [f'{mes}', f'{mes}', f'{mes}', f'{mes}'] 
    df['ano'] = [f'{ano}', f'{ano}', f'{ano}', f'{ano}'] 

    # Cria a coluna 'campanha' equivalente aos índices do DataFrame
    df['campanha'] = df.index
    colunas = ['ano', 'mes', 'campanha', 'cpc', 'impressoes_por_dia', 'ctr', 'tx_conversao', 'roi', 'vendas_dia', 'cpa', 'rpa', 'lucro_mensal']
    df = df[colunas]

    return df

def cria_df_ano(ano):
    meses = {
        'Janeiro': globals()[f'ano_{ano}_jan'],
        'Fevereiro': globals()[f'ano_{ano}_fev'],
        'Março': globals()[f'ano_{ano}_mar'],
        'Abril': globals()[f'ano_{ano}_abr'],
        'Maio': globals()[f'ano_{ano}_mai'],
        'Junho': globals()[f'ano_{ano}_jun'],
        'Julho': globals()[f'ano_{ano}_jul'],
        'Agosto': globals()[f'ano_{ano}_ago'],
        'Setembro': globals()[f'ano_{ano}_set'],
        'Outubro': globals()[f'ano_{ano}_out'],
        'Novembro': globals()[f'ano_{ano}_nov'],
        'Dezembro': globals()[f'ano_{ano}_dez']
    }

    df = pd.DataFrame()
    for mes, df_mes in meses.items():
        df = pd.concat([df, cria_df_mes(df_mes, mes, ano)], ignore_index=True)

    return df

ano_1_df = cria_df_ano(2001)
ano_2_df = cria_df_ano(2002)
ano_3_df = cria_df_ano(2003)
ano_4_df = cria_df_ano(2004)
ano_5_df = cria_df_ano(2005)
ano_6_df = cria_df_ano(2006)
ano_7_df = cria_df_ano(2007)
ano_8_df = cria_df_ano(2008)
ano_9_df = cria_df_ano(2009)
ano_10_df = cria_df_ano(2010)
ano_11_df = cria_df_ano(2011)
ano_12_df = cria_df_ano(2012)
ano_13_df = cria_df_ano(2013)
ano_14_df = cria_df_ano(2014)
ano_15_df = cria_df_ano(2015)
ano_16_df = cria_df_ano(2016)
ano_17_df = cria_df_ano(2017)
ano_18_df = cria_df_ano(2018)
ano_19_df = cria_df_ano(2019)
ano_20_df = cria_df_ano(2020)
ano_21_df = cria_df_ano(2021)
ano_22_df = cria_df_ano(2022)
ano_23_df = cria_df_ano(2023)
ano_24_df = cria_df_ano(2024)
ano_25_df = cria_df_ano(2025)
ano_26_df = cria_df_ano(2026)
ano_27_df = cria_df_ano(2027)
ano_28_df = cria_df_ano(2028)
ano_29_df = cria_df_ano(2029)
ano_30_df = cria_df_ano(2030)

dataframes = [ano_1_df, ano_2_df, ano_3_df, ano_4_df, ano_5_df, ano_6_df, ano_7_df, ano_8_df, ano_9_df, ano_10_df, ano_11_df, ano_12_df, ano_13_df, ano_14_df, ano_15_df, ano_16_df, ano_17_df, ano_18_df, ano_19_df, ano_20_df, ano_21_df, ano_22_df, ano_23_df, ano_24_df, ano_25_df, ano_26_df, ano_27_df, ano_28_df, ano_29_df, ano_30_df]

df = pd.concat(dataframes, axis=0, ignore_index=True)

df.to_csv('meu_dataframe.csv', index=False)
