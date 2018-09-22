import pandas as pd

xlsx = pd.ExcelFile('C:/Users/admin/Documents/Levenshtein-Distance/bases/teste.xlsx')
df_digitacao  = pd.read_excel(xlsx, 'Sheet1')

def teste(t):
    global appended_data
    appended_data = pd.DataFrame()
    for x in t.itertuples():
        df = {'index_a':x.nm_produtor}
        appended_data = appended_data.append(df, ignore_index=True)
    
teste(df_digitacao)

writer = pd.ExcelWriter('output.xlsx')
appended_data.to_excel(writer,'Sheet1')
writer.save()