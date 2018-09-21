import levenshtein as ls 
import pandas as pd 
import time
import timeit
# https://pythonspot.com/pandas-filter/
# https://chrisalbon.com/python/data_wrangling/filter_dataframes/

# calculate runtime
start = timeit.default_timer()

# test database
xlsx = pd.ExcelFile('C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V19.xlsx')
df1    = pd.read_excel(xlsx, 'Banco digitação')
df_aux_juazeiro = pd.read_excel(xlsx, 'Aux_Juazeiro')

for line in df1.itertuples():
    if line.local == "Juazeiro":
        print("É Juazeiro")
        for line in df1.itertuples():
            if line.local == "Juazeiro":
                print("É Juazeiro")
                print("É Juazeiro")
                for line in df1.itertuples():
                    print("entrei no if")