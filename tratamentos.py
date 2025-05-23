import pandas as pd

def trata_documento_devedor(planilha):
  if 'Documento do Devedor' in planilha.columns:
    planilha['Documento do Devedor'] = planilha['Documento do Devedor'].astype(str)
    planilha['Documento do Devedor'] = planilha['Documento do Devedor'].str.zfill(14)
  return planilha

def trata_documento_sacador(planilha):
  alvo = 'Documento do Sacador'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(14)
  return planilha

def trata_cod_portador(planilha):
  alvo = "Código do Portador"
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(3)
  return planilha
  
def trata_cod_cartorio(planilha):
  alvo = 'Código do Cartório'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(int)
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(2)
  return planilha

def trata_uf_cra(planilha):
  alvo = 'UF da CRA'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].zfill(2)
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha

def trata_uf_sacador(planilha):
  alvo = 'UF do Sacador'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].zfill(2)
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha

def trata_cod_ibge(planilha):
  alvo = 'Código IBGE da Pç Pagto'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].zfill(7)
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha


def tratamento_padrao(planilha):
  planilha = trata_documento_devedor(planilha)
  planilha = trata_documento_sacador(planilha)
  planilha = trata_cod_portador(planilha)
  planilha = trata_cod_cartorio(planilha)
  
  return planilha
