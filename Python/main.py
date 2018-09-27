from program import Generic

class Main:
    file = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/Compacto_monitoramento_V19.xlsx'
    output = 'C:/Users/admin/Documents/Levenshtein-Distance/bases/output_V4.xlsx'
    sheet1 = 'Banco digitação'
    sheet2 = 'Aux_Feira'
    t = Generic(file, sheet1, sheet2)
    t.export(output)
    t.append

  
   

