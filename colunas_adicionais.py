# Adiciona colunas básicas numa tabela

!pip install unidecode
from unidecode import unidecode

!wget https://raw.githubusercontent.com/Miphour/nacional_colunas_limpeza/refs/heads/main/municipios_tratado.csv

import pandas as pd

municipios = pd.read_csv('/content/municipios_tratado.csv', encoding='latin1',sep=',')
municipios["COD_IBGE"] = municipios["COD_IBGE"].astype(str)


def tempo_ate_envio(planilha):
  planilha["Tempo_ate_envio"] = planilha["Data de Confirmação"] - planilha["Data de Vencimento"]
  planilha["Tempo_ate_envio"] = planilha["Tempo_ate_envio"].astype('timedelta64[s]').dt.days

  return planilha

def tempo_retorno(planilha):
  planilha["Tempo_retorno"] = planilha['Data de Retorno'] - planilha["Data de Confirmação"]
  planilha["Tempo_retorno"] = planilha["Tempo_retorno"].astype('timedelta64[s]').dt.days

  return planilha

def tempo_protocolo(planilha):
  planilha["Tempo_protocolo"] = planilha["Data do Protocolo"] - planilha["Data de Confirmação"]
  planilha["Tempo_protocolo"] = planilha["Tempo_protocolo"].astype('timedelta64[s]').dt.days
  
  return planilha

def nome_municipio(planilha):
  planilha = planilha.merge(municipios, left_on="Código IBGE da Pç Pagto", right_on='COD_IBGE',how='left')
  planilha = planilha.drop(columns=['COD_IBGE','UF'], axis=0)
  planilha["MUNICIPIO"] = planilha["MUNICIPIO"].str.upper()
  planilha["MUNICIPIO"] = planilha["MUNICIPIO"].apply(lambda x: unidecode(x).upper())
  return planilha


def adiciona_colunas(planilha):
  planilha = tempo_ate_envio(planilha)
  planilha = tempo_retorno(planilha)
  planilha = tempo_protocolo(planilha)
  planilha = nome_municipio(planilha)
  return planilha
