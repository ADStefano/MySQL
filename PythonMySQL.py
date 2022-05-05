from dataclasses import field
import MySQLdb  # Módulo para conectar com o MySQL

host = "localhost"
usuario = "root"
senha = "root"
db = "ConexaoPython"
port = 3306

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor(MySQLdb.cursors.DictCursor) # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

def select(fields, tables, where = None): # Função para fazer um select

    global c # Indica que essa variável é a mesma de fora da função

    query = "SELECT "+ fields + " FROM " + tables # Query do select

    if(where): # Caso haja um WHERE o if adiciona ele à query
        query = query + " WHERE" + where
    
    c.execute(query) # Executa a query

    return c.fetchall() # Retorna todos os resultados do execute() 

read = select("NOME, CPF","ALUNOS")

print(read[0]["NOME"])