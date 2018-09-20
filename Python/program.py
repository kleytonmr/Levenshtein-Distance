import levenshtein as ls 
import pandas as pd 
import time
import timeit
# https://pythonspot.com/pandas-filter/
# https://chrisalbon.com/python/data_wrangling/filter_dataframes/

# calculate runtime
start = timeit.default_timer()

# test database
xlsx = pd.ExcelFile('../bases/Compacto_monitoramento_V19.xlsx')
df_digitacao    = pd.read_excel(xlsx, 'Banco digitação')
df_aux_juazeiro = pd.read_excel(xlsx, 'Aux_Juazeiro')

def read_database(df1, df2):
    temp = 0
    for i, line_i in df1.iterrows():
        if line_i['local'] == "Juazeiro":
            if line_i['cod_inep'] != temp:
                temp = line_i['cod_inep']
                print(temp)
            for j, line_j in df2.iterrows():
                if line_i['cod_inep'] == line_j['EscolaID']:
                    cod1 = line_i['cod_inep']
                    cod2 = line_j['EscolaID']
                    itaration(cod1,cod2, df1, df2)
                    print("Passei aqui {0} {1}" . format(cod1, cod2))


def itaration(cod1, cod2, df1, df2):
    name1 = pd.DataFrame(df1[df1.cod_inep == cod1].nm_aluno)
    name2 = pd.DataFrame(df2[df2.EscolaID == cod2].Nome_Aluno)
    print("Cod1:{0} Cod2:{1}" . format(cod1,cod2))
    
    for i, line_i in name1.iterrows():
        for j, line_j in name2.iterrows():
            percent = ls.compare(line_i['nm_aluno'],line_j['Nome_Aluno'])
            print("Nome1:{0}. Cod. Escola1:{1}. Nome2:{2}. Cod. Escola2:{3} {4}% " . format(line_i['nm_aluno'], cod1, line_j['Nome_Aluno'], cod2, percent ))

            
read_database(df_digitacao, df_aux_juazeiro)            

end = timeit.default_timer()
print ('duration: %f' % (end - start))                  

    
