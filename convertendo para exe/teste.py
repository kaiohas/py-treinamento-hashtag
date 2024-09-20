# %% [markdown]
# # Transformando Códigos em Python para Executáveis
# 
# ### Objetivo:
# 
# Os arquivos do jupyter que temos até aqui no curso são scripts que podemos usar para rodar códigos e fazer diversas tarefas.
# 
# Mas, algumas vezes, não seremos nós que iremos rodar os códigos e também não necessariamente o computador que vai executar o código não necessariamente tem python instalado.
# 
# Por isso, podemos transformar esses códigos em arquivos .exe (executáveis que funcionam em qualquer computador).
# 
# ### Cuidados
# 
# Para códigos simples, basta fazermos a conversão de python para executável, mas em muitos códigos, temos que pensar se precisamos fazer alguma adaptação.
# 
# Ex: Se o nosso código abre algum arquivo do nosso computador, temos que tornar essa ação de abrir o arquivo algo que funcione em qualquer computador. 
# 
# Sempre precisamos olhar o código e pensar: ele funcionaria em qualquer computador? Tem alguma coisa aqui nele que impede de funcionar no computador de outro pessoa? Se necessário, fazemos as adaptações. Vamos aprender como.
# 
# ### Funcionamento:
# 
# - Passo 1 - Seu código deve estar funcionando sem erros no jupyter
# 
# - Passo 2 - Transformar o código jupyter em scripts python padrão (extensão .py). Seu código deve estar funcionando nesse formato também.
# 
# - Passo 3 - Usar uma biblioteca de conversão (pyinstaller ou auto-py-to-exe) para transformar o código em executável.
# 
# - Passo 4 - Testar e adaptar o que for necessário.

# %%
print('Lira')


