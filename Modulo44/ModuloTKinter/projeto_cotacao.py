import tkinter as tk
from tkinter import  ttk
from tkcalendar import DateEntry
import requests
import pandas as pd
from tkinter.filedialog import  askopenfilename
from datetime import datetime
import numpy as np

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
dic_moedas = requisicao.json()
lista_moedas = list(dic_moedas.keys())



def pegarcotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link =f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao = requests.get(link)
    dic_moedas = requisicao.json()
    valor_moeda = dic_moedas[0]['bid']
    label_textocotacao['text'] = f"A moeda {moeda} no dia {data_cotacao} teve uma cotação de: R${valor_moeda}"

def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="selecione o arquivo de moeda")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f'Arquivo selecionado: {caminho_arquivo}'


def atualizar_cotacoes():
    try:
        arquivo = pd.read_excel(var_caminhoarquivo.get())
        moedas = arquivo.iloc[:,0]
        data_in = calendario_datain.get()
        data_fim = calendario_datafim.get()
        ano_in = data_in[-4:]
        mes_in = data_in[3:5]
        dia_in = data_in[:2]
        ano_fim = data_fim[-4:]
        mes_fim = data_fim[3:5]
        dia_fim = data_fim[:2]
        for moeda in moedas:
            link2 = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/31?start_date={ano_in}{mes_in}{dia_in}&end_date={ano_fim}{mes_fim}{dia_fim}'
            requisicao = requests.get(link2)
            dic_cotacoes = requisicao.json()
            for cotacao in dic_cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in arquivo:
                    arquivo[data] = np.nan

                #dataframe.loc[linha,coluna]
                arquivo.loc[arquivo.iloc[:,0] == moeda, data] = bid
        arquivo.to_excel("teste.xlsx")
        label_atualizarcotacoes['text']="Arquivo atualizado com sucesso"
    except:
        label_atualizarcotacoes['text'] = "Selecione um arquivo Excel valido"





janela = tk.Tk()

janela.title("Ferramenta de cotação")

label_cotacaomoeda = tk.Label(text="Cotação de 1 moeda específica",borderwidth=2, relief='solid')
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecaomoeda = tk.Label(text="Selecione a moeda: ")
label_selecaomoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky="nswe")

label_selecaodata = tk.Label(text="Selecione a data: ")
label_selecaodata.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

calendario_moeda = DateEntry(year=2024,locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

texto = pegarcotacao
label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

bota_pegarcotacao = tk.Button(text="Pegar cotação",command=pegarcotacao)
bota_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")

#Cotação varias moedas

label_cotacaovariasmoedas = tk.Label(text="Cotação de multiplas moedas",borderwidth=2, relief='solid')
label_cotacaovariasmoedas.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecioararquivo = tk.Label(text="selecione um arquivo em Excel com as moedas na coluna A")
label_selecioararquivo.grid(row=5, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

bota_selecionararquivo = tk.Button(text="Clique para selecionar um arquivo",command=selecionar_arquivo)
bota_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky="nswe")

var_caminhoarquivo = tk.StringVar()


label_arquivoselecionado = tk.Label(text="Nenhum arquivo selecionado",anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_datainicial = tk.Label(text="Data inicial",anchor='e')
label_datafinal = tk.Label(text="Data Final",anchor='e')
label_datainicial.grid(row=7, column=0, padx=10, pady=10, sticky="nswe")
label_datafinal.grid(row=8, column=0, padx=10, pady=10, sticky="nswe")

calendario_datain = DateEntry(year=2024,locale='pt_br')
calendario_datafim = DateEntry(year=2024,locale='pt_br')
calendario_datain.grid(row=7, column=2, padx=10, pady=10, sticky="nswe")
calendario_datafim.grid(row=8, column=2, padx=10, pady=10, sticky="nswe")

bota_atualizarcotacoes = tk.Button(text="Clique para atualizar cotações",command=atualizar_cotacoes)
bota_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky="nswe")

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, padx=10, pady=10, sticky="nswe", columnspan=2)

bota_fechar = tk.Button(text="Fechar",command=janela.quit)
bota_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nswe")



janela.mainloop()