from program import Generic

class Main:

    # Dataset
    file    = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/base_teste.xlsx'
    sheet_a = 'Banco digitação'
    sheet_b = 'Aux_Feira'
    
    # Dataset output
    output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_V5.xlsx'

    # set name variable
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


    
    
   

  
   

