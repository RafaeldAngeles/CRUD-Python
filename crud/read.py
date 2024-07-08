import psycopg2
import json
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

def get_read(event):
    
    valor_produto = event["valor"]
    nome_produto = event["nome_produto"]
    
    conexao = psycopg2.connect(
        database=DATABASE_NAME,
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        port=DATABASE_PORT
    )

    cunn = conexao.cursor()

    comando = f'SELECT * FROM vendas'
    values = (nome_produto, valor_produto)
    cunn.execute(comando, values)
    resultado = cunn.fetchall()

    cunn.close()
    conexao.close()

    return json.dumps(resultado, default=str)