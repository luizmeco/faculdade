import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database='teste_db'
)

db = conn.cursor()

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

query = f"SELECT * FROM `login` WHERE usuario = '{usuario}' and senha = '{senha}'"

db.execute(query)
resultado = db.fetchall()

if (resultado):
    print('acesso liberado')
else:
    print('acesso negado')