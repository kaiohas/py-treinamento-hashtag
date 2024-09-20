import tkinter as tk
from email.policy import default

def enviar():
    print(var_aviao.get())

janela = tk.Tk()

var_aviao = tk.StringVar(value=" ")

botao_clEconomica = tk.Radiobutton(text="Classe Economica",variable=var_aviao,value="Classe Economica",command=enviar)
botao_clExecutiva = tk.Radiobutton(text="Classe Executiva",variable=var_aviao,value="Classe Executiva",command=enviar)
botao_Primeiraclasse = tk.Radiobutton(text="Primeira Classe",variable=var_aviao,value="Primeira Classe",command=enviar)

def enviar():
    print(var_aviao.get())

# botao_enviar = tk.Button(text="Enviar",command=enviar)
# botao_enviar.grid(row=1,column=0)


botao_clEconomica.grid(row=0,column=0)
botao_clExecutiva.grid(row=0,column=1)
botao_Primeiraclasse.grid(row=0,column=2)
janela.mainloop()