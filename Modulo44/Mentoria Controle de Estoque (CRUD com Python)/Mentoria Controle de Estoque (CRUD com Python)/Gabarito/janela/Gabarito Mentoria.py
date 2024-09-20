#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import *
import tkinter.messagebox
import pyodbc

# integração com o Banco de Dados
dados_conexao = ("Driver={SQL Server};"
                 "Server=SEU_SERVIDOR;"
                 "Database=EstoqueMentoria")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# Insumos

# procurar insumo
def btn_clicked0():
    # pegar a informação do campo nome_insumo (entry1)
    nome_insumo = entry1.get()
    # buscar essa informação do insumo no banco de dados
    # colocar no entry0 (caixa de texto) as informações do insumo no banco de dados
    print("Procurar Insumo")
    comando = f"""SELECT * from Insumos
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    # [(1, 'garrafa', '2050-12-31', 1, Decimal('9500.00'))]
    # entry0.delete("1.0", END)
    for linha in cursor.fetchall():
        texto = f"Item: {linha.nome_insumo}\n Quantidade: {linha.qtde}\n Lote:{linha.lote}\n Validade:{linha.data_validade}\n"
        entry0.insert("1.0", texto)

# deletar insumo
def btn_clicked1():
    # pegar a informação do campo nome_insumo (entry1)
    nome_insumo = entry1.get()
    # buscar e deletar a informação do insumo no banco de dados
    # exibir uma mensagem dizendo que deletou o insumo do banco de dados
    comando = f"""DELETE from Insumos
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    cursor.commit()
    print("Deletar insumo")
    tkinter.messagebox.showinfo(title="Aviso Uso Excluído",message=f"{nome_insumo} foi excluído do Banco de Dados")

# consumir insumo (registrar uso insumo)
def btn_clicked2():
    # pegar a informação do campo nome_insumo (entry1)
    # pegar a informação do campo qtde (entry4)
    nome_insumo = entry1.get()
    qtde_usada = entry4.get()
    # buscar o insumo pelo nome dele no banco de dados
    # diminuir da quantidade do insumo, a quantidade que eu consumi
    comando = f"""UPDATE Insumos
        SET qtde = qtde - {qtde_usada}
        WHERE nome_insumo = '{nome_insumo}';
        """
    cursor.execute(comando)
    cursor.commit()
    # exibir uma mensagem dizendo quantas unidades eu consumi do banco de dados
    print("Usar Insumo")
    tkinter.messagebox.showinfo(title="Aviso Uso Insumo",message=f"{qtde_usada} unidades do {nome_insumo} foram usadas")

# adicionar insumo
def btn_clicked3():
    # pegar todos os campos
    nome_insumo = entry1.get()
    data_validade = entry2.get()
    lote = entry3.get()
    qtde = entry4.get()
    
    # rodar um procurar no banco de dados pelo insumo
    # olhar o cursor.fetchall()
    # se o insumo tiver dentro do cursor.fetchall()
    # faço um update adicionando a quantidade
    # caso contrário
    # adicionar no banco de dados aquele insumo
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde)
    VALUES
        ('{nome_insumo}', '{data_validade}', '{lote}', '{qtde}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Adicionar Produto",message="Produto Adicionado com Sucesso")
    print("Adicionar Insumo")
#     entry1.delete()
#     entry2.delete()
#     entry3.delete()
#     entry4.delete()
    
    
# print(entry1.get()) -> nome_insumo
# print(entry2.get()) -> data_validade
# print(entry3.get()) -> lote
# print(entry4.get()) -> quantidade
# entry0.get("1.0", END) -> campo para exibir o produto do banco de dados

window = Tk()

window.geometry("711x646")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 646,
    width = 711,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    355.5, 323.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 479, y = 195,
    width = 178,
    height = 38)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 247, y = 197,
    width = 178,
    height = 36)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 479, y = 123,
    width = 178,
    height = 35)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 247, y = 125,
    width = 178,
    height = 34)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    455.0, 560.0,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 250, y = 502,
    width = 410,
    height = 114)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    517.0, 294.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 377, y = 278,
    width = 280,
    height = 31)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    517.0, 340.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 377, y = 324,
    width = 280,
    height = 31)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    517.0, 388.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 377, y = 372,
    width = 280,
    height = 31)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    517.0, 436.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 377, y = 420,
    width = 280,
    height = 31)

window.resizable(False, False)
window.mainloop()

