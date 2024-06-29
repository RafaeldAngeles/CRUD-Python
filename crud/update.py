import psycopg2
from config import DATABASE_NAME, DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_PORT

# Conectar ao banco de dados
conexao = psycopg2.connect(
    database=DATABASE_NAME,
    host=DATABASE_HOST,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    port=DATABASE_PORT
)

cunn = conexao.cursor()


nomeProduto = "mouse"
valor = 350

comando = f"UPDATE vendas SET valor = %s WHERE nome_produto = %s "
cunn.execute(comando, (valor, nomeProduto))
conexao.commit()

cunn.close()
conexao.close()




