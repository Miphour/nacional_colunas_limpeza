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

def tratamento_padrao(planilha):
  planilha = trata_documento_devedor(planilha)
  planilha = trata_documento_sacador(planilha)
  
  return planilha
