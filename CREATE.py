import MySQLdb  # Módulo para conectar com o MySQL
from conParameters import host,usuario,senha,db,port

con = MySQLdb.connect(host,usuario,senha,db,port) # Faz a conexão
c = con.cursor() # O cursor é necessário para realizar a query / Com o parâmetro MySQLdb.cursors.DictCursor ele retorna um dicionário em vez de uma tupla

# Sintaxe do insert: INSERT INTO TABLE(FIELDS) VALUES(VALUES)

def insert(values,table,fields = None):

    global c, con

    query = "INSERT INTO "+ table

    if(fields): 
        query = query + " (" + fields + ") "
    
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])

    print(query)

    c.execute(query) # Executa a query
    con.commit() # Garante que a execução aconteça

values = [" DEFAULT, 'Michael Jackson', '1958-08-29', '11987654321' ", 
          "DEFAULT, 'Arlete Vizinha', '1800-02-11', '25836914731' "]



insert(values,"ALUNOS")