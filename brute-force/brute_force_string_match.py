# Searching for a pattern "P" in text "T"

def brute_force_string_match(T, P):
    n = len(T) 
    m = len(P)

    for i in range(n-m+1):
        j = 0
        while j<m and P[j]==T[i+j]:
            j = j+1
        
        if j == m:
            return i
    
    return -1
