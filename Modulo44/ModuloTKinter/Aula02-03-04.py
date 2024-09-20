import tkinter as tk

janela = tk.Tk()

janela.title("Cotação Moedas")
mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas",fg="#FFFFFF", bg='#000000', width=50, height= 5)

mensagem.pack()

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.pack()

moeda = tk.Entry()
moeda.pack()


janela.mainloop()