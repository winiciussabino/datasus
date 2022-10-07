#install.packages("read.dbc")

library(read.dbc)

dados = read.dbc("dados_dbc/STMT2208.dbc")

print(head(dados))

write.table(dados,"dados_csv/r_dados.csv",sep="|")
