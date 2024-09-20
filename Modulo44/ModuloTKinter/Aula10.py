import tkinter as tk
from tabnanny import check

janela = tk.Tk()


var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber email promocionais?", variable=var_promocoes)
checkbox_promocoes.grid(row=0, column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceita os termos de regulamento?",variable=var_politicas)
checkbox_politicas.grid(row=1,column=0)

def enviar():
    if var_promocoes.get():
        print("Usuario quer receber")
    else:
        print("Usuário não quer receber")
    if var_politicas.get():
        print("Usuario concordou")
    else:
        print("Usuario não concordou")

botao_enviar = tk.Button(text="Enviar",command=enviar)
botao_enviar.grid(row=2,column=0)


janela.mainloop()