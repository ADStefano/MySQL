from dataclasses import field
import MySQLdb  # Módulo para conectar com o MySQL
from conParameters import host,usuario,senha,db,port

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor() # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

# Sintaxe do select: SELECT fields FROM table WHERE where

def select(fields, tables, where = None): # Função para fazer um select

    global c # Indica que essa variável é a mesma de fora da função

    query = "SELECT "+ fields + " FROM " + tables # Query do select

    if(where): # Caso haja um WHERE o if adiciona ele à query
        query = query + " WHERE " + where
    
    c.execute(query) # Executa a query

    return c.fetchall() # Retorna todos os resultados do execute() 

read = select("NOME","ALUNOS","ID = 2")

print(read)
