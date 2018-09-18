def iterative_levenshtein(s, t):
  
    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings 
    
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution
    
    for r in range(rows):
        dist[r]
    
    return dist[row][col]

# compare similarity in percentage
def compare(a,b):
    distance = iterative_levenshtein(a, b)
    
    if distance == 0: 
        return 100
    
    lenght = max(len(a),len(b))

    if distance == lenght:
        return 0
    
    inverted = invert(distance, lenght)
    percent = (inverted/lenght)*100

    return round(percent)


def invert(min,max):
    return max-min

# print("Levenshtien distance: ", iterative_levenshtein("Kleyto ", "Kleyton"))
# print("Levenshtien distance: {0}%" .format(compare("Kleyto", "Kleyton")))












