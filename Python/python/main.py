import tkinter as tk
import os

if not os.path.exists("bancos"):
    os.mkdir("bancos")

banco = ""

def atualizar():

    lista.delete(0, tk.END)

    for i in os.listdir("bancos"):
        lista.insert(tk.END, i)

def criar():

    nome = entrada_banco.get()

    if nome == "":
        return

    os.mkdir("bancos/" + nome)

    open("bancos/" + nome + "/dados.txt", "a").close()

    entrada_banco.delete(0, tk.END)

    atualizar()

def abrir():

    global banco

    banco = lista.get(lista.curselection())

    titulo["text"] = "Banco: " + banco

    mostrar()

def excluir_banco():

    nome = lista.get(lista.curselection())

    os.remove("bancos/" + nome + "/dados.txt")

    os.rmdir("bancos/" + nome)

    atualizar()

def renomear_banco():

    nome = lista.get(lista.curselection())

    novo = entrada_banco.get()

    os.rename("bancos/" + nome, "bancos/" + novo)

    entrada_banco.delete(0, tk.END)

    atualizar()

def mostrar():

    texto.delete("1.0", tk.END)

    try:

        arq = open("bancos/" + banco + "/dados.txt", "r")

        for linha in arq:
            texto.insert(tk.END, linha)

        arq.close()

    except:
        pass

def adicionar():

    if banco == "":
        return

    nome = entrada_nome.get()
    idade = entrada_idade.get()

    if nome == "" or idade == "":
        return

    id = 1

    arq = open("bancos/" + banco + "/dados.txt", "r")

    for linha in arq:
        id = int(linha.split(";")[0]) + 1

    arq.close()

    arq = open("bancos/" + banco + "/dados.txt", "a")

    arq.write(f"{id};{nome};{idade}\n")

    arq.close()

    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)

    mostrar()

def remover():

    id = entrada_id.get()

    linhas = []

    arq = open("bancos/" + banco + "/dados.txt", "r")

    for linha in arq:

        if not linha.startswith(id + ";"):
            linhas.append(linha)

    arq.close()

    arq = open("bancos/" + banco + "/dados.txt", "w")

    arq.writelines(linhas)

    arq.close()

    mostrar()

def buscar():

    id = entrada_id.get()

    texto.delete("1.0", tk.END)

    arq = open("bancos/" + banco + "/dados.txt", "r")

    for linha in arq:

        if linha.startswith(id + ";"):
            texto.insert(tk.END, linha)

    arq.close()

janela = tk.Tk()

janela.geometry("700x400")

frame1 = tk.Frame(janela)
frame1.pack(side="left")

frame2 = tk.Frame(janela)
frame2.pack(side="right")

tk.Label(frame1, text="Bancos").pack()

lista = tk.Listbox(frame1, width=20)
lista.pack()

entrada_banco = tk.Entry(frame1)
entrada_banco.pack()

tk.Button(frame1, text="Criar", command=criar).pack()

tk.Button(frame1, text="Abrir", command=abrir).pack()

tk.Button(frame1, text="Renomear", command=renomear_banco).pack()

tk.Button(frame1, text="Excluir", command=excluir_banco).pack()

titulo = tk.Label(frame2, text="Banco")
titulo.pack()

tk.Label(frame2, text="Nome").pack()
entrada_nome = tk.Entry(frame2)
entrada_nome.pack()

tk.Label(frame2, text="Idade").pack()
entrada_idade = tk.Entry(frame2)
entrada_idade.pack()

tk.Button(frame2, text="Adicionar", command=adicionar).pack()

tk.Label(frame2, text="ID").pack()
entrada_id = tk.Entry(frame2)
entrada_id.pack()

tk.Button(frame2, text="Buscar", command=buscar).pack()

tk.Button(frame2, text="Remover", command=remover).pack()

texto = tk.Text(frame2, width=50, height=20)
texto.pack()

atualizar()

janela.mainloop()