import MySQLdb  # Módulo para conectar com o MySQL
from conSettings import host,usuario,senha,db,port

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor() # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

# Sintaxe do update: UPDATE table SET sets WHERE where

def update(sets, table, where = None):

    global c, con

    query = "UPDATE " + table + " SET " + ",".join([field + " = '" +value + "'" for field, value in sets.items()]) # Atenção para as aspas simples do = 'value'
    
    if(where):
        query = query + " WHERE " + where

    #c.execute(query)
    #con.commit()
    print("Consulta concluida: ",query)

update({"NOME":"Arlette Vizinha"}, "ALUNOS", "ID = 5") # Exemplo = update({"Coluna":"Conteúdo"}, "Tabela", "Where")
