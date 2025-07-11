import tkinter as tk
from tkinter import messagebox, simpledialog

hamburguerias = []


COR_FUNDO = "#fff4e6"
COR_TITULO = "#d62828"
COR_BOTAO = "#f77f00"
COR_BOTAO_TEXTO = "#ffffff"
FONTE_TITULO = ("Helvetica", 18, "bold")
FONTE_PADRAO = ("Helvetica", 12)


def janela_animate(win):
    alpha = 0.0
    increment = 0.05

    def fade_in():
        nonlocal alpha
        alpha += increment
        if alpha > 1.0:
            alpha = 1.0
            win.attributes("-alpha", alpha)
        else:
            win.attributes("-alpha", alpha)
            win.after(20, fade_in)

    win.attributes("-alpha", 0.0)
    fade_in()


def add_placeholder(entry, placeholder):
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry.insert(0, placeholder)
    entry.config(fg="gray")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def criar_botao_animado(parent, texto, comando):
    btn = tk.Button(
        parent,
        text=texto,
        font=FONTE_PADRAO,
        width=25,
        height=2,
        bg=COR_BOTAO,
        fg=COR_BOTAO_TEXTO,
        bd=0,
        relief="ridge",
        activebackground="#d96e00",
        command=comando,
    )

    def on_enter(e):
        btn.config(bg="#d96e00")

    def on_leave(e):
        btn.config(bg=COR_BOTAO)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn


def adicionar_hamburgueria():
    win = tk.Toplevel(root)
    win.title("🍔 Adicionar Hamburgueria")
    win.geometry("350x400")
    win.configure(bg=COR_FUNDO)
    janela_animate(win)

    tk.Label(win, text="Adicionar Hamburgueria", font=FONTE_TITULO, fg=COR_TITULO, bg=COR_FUNDO).pack(pady=10)

    frame_form = tk.Frame(win, bg=COR_FUNDO)
    frame_form.pack(pady=5)

    lbl_nome = tk.Label(frame_form, text="Nome:", font=FONTE_PADRAO, bg=COR_FUNDO)
    lbl_nome.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_nome = tk.Entry(frame_form, width=30)
    entry_nome.grid(row=0, column=1, pady=5)
    add_placeholder(entry_nome, "Digite o nome da hamburgueria")

    lbl_lat = tk.Label(frame_form, text="Latitude:", font=FONTE_PADRAO, bg=COR_FUNDO)
    lbl_lat.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_lat = tk.Entry(frame_form, width=30)
    entry_lat.grid(row=1, column=1, pady=5)
    add_placeholder(entry_lat, "Ex: -23.5505")

    lbl_long = tk.Label(frame_form, text="Longitude:", font=FONTE_PADRAO, bg=COR_FUNDO)
    lbl_long.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_long = tk.Entry(frame_form, width=30)
    entry_long.grid(row=2, column=1, pady=5)
    add_placeholder(entry_long, "Ex: -46.6333")

    promo_frame = tk.Frame(win, bg=COR_FUNDO)
    promo_frame.pack(pady=10, fill="x")

    tk.Label(promo_frame, text="Adicionar Promoções", font=("Helvetica", 14, "bold"), bg=COR_FUNDO).pack()

    produtos = []

    def adicionar_produto():
        nome_prod = entry_produto.get()
        preco_prod = entry_preco.get()
        desconto_prod = entry_desconto.get()

        if nome_prod in ("", "Nome do Produto") or preco_prod in ("", "Preço (ex: 25.90)"):
            messagebox.showwarning("Aviso", "Preencha nome e preço do produto.")
            return
        desconto_prod = desconto_prod if desconto_prod != "Desconto (%)" else "0"
        desconto_prod += "%"

        produtos.append({"nome": nome_prod, "preco": f"R$ {preco_prod}", "desconto": desconto_prod})

        entry_produto.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_desconto.delete(0, tk.END)
        add_placeholder(entry_produto, "Nome do Produto")
        add_placeholder(entry_preco, "Preço (ex: 25.90)")
        add_placeholder(entry_desconto, "Desconto (%)")

    frame_promo_inputs = tk.Frame(promo_frame, bg=COR_FUNDO)
    frame_promo_inputs.pack(pady=5)

    entry_produto = tk.Entry(frame_promo_inputs, width=18)
    entry_produto.grid(row=0, column=0, padx=3)
    add_placeholder(entry_produto, "Nome do Produto")

    entry_preco = tk.Entry(frame_promo_inputs, width=10)
    entry_preco.grid(row=0, column=1, padx=3)
    add_placeholder(entry_preco, "Preço (ex: 25.90)")

    entry_desconto = tk.Entry(frame_promo_inputs, width=10)
    entry_desconto.grid(row=0, column=2, padx=3)
    add_placeholder(entry_desconto, "Desconto (%)")

    btn_add_produto = criar_botao_animado(promo_frame, "➕ Adicionar Produto", adicionar_produto)
    btn_add_produto.pack(pady=5)

    def salvar_hamburgueria():
        nome = entry_nome.get()
        lat = entry_lat.get()
        long = entry_long.get()

        if nome.strip() == "" or nome == "Digite o nome da hamburgueria":
            messagebox.showwarning("Aviso", "Preencha o nome da hamburgueria.")
            return
        if lat.strip() == "" or lat == "Ex: -23.5505":
            messagebox.showwarning("Aviso", "Preencha a latitude.")
            return
        if long.strip() == "" or long == "Ex: -46.6333":
            messagebox.showwarning("Aviso", "Preencha a longitude.")
            return

        hamburgueria = {
            "nome": nome,
            "localizacao": {"latitude": lat, "longitude": long},
            "promocoes": produtos,
            "combos": [],
        }
        hamburguerias.append(hamburgueria)
        messagebox.showinfo("✅ Sucesso", f"Hamburgueria '{nome}' adicionada.")
        win.destroy()

    btn_salvar = criar_botao_animado(win, "💾 Salvar Hamburgueria", salvar_hamburgueria)
    btn_salvar.pack(pady=15)


