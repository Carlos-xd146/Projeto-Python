import sqlite3
import os

caminho_bancodados = 'produtos.db'

# Criar o bando de dados
def inicializar_bancodados():
    if os.path.exists(caminho_bancodados):
        return
    with open("bancoDados.sql", 'r') as arquivo:
        sql = arquivo.read()
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.executescript(sql)
    conexao.commit()
    conexao.close()
inicializar_bancodados()

# Pegar todos produtos
def pegar_produtos():
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = []
    for linha in cursor.fetchall():
        produtos.append(dict(linha))
    conexao.close()
    return produtos

# produtos = pegar_produtos()

# for produto in produtos:
#     nome = produto["nome"]
#     preco = produto["preco"]
    
#     print(f"{nome} - R$ {preco:.2f}".replace('.', ','))

# Pegar só um produto