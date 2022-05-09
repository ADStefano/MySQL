import MySQLdb  # Módulo para conectar com o MySQL
from conSettings import host,usuario,senha,db,port

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor() # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

# Sintaxe do delete: DELETE FROM table WHERE where

def delete(table,where):

    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    c.execute(query)
    con.commit()

    print(f"Conteúdo deletado da tabela: {table}\n", query)

delete("ALUNOS","ID = 5")
