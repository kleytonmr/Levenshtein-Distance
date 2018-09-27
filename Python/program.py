import levenshtein as ls 
import pandas as pd 

class Generic:

    def __init__(self, file, sheet1, sheet2):
        self.appended_data = pd.DataFrame()
        self.xlsx = pd.ExcelFile(file)
        self.df_digitacao = pd.read_excel(self.xlsx, sheet1)
        self.df_aux_feira = pd.read_excel(self.xlsx, sheet2)
        self.read_database(self.df_digitacao,self.df_aux_feira) 
    
    @property
    def append(self):
        print(self.appended_data.head(100))
        return self.appended_data
    
    @append.setter
    def append(self, value):
        self.appended_data = self.appended_data.append(value, ignore_index=True)

    def read_database(self,df1, df2):
        temp = 0
        for i in df1.itertuples():
            if i.local == 'Feira de Santana':
                for j in df2.itertuples():
                    if i.cod_inep == j.inep_escola:
                        if i.cod_inep != temp:
                            cod1 = temp = i.cod_inep
                            cod2 = j.inep_escola
                            self.itaration(cod1,cod2, df1, df2)
                            print("Passei aqui {0} {1}" . format(cod1, cod2))
                            break
                        else:
                            break        

    def itaration(self,cod1, cod2, df1, df2):
        df_temp_a = pd.DataFrame(df1[df1.cod_inep == cod1])
        df_temp_b = pd.DataFrame(df2[df2.inep_escola == cod2])

        for i in df_temp_a.itertuples():
            for j in df_temp_b.itertuples():
                percent = ls.compare(i.nm_aluno, j.aluno)
                df = {'index_a':i.Index+2, 'cod_escola_a': cod1,'ano_a:':i.ano_curso, 'aluno_a':i.nm_aluno, 'index_b':j.Index+2, 'cod_escola_b': cod2,'ano_b:':j.serie, 'aluno_b':j.aluno, 'Semelhanca %': percent}
                self.append = df
                print("index:{0}, Nome:{1}, index:{2}, nome:{3} {4}%" . format(i.Index+2, i.nm_aluno, j.Index+2, j.aluno, percent))
    
    def export(self, file):
        writer = pd.ExcelWriter(file)
        new_df = self.appended_data.loc[self.appended_data.groupby('aluno_a', sort=False)['Semelhanca %'].idxmax()]
        new_df.to_excel(writer,'Sheet1')
        writer.save()
    
    
    
    
    
  