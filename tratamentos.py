import pandas as pd

def trata_documento_devedor(planilha):
  alvo = 'Documento do Devedor'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(14)
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
    planilha[alvo] = planilha[alvo].str.upper()
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
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(2)

  return planilha

def trata_uf_sacador(planilha):
  alvo = 'UF do Sacador'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(2)
  return planilha

def trata_cod_ibge(planilha):
  alvo = 'Código IBGE da Pç Pagto'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(7)
  return planilha

def trata_ocorrencia_cartorio(planilha): 
  alvo = 'Ocorrência em Cartório'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha 

def trata_especie_titulo(planilha):
  alvo = 'Espécie do Título'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(3)
  return planilha 

def trata_valor_saldo(planilha): 
  alvo = 'Valor do Saldo'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(float)
  return planilha

def trata_valor_titulo(planilha):
  alvo = 'Valor do Título'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(float)
  return planilha 

def trata_uf_devedor(planilha): 
  alvo = 'UF do Devedor'
  if alvo in planilha.columns:
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(2)
  return planilha

def trata_data_vencimento(planilha): 
  alvo = 'Data de Vencimento'
  try:
    if alvo in planilha.columns:
      planilha['provisorio'] = pd.to_datetime(planilha['Data de Vencimento'], format='%d/%m/%Y')
      planilha[alvo] = planilha['provisorio']
      planilha = planilha.drop(columns=['provisorio'])
  except:
    pass
  return planilha

def trata_data_protocolo(planilha): 
  alvo = 'Data do Protocolo'
  try:
    if alvo in planilha.columns:
      planilha['provisorio'] = pd.to_datetime(planilha[alvo], format='%d/%m/%Y')
      planilha[alvo] = planilha['provisorio']
      planilha = planilha.drop(columns=['provisorio'])
  except:
    pass
  return planilha

def trata_data_confirmacao(planilha): 
  alvo = 'Data de Confirmação'
  try:
    if alvo in planilha.columns:
      planilha['provisorio'] = pd.to_datetime(planilha[alvo], format='%d/%m/%Y')
      planilha[alvo] = planilha['provisorio']
      planilha = planilha.drop(columns=['provisorio'])
  except:
    pass
  return planilha

def trata_data_retorno(planilha): 
  alvo = 'Data de Retorno'
  try:
    if alvo in planilha.columns:
      planilha['provisorio'] = pd.to_datetime(planilha[alvo], format='%d/%m/%Y')
      planilha[alvo] = planilha['provisorio']
      planilha = planilha.drop(columns=['provisorio'])
  except:
    pass
  return planilha

def trata_tipo_doc_devedor(planilha): 
  alvo = 'Tipo do Documento do Devedor'
  try:
    if alvo in planilha.columns: 
      planilha[alvo] = planilha[alvo].astype(str)
      planilha['provisoria'] = planilha[alvo].apply(lambda x:'CPF' if x == '2' else 'CNPJ')
      planilha[alvo] = planilha['provisoria']
      planilha = planilha.drop(columns=['provisoria'])
  except:
    pass
  return planilha 

def trata_cod_irregularidade(planilha): 
  alvo = 'Código da Irregularidade'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].astype(str)
    planilha[alvo] = planilha[alvo].str.zfill(2) 
  return planilha 
 

def trata_comp_irregularidade(planilha):
  alvo = 'Complemento de Irregularidade'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].replace({' ': None, '0': None, '00': None, 'nan': None})
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha 
  
def trata_falimentar(planilha): 
  alvo = 'Falimentar'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(str)
  return planilha

def trata_valor_custas(planilha):
  alvo = 'Valor das Custas'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(float)
    planilha[alvo] = planilha[alvo].round(2)
  return planilha 
 

def trata_valor_distribuicao(planilha): 
  alvo = 'Valor de Distribuição'
  if alvo in planilha.columns: 
    planilha[alvo] = planilha[alvo].fillna(0)
    planilha[alvo] = planilha[alvo].astype(float)
    planilha[alvo] = planilha[alvo].round(2)
  return planilha 

def trata_data_remessa(planilha):
alvo = 'Data de Remessa'
  try:
    if alvo in planilha.columns:
      planilha['provisorio'] = pd.to_datetime(planilha[alvo], format='%d/%m/%Y')
      planilha[alvo] = planilha['provisorio']
      planilha = planilha.drop(columns=['provisorio'])
  except:
    pass
  return planilha

# unifica e cria uma função padrão

def tratamento_padrao(planilha):
  # Aplica todos os tratamentos
    planilha = trata_documento_devedor(planilha)
    planilha = trata_documento_sacador(planilha)
    planilha = trata_cod_portador(planilha)
    planilha = trata_cod_cartorio(planilha)
    planilha = trata_uf_cra(planilha)
    planilha = trata_uf_sacador(planilha)
    planilha = trata_cod_ibge(planilha)
    planilha = trata_ocorrencia_cartorio(planilha)
    planilha = trata_especie_titulo(planilha)
    planilha = trata_valor_saldo(planilha)
    planilha = trata_valor_titulo(planilha)
    planilha = trata_uf_devedor(planilha)
    planilha = trata_data_vencimento(planilha)
    planilha = trata_data_protocolo(planilha)
    planilha = trata_data_confirmacao(planilha)
    planilha = trata_data_retorno(planilha)
    planilha = trata_tipo_doc_devedor(planilha)
    planilha = trata_cod_irregularidade(planilha)
    planilha = trata_comp_irregularidade(planilha)
    planilha = trata_falimentar(planilha)
    planilha = trata_valor_custas(planilha)
    planilha = trata_valor_distribuicao(planilha)
    planilha = trata_data_remessa(planilha)
  

    # verifica se alguma coluna não foi tratada
    alvos = [
           'Documento do Devedor', 
           'Documento do Sacador', 
           'Código do Portador',        
           'Código do Cartório', 
           'UF da CRA', 
           'UF do Sacador',
           'Código IBGE da Pç Pagto',
           'Ocorrência em Cartório',
           'Espécie do Título',
           'Valor do Saldo',
           'Valor do Título',
           'UF do Devedor',
           'Data de Vencimento',
           'Data do Protocolo',
           'Data de Confirmação',
           'Data de Retorno',
           'Data de Remessa',
           'Tipo do Documento do Devedor',
           'Código da Irregularidade',
           'Complemento de Irregularidade',
           'Falimentar',
           'Valor das Custas',
           'Valor de Distribuição'
          ]

    nao_tratados = [coluna for coluna in planilha.columns if coluna not in alvos]
    if len(nao_tratados) > 0:
      print(f'Colunas não tratadas: "{", ".join(nao_tratados)}"')
    else:
      print('Nenhuma coluna não tratada')
    return planilha
