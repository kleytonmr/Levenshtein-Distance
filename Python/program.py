import levenshtein as ls 
import pandas as pd 

class Generic:

    def __init__(self, file, sheet_a, sheet_b, country, local, nm_a, serie_a,nm_b, serie_b, school_a, school_b): #construct
        self.appended_data = pd.DataFrame()
        # country
        self.country = country

        # set variable name 
        self.local = local
        self.nm_a = nm_a
        self.serie_a = serie_a
        self.nm_b = nm_b
        self.serie_b = serie_b
        self.school_a = school_a
        self.school_b = school_b

        # import dataset 
        self.xlsx = pd.ExcelFile(file)
        self.df_database_a = pd.read_excel(self.xlsx, sheet_a)
        self.df_database_b = pd.read_excel(self.xlsx, sheet_b)
        self.read_database(self.df_database_a,self.df_database_b) 
    
    @property # getAppend
    def append(self):
        print(self.appended_data.head(100))
        return self.appended_data
    
    @append.setter # setAppend
    def append(self, value):
        self.appended_data = self.appended_data.append(value, ignore_index=True)

    def read_database(self,df1, df2):
        temp = 0
        for i in df1.itertuples():
            if getattr(i, self.local) == self.country:
                for j in df2.itertuples():
                    if getattr(i, self.school_a) == getattr(j, self.school_b):
                        if getattr(i, self.school_a) != temp:
                            cod1 = temp = getattr(i, self.school_a)
                            cod2 = getattr(j, self.school_b)
                            self.itaration(cod1,cod2, df1, df2)
                            print("Passei aqui {0} {1}" . format(cod1, cod2))
                            break
                        else:
                            break        

    # get the current school and compare the students of the bank "A" with the students of the bank "B"
    def itaration(self,cod1, cod2, df1, df2): 
        df_temp_a = pd.DataFrame(df1[df1[self.school_a] == cod1])
        df_temp_b = pd.DataFrame(df2[df2[self.school_b] == cod2])

        for i in df_temp_a.itertuples():
            for j in df_temp_b.itertuples():
                percent = ls.compare(getattr(i, self.nm_a), getattr(j, self.nm_b))
                df = {'index_a':i.Index+2, 'cod_escola_a': cod1,'ano_a':getattr(i,self.serie_a), 'aluno_a':getattr(i,self.nm_a), 'index_b':j.Index+2, 'cod_escola_b': cod2,'ano_b':getattr(j,self.serie_b), 'aluno_b':getattr(j,self.nm_b), 'Semelhanca %': percent}
                self.append = df
                print("index:{0}, Nome:{1}, index:{2}, nome:{3} {4}%" . format(i.Index+2, getattr(i,self.nm_a), j.Index+2, getattr(j,self.nm_b), percent))
    
    def export(self, file): #export bank group by "Semelhança"
        writer = pd.ExcelWriter(file)
        new_df = self.appended_data.loc[self.appended_data.groupby('aluno_a', sort=False)['Semelhanca %'].idxmax()]
        new_df.to_excel(writer,'Sheet1')
        writer.save()
    
    
    
    
    
  