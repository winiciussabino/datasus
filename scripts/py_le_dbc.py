import pandas as pd
from rpy2.robjects.packages import importr

le = importr('read.dbc')
utils = importr('utils')

#dados = le.read_dbc("../dados_dbc/STMT2208.dbc")

#utils.write_table(dados,"../dados_csv/py_dados.csv",sep="|")

df = pd.read_csv('../dados_csv/py_dados.csv',sep='|',dtype=str)

print(df)