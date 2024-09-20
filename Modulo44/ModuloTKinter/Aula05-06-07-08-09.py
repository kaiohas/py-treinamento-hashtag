import tkinter as tk
from tkinter import  ttk
janela = tk.Tk()

janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1], weight=1)

janela.title("Cotação Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas",fg="#FFFFFF", bg='#000000', width=35, height= 5)
mensagem.grid(row=0, column=0, columnspan=2,sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

# moeda = tk.Entry()
# moeda.grid(row=1, column=1)

dic_cotacoes = {
    'Dolar':5.5,
    'Euro':6.68,
    'Peso':0.80
}

moedas = list(dic_cotacoes.keys())

moeda = ttk.Combobox(janela,values=moedas)
moeda.grid(row=1, column=1)

def buscar_cotacao():
    moeda_digitada = moeda.get()
    cotacao_moeda = dic_cotacoes.get(moeda_digitada)
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3,column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"Cotação do {moeda_digitada} e de {cotacao_moeda} reais"


botao = tk.Button(text="Buscar cotação",command=buscar_cotacao)
botao.grid(row=2, column=1)

mensagem3  = tk.Label(text="Caso queira pegar mais de uma cotação ao mesmo tempo, digite uma moeda em cada linha")
mensagem3.grid(row=4,column=0,columnspan=2)

caixa_texto = tk.Text(width=10, height=5)
caixa_texto.grid(row=5,column=0,sticky="nswe")

def buscar_cotacoes():
    texto = caixa_texto.get("1.0",tk.END)
    lista_moedas = texto.split("\n")
    mensagem_cotacao = []
    for moeda in lista_moedas:
        cotacao = dic_cotacoes.get(moeda)
        if cotacao:
            mensagem_cotacao.append(f'{moeda}: {cotacao}')
    mensagem4 = tk.Label(text="\n".join(mensagem_cotacao))
    mensagem4.grid(row=6,column=1)



botao_multi = tk.Button(text="Buscar cotação",command=buscar_cotacoes)
botao_multi.grid(row=5,column=1,)

janela.mainloop()