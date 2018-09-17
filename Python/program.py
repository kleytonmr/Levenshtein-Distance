from openpyxl import load_workbook 
import levenshtein

# print("Levenshtien distance: ", levenshtein.iterative_levenshtein("notKley", "Kleyton"))
# print("Levenshtien distance: {0}%" .format(levenshtein.compare("notKley", "Kleyton")))

baseA = load_workbook('../bases/base_a.xlsx')
baseB = load_workbook('../bases/base_b.xlsx')

nameA = baseA['Sheet1']
nameB = baseB['Sheet1']


# for x in range(2,18000):
#     print(nameA['A'+str(x)].value) 

for line_A in nameA.rows:
    for cell_A in line_A:
        # print("NomeA:" + cell_A.value)
        for line_B in nameB.rows:
            for cell_B in line_B:
                print("Comparei A: {0} com B: {1}" .format(cell_A.value, cell_B.value))
                # print("NomeB:" + cell_B.value)
                # if levenshtein.compare(cell_A.value,cell_B.value) >= 75:
                    # print("São iguais e passam no teste: {0}, {1}. Nível de semelhança: {2}% " .format(cell_A.value,cell_B.value,levenshtein.compare(cell_A.value,cell_B.value)))

        




