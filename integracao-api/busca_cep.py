# %% [markdown]
# ### Via CEP
# 
# https://viacep.com.br/

# %% [markdown]
# #### Consulta de informações de um CEP

# %% [markdown]
# #### Busca de CEP a partir de endereço

# %%
import requests
import os

uf = "MG"
cidade = "Uberlândia"
endereco = "Oscar"

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
requisicao = requisicao.json()


# %%
import pandas as pd
caminho = os.getcwd()
tabela = pd.DataFrame(requisicao)
tabela.to_csv(caminho +"\ceps.csv")

# %%



