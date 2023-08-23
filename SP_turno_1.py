# Importando a biblitoeca pandas
import pandas as pd

# Salvando o arquivo em uma variavel
arquivo_csv = 'SP_turno_1.csv'

# Separa o arquivo csv por colunas
arquivo_csv_df = pd.read_csv(arquivo_csv, sep=';', header=0, encoding='latin-1')

# Lista de cabeçalho para ser ultilizado na filtragem dos dados
lista_cabecalho = ['DT_GERACAO', 'HH_GERACAO', 'ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'NM_TIPO_ELEICAO', 'CD_PLEITO',
'DT_PLEITO', 'NR_TURNO', 'CD_ELEICAO', 'DS_ELEICAO', 'SG_UF', 'CD_MUNICIPIO', 'NM_MUNICIPIO',
'NR_ZONA', 'NR_SECAO', 'NR_LOCAL_VOTACAO', 'CD_CARGO_PERGUNTA', 'DS_CARGO_PERGUNTA',
'NR_PARTIDO', 'SG_PARTIDO', 'NM_PARTIDO', 'DT_BU_RECEBIDO', 'QT_APTOS', 'QT_COMPARECIMENTO',
'QT_ABSTENCOES', 'CD_TIPO_URNA', 'DS_TIPO_URNA', 'CD_TIPO_VOTAVEL', 'DS_TIPO_VOTAVEL',
'NR_VOTAVEL', 'NM_VOTAVEL', 'QT_VOTOS', 'NR_URNA_EFETIVADA', 'CD_CARGA_1_URNA_EFETIVADA',
'CD_CARGA_2_URNA_EFETIVADA', 'CD_FLASHCARD_URNA_EFETIVADA', 'DT_CARGA_URNA_EFETIVADA',
'DS_CARGO_PERGUNTA_SECAO', 'DS_AGREGADAS', 'DT_ABERTURA', 'DT_ENCERRAMENTO',
'QT_ELEITORES_BIOMETRIA_NH', 'DT_EMISSAO_BU', 'NR_JUNTA_APURADORA', 'NR_TURMA_APURADORA']

# Remove votos Nulos, Brancos e votos "Legenda"
arquivo_csv_df = arquivo_csv_df[(arquivo_csv_df[lista_cabecalho[28]] == 'Nominal')]

# Remove linhas em brancos
arquivo_csv_df = arquivo_csv_df.dropna()

# Salva a quantidade de linhas 
quantidade_linhas = arquivo_csv_df.shape[0]

# Filtra por municipio e remove informações duplicadas
municipio_df = arquivo_csv_df[[lista_cabecalho[11], lista_cabecalho[12]]].drop_duplicates()

# Exporta o CSV já pronto para ser cadastrado em um Bacndo de dados ou Planilha.
municipio_df.to_csv('municipio.csv', index=False,encoding='latin-1')

tipo_voto_df = arquivo_csv_df[[lista_cabecalho[16],lista_cabecalho[17]]].drop_duplicates()

# Exporta o CSV já pronto para ser cadastrado em um Bacndo de dados ou Planilha.
tipo_voto_df.to_csv('tipo_voto.csv', index=False,encoding='latin-1')

# Filtra por partidos e remove informações duplicadas
partido_df = arquivo_csv_df[[lista_cabecalho[18], lista_cabecalho[19], lista_cabecalho[20]]].drop_duplicates()

# Exporta o CSV já pronto para ser cadastrado em um Bacndo de dados ou Planilha.
partido_df.to_csv('partido.csv', index=False,encoding='latin-1')

# Cria o número inicial do ID, quer será ultilizado no laço de repetição
numero_id = 1;

# Cria o vetor que vai armazenar os IDs
lista_id=[]

# Laço de repetição que armazena os IDs
while quantidade_linhas >= numero_id:
    
    # Adiciona os id dentro do vetor
    lista_id.append(f'I.D{numero_id}')

    # Aumenta o número do ID de 1 em 1
    numero_id = numero_id+1

# Filtra por candidato
candidato_df = arquivo_csv_df[[lista_cabecalho[29], lista_cabecalho[30], lista_cabecalho[31]]]

# Cria um id e coloca na coluna 0
candidato_df.insert(0,'ID_candidato',lista_id)

# Exporta o CSV já pronto para ser cadastrado em um Banco de dados ou Planilha.
candidato_df.to_csv('candidato.csv', index=False,encoding='latin-1')

# Monta uma base de dados com informações úteis para serem filtradas
dados_voto = arquivo_csv_df[[lista_cabecalho[11],lista_cabecalho[16],lista_cabecalho[18],lista_cabecalho[29],lista_cabecalho[30],lista_cabecalho[31]]]

# Cria uma nova coluna  e a posiciona na posição 0
dados_voto.insert(0, 'ID_voto', lista_id)

# Exporta o CSV já pronto para ser cadastrado em um Banco de dados ou Planilha.
dados_voto.to_csv('dados_voto.csv', index=False,encoding='latin-1')



