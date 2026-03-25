CREATE TABLE 
    IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL
    );

INSERT INTO produtos (nome,preco)
VALUES
    ('Preto São Gabriel', 300.00),
    ('Verde Ubatuba', 250.00),
    ('Cinza Andorinha', 270.00),
    ('Marrom Café Imperial', 320.00),
    ('Branco Itaúnas', 290.00);

