# Importando a biblitoeca pandas
import pandas as pd

# Salvando o arquivo em uma variavel
arquivo_csv = 'perfil_eleitorado_2020.csv'

# Separa o arquivo csv por colunas
arquivo_csv_df = pd.read_csv(arquivo_csv, sep=';', header=0, encoding='latin-1')

# Lista de cabeçalho para ser ultilizado na filtragem dos dados
lista_cabecalho = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO', 
'CD_MUN_SIT_BIOMETRIA', 'DS_MUN_SIT_BIOMETRIA', 'NR_ZONA', 'CD_GENERO', 'DS_GENERO', 
'CD_ESTADO_CIVIL', 'DS_ESTADO_CIVIL', 'CD_FAIXA_ETARIA', 'DS_FAIXA_ETARIA', 
'CD_GRAU_ESCOLARIDADE', 'DS_GRAU_ESCOLARIDADE', 'QT_ELEITORES_PERFIL', 
'QT_ELEITORES_BIOMETRIA', 'QT_ELEITORES_DEFICIENCIA', 'QT_ELEITORES_INC_NM_SOCIAL']

# Armazena apenas os valores de SP e apaga valores de "CD_FAIXA_ETARIA" que estão invalidos
arquivo_csv_df = arquivo_csv_df[(arquivo_csv_df[lista_cabecalho[13]] != -3) & 
(arquivo_csv_df[lista_cabecalho[3]] == 'SP')]

# Remove linhas em brancos
arquivo_csv_df = arquivo_csv_df.dropna()

# Salva a quantidade de linhas 
quantidade_linhas = arquivo_csv_df.shape[0]

# Cria o número inicial do ID, quer será ultilizado no laço de repetição
numero_id = 1;

# Cria o vetor que vai armazenar os IDs
lista_id=[]

# Laço de repetição que armazena os IDs
while quantidade_linhas >= numero_id:
    
    # Adiciona os id dentro do vetor
    lista_id.append(f'P.E{numero_id}')

    # Aumenta o número do ID de 1 em 1
    numero_id = numero_id+1

# Cria uma nova coluna  e a posiciona na posição 0
arquivo_csv_df.insert(0, 'ID', lista_id)

# Exporta um csv do arquivo tratado
arquivo_csv_df.to_csv('perfil_eleitorado_tratado.csv', index=False,encoding='latin-1')




















