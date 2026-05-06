import sqlite3
import os
import time
import json
import hashlib

caminho_bancodados = 'produtos.db'
carrinhos_file = 'carrinhos.json'

# Criar o bando de dados
def inicializar_bancodados():
    if os.path.exists(caminho_bancodados):
        return
    with open("bancoDados.sql", 'r', encoding="utf-8") as arquivo:
        sql = arquivo.read()
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.executescript(sql)
    conexao.commit()
    conexao.close()
# inicializar_bancodados()

# Pegar todos produtos
def pegar_produtos(filtro=""):
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    if filtro:
        cursor.execute(
            "SELECT * FROM produtos WHERE nome LIKE ? ORDER BY nome",
            (f"%{filtro}%",)
        )
    else:
        cursor.execute("SELECT * FROM produtos ORDER BY nome")
    produtos = []
    for linha in cursor.fetchall():
        produtos.append(dict(linha))
    conexao.close()
    return produtos

def gerar_codigo():
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:12].upper()

def salvar_carrinho(itens):
    codigo = gerar_codigo()
    carrinhos = {}
    if os.path.exists(carrinhos_file):
        with open(carrinhos_file, 'r', encoding="utf-8") as arquivo:
            carrinhos = json.load(arquivo)
    total = 0
    for item in itens:
        total += item["qty"] * item["preco"]
    carrinhos[codigo] = {"itens": itens, "total": total}
    with open(carrinhos_file, 'w', encoding="utf-8") as arquivo:
        json.dump(carrinhos, arquivo)
    return codigo

def carregar_carrinho(codigo):
    if not os.path.exists(carrinhos_file):
        return None
    with open(carrinhos_file, "r", encoding="utf-8") as f:
        return json.load(f).get(codigo)
    
 
# produtos = pegar_produtos()

# for produto in produtos:
#     nome = produto["nome"]
#     preco = produto["preco"]
    
#     print(f"{nome} - R$ {preco:.2f}".replace('.', ','))

# Pegar só um produto