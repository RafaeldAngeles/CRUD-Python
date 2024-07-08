import psycopg2
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

def get_update(event):
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

    comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"
    values = (valor_produto, nome_produto)
    cunn.execute(comando, values)
    conexao.commit()

    cunn.close()
    conexao.close()