def listar_hamburguerias():
    if not hamburguerias:
        messagebox.showinfo("Aviso", "Nenhuma hamburgueria cadastrada.")
        return

    win = tk.Toplevel(root)
    win.title("📋 Lista de Hamburguerias")
    win.geometry("400x400")
    win.configure(bg=COR_FUNDO)
    janela_animate(win)

    text = tk.Text(win, wrap="word", bg="#fff9f0", fg="#3d1c1c", font=FONTE_PADRAO)
    text.pack(padx=10, pady=10, fill="both", expand=True)

    info = ""
    for hb in hamburguerias:
        info += f"🍔 Hamburgueria: {hb['nome']}\n"
        info += f"📍 Localização: {hb['localizacao']['latitude']}, {hb['localizacao']['longitude']}\n"
        info += "🔥 Promoções:\n"
        for p in hb["promocoes"]:
            info += f" - {p['nome']}: {p['preco']} (Desconto: {p['desconto']})\n"
        info += "\n"

    text.insert("1.0", info)
    text.config(state="disabled")


def buscar_hamburgueria():
    win = tk.Toplevel(root)
    win.title("🔍 Buscar Hamburgueria")
    win.geometry("300x180")
    win.configure(bg=COR_FUNDO)
    janela_animate(win)

    tk.Label(win, text="🔍 Digite o nome da Hamburgueria:", font=FONTE_PADRAO, bg=COR_FUNDO).pack(pady=10)

    entry = tk.Entry(win, font=FONTE_PADRAO, width=30)
    entry.pack(pady=5)
    entry.focus()

    def procurar():
        nome = entry.get()
        if not nome:
            messagebox.showwarning("Aviso", "Digite um nome para buscar.")
            return

        for hb in hamburguerias:
            if hb["nome"].lower() == nome.lower():
                resultado = tk.Toplevel(root)
                resultado.title(f"🍔 {hb['nome']}")
                resultado.geometry("400x350")
                resultado.configure(bg=COR_FUNDO)
                janela_animate(resultado)

                text = tk.Text(resultado, wrap="word", bg="#fff9f0", fg="#3d1c1c", font=FONTE_PADRAO)
                text.pack(padx=10, pady=10, fill="both", expand=True)

                info = f"🍔 Hamburgueria: {hb['nome']}\n"
                info += f"📍 Localização: {hb['localizacao']['latitude']}, {hb['localizacao']['longitude']}\n"
                info += "🔥 Promoções:\n"
                for p in hb["promocoes"]:
                    info += f" - {p['nome']}: {p['preco']} (Desconto: {p['desconto']})\n"
                text.insert("1.0", info)
                text.config(state="disabled")
                return

        messagebox.showwarning("Não encontrada", "Hamburgueria não encontrada.")

    btn_procurar = criar_botao_animado(win, "🔎 Procurar", procurar)
    btn_procurar.pack(pady=10)
root = tk.Tk()
root.title("🍔 Cadastro de Hamburguerias")
root.geometry("300x340")
root.configure(bg=COR_FUNDO)

tk.Label(root, text="🍔 Hamburguerias", font=FONTE_TITULO, fg=COR_TITULO, bg=COR_FUNDO).pack(pady=20)

btn_add = criar_botao_animado(root, "➕ Adicionar Hamburgueria", adicionar_hamburgueria)
btn_add.pack(pady=10)

btn_list = criar_botao_animado(root, "📋 Listar Hamburguerias", listar_hamburguerias)
btn_list.pack(pady=10)

btn_search = criar_botao_animado(root, "🔍 Procurar Hamburgueria", buscar_hamburgueria)
btn_search.pack(pady=10)

btn_sair = criar_botao_animado(root, "🚪 Sair", root.destroy)
btn_sair.pack(pady=10)

root.mainloop()
