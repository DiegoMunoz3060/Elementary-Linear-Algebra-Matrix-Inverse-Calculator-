def cofactorExpansion(matrix):
    #for i in len(arr)
    # Calculate the determinant using cofactor expansion
    #determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
   
    #BASE CASE
    if len(matrix) == 1: 
        return matrix[0][0]
    else:
        det = 0
        for j in range(len(matrix)):             # Loop over each element in the first row
            cofactor = ((-1) ** j) * matrix[0][j]   # Cofactor sign alternates
            minor = getMinor(matrix, j)         # Get minor by removing row 0 and column j
            det += cofactor * cofactorExpansion(minor)        # Recursive call to determinant of the minor
        return det

        #we need time for
        #calculate Minor
        #for j in arr:
            #if j % N == i:
                #here we actually want to delete the row, zero? 

            #now delete the first row     
         #update values 
        #after this for loop A should be a 2 by 2    
        #return matrix[i] * cofactorExpansionTest(a)    
    

    #first delete the col and then the row 


#we can call this function with the appropiate parameters
#skip_row = should be the first N indecies or the 0 row
#skip_col = should be determinen by the formula  i % N == j
#where N to be the size of the matrix, i is the indesie and j is the output that should start at 0 and go up to N by each iteration.   


def getMinor(matrix, i):
    N = len(matrix)  # Size of the matrix
    col_to_skip = i % N  # Determine which column to skip using modulus rule
    
    minor = []  # Initialize minor matrix
    
    for row_idx in range(1, N):  # Always going to be skipping the first row
        row = []
        for col_idx in range(N):  # Iterate through each column
            if col_idx == col_to_skip:  # Skip the column determined by modulus rule
                continue
            
            row.append(matrix[row_idx][col_idx])  # Add element to the new row
        
        minor.append(row)  # Add the row to the minor matrix
    
    return minor


testMatrix = [[2, 3, 1],[4, 5, 6],[7, 8, 9]]

print(cofactorExpansion(testMatrix))