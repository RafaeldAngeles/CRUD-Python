import psycopg2
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

def get_create(event):
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


    comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
    values = (nome_produto, valor_produto)
    cunn.execute(comando, values)

    conexao.commit()

    cunn.close()
    conexao.close()
    

