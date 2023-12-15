import pyodbc

server = '192.168.176.19'
database = 'UIS2'
user = 'DesenvolvimentoLar'
password = 'LarDB842'

connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}'
conexao = pyodbc.connect(connection_string)
cursor = conexao.cursor()
consulta = """
    SELECT
    TOP 1500 TimeStamp,
    BAT210001,
    BAT400001,
    FT581,
    FT200,
    FT200001
    FROM UIS2.dbo.TotalizeData
    ORDER BY [TimeStamp] DESC
"""
cursor.execute(consulta)
registros = cursor.fetchall()
conexao.close()

time_stamp = []
balanca_de_fluxo = []
balanca_do_farelo = []
producao_de_oleo = []
consumo_de_vapor_extracao = []
consumo_de_vapor_preparacao = []

for registro in registros:    
    time_stamp.append(registro[0])
    balanca_de_fluxo.append(registro[1])
    balanca_do_farelo.append(registro[2])
    producao_de_oleo.append(registro[3])
    consumo_de_vapor_extracao.append(registro[4])
    consumo_de_vapor_preparacao.append(registro[5])
