import levenshtein as ls 
import pandas as pd 
import time
import timeit

# calculate runtime
start = timeit.default_timer()

# test database
xlsx = pd.ExcelFile('C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V19.xlsx')
df_digitacao    = pd.read_excel(xlsx, 'Banco digitação')
df_aux_juazeiro = pd.read_excel(xlsx, 'Aux_Juazeiro')
global newDF
newDF = pd.DataFrame()

    

def read_database(df1, df2):
    temp = 0
    for line_i in df1.itertuples():
        if line_i.local == 'Juazeiro':
            for line_j in df2.itertuples():
                if line_i.cod_inep == line_j.EscolaID:
                    if line_i.cod_inep != temp:
                        temp = line_i.cod_inep
                        cod1 = line_i.cod_inep
                        cod2 = line_j.EscolaID
                        itaration(cod1,cod2, df1, df2,newDF)
                        print("Passei aqui {0} {1}" . format(cod1, cod2))
                        break
                    else:
                        break        
                    
def itaration(cod1, cod2, df1, df2, newDF):
    name1 = pd.DataFrame(df1[df1.cod_inep == cod1].nm_aluno)
    name2 = pd.DataFrame(df2[df2.EscolaID == cod2].Nome_Aluno)
    for i in name1.itertuples():
        for j in name2.itertuples():
            percent = ls.compare(i.nm_aluno, j.Nome_Aluno)
            df = {'index_a':i.Index+2, 'cod_escola_a': cod1, 'nome_aluno_a': i.nm_aluno, 'index_b':j.Index+2, 'cod_escola_b': cod2, 'nome_aluno_b':j.Nome_Aluno, 'Semelhanca': percent}
            newDF = newDF.append(df, ignore_index=True)
            print("index:{0}, Nome:{1}, index:{2}, nome:{3} {4}%" . format(i.Index+2, i.nm_aluno, j.Index+2, j.Nome_Aluno, percent))
            # print("Nome1:{0}. Cod. Escola1:{1}. Nome2:{2}. Cod. Escola2:{3} {4}% " . format(i.nm_aluno, cod1, j.Nome_Aluno, cod2, percent ))

read_database(df_digitacao, df_aux_juazeiro)  

writer = pd.ExcelWriter('C:/Users/admin/Documents/Levenshtein-Distance/bases/output.xlsx')
newDF.to_excel(writer,'Sheet1')
writer.save

end = timeit.default_timer()
print(newDF)
print ('duration: %f' % (end - start))                  


    