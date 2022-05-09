import MySQLdb  # Módulo para conectar com o MySQL
from conSettings import host,usuario,senha,db,port

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor() # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

# Sintaxe do CREATE: CREATE TABLE/DATABASE IF NOT EXISTS TABLE_NAME(COLUMN_NAME DATA_TYPE,...);

def createTable(table,values):

    global c, con

    query = "CREATE TABLE IF NOT EXISTS " + table + " ("

    query = query + ", ".join([ v  for v in values]) + ");"

    print(query)

    c.execute(query) # Executa a query
    con.commit() # Garante que a execução aconteça

values = ["ID INT PRIMARY KEY ", "NOME CHAR(30)", "CPF CHAR(11)", "IDADE INT"]

createTable("ALUNOS",values)