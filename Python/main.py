from program import Generic

class Main:

    @staticmethod
    def feira ():
        # Dataset
        file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V22.xlsx'
        sheet_a = 'Banco digitação'
        sheet_b = 'Aux_Feira'
        
        # Dataset output
        output  = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_Feira_de_Santana_V1.xlsx'

        # set variable name
        country  = 'Feira de Santana'
        local    = 'local'
        nm_a     = "nm_aluno"
        serie_a  = 'ano_curso'
        school_a = 'cod_inep'
        nm_b     = 'aluno'
        serie_b  = 'serie'
        school_b = 'inep_escola'

        # Feira de Santana
        feira = Generic(file, sheet_a, sheet_b, country, local, nm_a, serie_a, nm_b, serie_b, school_a, school_b )
        feira.export(output)
        feira.append
    
    @staticmethod
    def juazeiro ():
        # Dataset
        file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V22.xlsx'
        sheet_a = 'Banco digitação'
        sheet_b = 'Aux_Juazeiro'
        
        # Dataset output
        output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_juazeiro_V1.xlsx'

        # set variable name
        country  = 'Juazeiro'
        local    = 'local'
        nm_a     = "nm_aluno"
        serie_a  = 'ano_curso'
        school_a = 'cod_inep'
        nm_b     = 'nm_aluno'
        serie_b  = 'turma'
        school_b = 'escolaid'

        # Juazeiro
        juazeiro = Generic(file, sheet_a, sheet_b, country, local, nm_a, serie_a, nm_b, serie_b, school_a, school_b )
        juazeiro.export(output)
        juazeiro.append
    
    @staticmethod
    def portoVelho ():
        # Dataset
        file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V22.xlsx'
        sheet_a = 'Banco digitação'
        sheet_b = 'Aux_PV'
        
        # Dataset output
        output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_porto_velho_V1.xlsx'

        # set variable name
        country  = 'Porto Velho'
        local    = 'local'
        nm_a     = "nm_aluno"
        serie_a  = 'ano_curso'
        school_a = 'cod_inep'
        nm_b     = 'nm_aluno'
        serie_b  = 'serie'
        school_b = 'codesc'

        # Porto Velho
        portoVelho = Generic(file, sheet_a, sheet_b, country, local, nm_a, serie_a, nm_b, serie_b, school_a, school_b )
        portoVelho.export(output)
        portoVelho.append
    
    @staticmethod
    def maceio ():
        # Dataset
        file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V22.xlsx'
        sheet_a = 'Banco digitação'
        sheet_b = 'Aux_Maceio'
        
        # Dataset output
        output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_maceio_V1.xlsx'

        # set variable name
        country  = 'Maceió'
        local    = 'local'
        nm_a     = "nm_aluno"
        serie_a  = 'ano_curso'
        school_a = 'cod_inep'
        nm_b     = 'nm_aluno'
        serie_b  = 'nome_turma'
        school_b = 'codesc'

        # Maceió
        maceio = Generic(file, sheet_a, sheet_b, country, local, nm_a, serie_a, nm_b, serie_b, school_a, school_b )
        maceio.export(output)
        maceio.append

    @staticmethod
    def novoRecife ():
        # Dataset
        file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V22.xlsx'
        sheet_a = 'Banco digitação'
        sheet_b = 'Aux_Recife_novo'
        
        # Dataset output
        output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_novo_recife_V1.xlsx'

        # set variable name
        country  = 'Recife'
        local    = 'local'
        nm_a     = "nm_aluno"
        serie_a  = 'ano_curso'
        school_a = 'cod_inep'
        nm_b     = 'nm_aluno'
        serie_b  = 'serie'
        school_b = 'codesc'

        # Recife
        recife = Generic(file, sheet_a, sheet_b, country, local, nm_a, serie_a, nm_b, serie_b, school_a, school_b )
        recife.export(output)
        recife.append

Main.feira()
Main.juazeiro()
Main.portoVelho()
Main.novoRecife()
Main.maceio()   


  


