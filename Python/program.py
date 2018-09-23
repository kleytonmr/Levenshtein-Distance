import levenshtein as ls 
import pandas as pd 
import time
import timeit

# calculate runtime
start = timeit.default_timer()

# test database
xlsx = pd.ExcelFile('C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V19.xlsx')
df_digitacao    = pd.read_excel(xlsx, 'Banco digitação')
df_aux_feira = pd.read_excel(xlsx, 'Aux_Feira')

def read_database(df1, df2):
    temp = 0

    for i in df1.itertuples():
        if i.local == 'Feira de Santana':
            for j in df2.itertuples():
                if i.cod_inep == j.inep_escola:
                    if i.cod_inep != temp:
                        temp = i.cod_inep
                        cod1 = i.cod_inep
                        cod2 = j.inep_escola
                        itaration(cod1,cod2, df1, df2)
                        print("Passei aqui {0} {1}" . format(cod1, cod2))
                        break
                    else:
                        break        
                    
def itaration(cod1, cod2, df1, df2):
    global appended_data
    appended_data = pd.DataFrame()

    df_temp_a = pd.DataFrame(df1[df1.cod_inep == cod1])
    df_temp_b = pd.DataFrame(df2[df2.inep_escola == cod2])

    for i in df_temp_a.itertuples():
        for j in df_temp_b.itertuples():
            percent = ls.compare(i.nm_aluno, j.aluno)
            df = {'index_a':i.Index+2, 'cod_escola_a': cod1,'ano_a:':i.ano_curso, 'aluno_a':i.nm_aluno, 'index_b':j.Index+2, 'cod_escola_b': cod2,'ano_b:':j.serie, 'aluno_b':j.aluno, 'Semelhanca %': percent}
            appended_data = appended_data.append(df, ignore_index=True)
            print("index:{0}, Nome:{1}, index:{2}, nome:{3} {4}%" . format(i.Index+2, i.nm_aluno, j.Index+2, j.aluno, percent))

read_database(df_digitacao, df_aux_feira)  

writer = pd.ExcelWriter('C:/Users/admin/Documents/Levenshtein-Distance/bases/output.xlsx')
appended_data.to_excel(writer,'Sheet1')
writer.save()

end = timeit.default_timer()
print(appended_data.head(100))
print ('Duration: %f' % (end - start))                  


    