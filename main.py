import customtkinter as ctk

from bancoDadosControle import inicializar_bancodados, pegar_produtos

carrinho = {}
root = None
btn_carrinho = None

def atualizar_botao_carrinho ():
    if btn_carrinho:
        btn_carrinho.configure(text=f"🛒 Carrinho ({(carrinho)})")
    
def adcionar(p):
    if p["id"] in carrinho:
        carrinho[p["id"]]["qtd"] += 1
    else:
        carrinho[p["id"]] = {"produto": p, "qtd": 1}
    atualizar_botao_carrinho()

def tela_produtos():
    frame = ctk.CTkFrame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    header = ctk.CTkFrame(frame)
    header.pack(fill="x", pady=10)

    ctk.CTkLabel(
        header,
        text="📦 Share Products", 
        font=("Arial", 24, "bold"),
    ).pack(side="left")

    global btn_carrinha
    btn_carrinho = ctk.CTkButton(
        header,
        text=f"🛒 Carrinho ({len(carrinho)})",
    )
    btn_carrinho.pack(side="right", padx=5)

    lista = ctk.CTkScrollableFrame(frame)
    lista.pack(fill="both", expand=True)

    for produto in pegar_produtos():
        card = ctk.CTkFrame(lista, corner_radius=10)
        card.pack(fill="x", padx=5, pady=5)

    ctk.CTkLabel(
        card,
        text=f"{produto['nome']} - R$ {produto['preco']:.2f}",
        font=("Arial", 12),
    ).pack(side="left", padx=10, pady=8)

    ctk.CTkButton(
        card,
        text="🛒 Adcionar",
        width=100,
        commando=lambda p=produto: adcionar(p),
    ).pack(side="right", padx=5, pady=5)

def main():
    global root
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    root.title("Share Products")
    root.geometry("800x600")
    inicializar_bancodados()
    tela_produtos()
    root.mainloop()

if __name__ == "__name__":
    main()

        