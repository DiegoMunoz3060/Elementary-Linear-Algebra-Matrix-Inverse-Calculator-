#This program should simulate the algorithm cofactor expansion 
#how can numpy make my life simpler 

#computing RE along side with reducing (determinnant rules) elemenetary row
# Upper triangular matrix determinant 

import numpy as np
import tkinter as tk
from tkinter import messagebox




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


def adjoin_identity(matrix):
    N = len(matrix)  # Size of the matrix
    identity_matrix = []  # Create identity matrix
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity_matrix.append(row)
    
    adjoined_matrix = []  # Initialize the adjoined matrix
    
    for i in range(N):
        adjoined_matrix.append(matrix[i] + identity_matrix[i])  # Combine rows of input matrix and identity matrix
    
    return adjoined_matrix

# Example usage


#we need to RREF the matrix
def swap_rows(matrix, i, j):
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp

def scale_row(matrix, rowIndex, scalar):
    matrix[rowIndex] = [scalar * x for x in matrix[rowIndex]]

#Add a scalar multiple of one row to another row
def add_row(matrix, src, dest, scalar):
    #Computes R(dest) = R(dest) + scalar * R(src)
    #Zip is used to iterate over parallel lists, in this case the rows of the matrix from the source and destination
    matrix[dest] = [a + scalar * b for a, b in zip(matrix[dest], matrix[src])]


#Next step is calculate determinant and inverse at the same time by adjoinging the Identity matrix with the appropiate size
#We need to RREF the Inverse matrix, thus the matrix we are RREF is double the size.
#Since we are using elementary operations the determinant will be the product of the inverse of any scalar multiple and a -1 when you swap rows
#Once the left side resembles the Identity matrix the right side will be our inverse
#if diagonal has a 0 determinant is 0 and matrix is invertible
#how do you RREF with elemantary operations?
#should chek if the first element is either 1 or 0, the first element value should increament by 1 till N, 
#I think the first step should be to check if any rows start at 1 becasue then we can just make that our first row
#if 1 then we can either multiply by the elements recipocrate to get one
#

  
#Now that we have our functions we need to know when we should use them, what is the most efficient way? should we just use the pattern that we know? 
#Using the pattern that we know from class we start by 


input_matrix = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]
adjoined_matrix = adjoin_identity(input_matrix)

for row in adjoined_matrix:
    print(row)

# Swap rows 0 and 1
def testSwap():
    swap_rows(adjoined_matrix, 0, 1)
    print(" ")
    for row in adjoined_matrix:
        print(row)

def testScale():
    scale_row(adjoined_matrix, 2, 1/7)
    print(" ")
    for row in adjoined_matrix:
        print(row)

def testAdd():
    add_row(adjoined_matrix, 2, 1)
    print(" ")
    for row in adjoined_matrix:
        print(row)
#RREF process: start with the last row first column, make it 0 by scaling it by the reciprocal of its value; 
#should we also be looikng for 0? that is to say swapping? 
#right now my implimentation only scales the row, should I also be looking for 0?
#This does not make it go to 0 but 1, so if we want to make the last row first column 0 we should multply by the NEGATIVE multiple of the next row IN THE SAME COLUMN then add it to the row we want to make 0


#QUESTION FOR MR.O, how should I implement the elementary operations? how we did it in class? Is there a more efficent way? 

#

# def adjoin_identity(matrix):
#     """
#     Create the augmented matrix [A | I], where I is the identity matrix.
#     """
#     N = len(matrix)  # Size of the matrix
#     identity_matrix = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
#     adjoined_matrix = [matrix[i] + identity_matrix[i] for i in range(N)]
#     return adjoined_matrix


# def swap_rows(matrix, i, j):
#     """
#     Swap row i and row j in the matrix.
#     """
#     matrix[i], matrix[j] = matrix[j], matrix[i]

# def scale_row(matrix, i, scalar):
#     """
#     Scale row i by a given scalar.
#     """
#     matrix[i] = [scalar * x for x in matrix[i]]

def rref(matrix):
    
    N = len(matrix)
    augmented_matrix = adjoin_identity(matrix)

    for col in range(N):
        # Step 1: Ensure pivot is non-zero; if zero, swap rows
        if augmented_matrix[col][col] == 0:
            for row in range(col + 1, N):
                if augmented_matrix[row][col] != 0: 
                    swap_rows(augmented_matrix, col, row) 
                    break 
            else:
                raise ValueError("Matrix is singular and cannot be inverted.")

        # Step 2: Normalize pivot row
        pivot = augmented_matrix[col][col]
        scale_row(augmented_matrix, col, 1 / pivot)

        # Step 3: Eliminate the current column in other rows
        for row in range(N):
            if row != col:
                factor = -augmented_matrix[row][col]
                add_row(augmented_matrix, col, row, factor)

    # Extract the right part of the augmented matrix, which is the inverse and round to 1 decimal place
    inverse_matrix = []
    for row in augmented_matrix:
        inverse_row = []
        for element in row[N:]:
            inverse_row.append(round(element, 8))
        inverse_matrix.append(inverse_row)
    
    return inverse_matrix

# Example usage
matrix = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
]

try:
    inverse = rref(matrix)
    print("Inverse matrix:")
    for row in inverse:
        print(row)
except ValueError as e:
    print(e)


def get_matrix(entries, size):
    try:
        return [[float(entries[i][j].get()) for j in range(size)] for i in range(size)]
    except ValueError:
        raise ValueError("Please enter valid numbers in all fields.")

def display_result(matrix, result_frame):
    """Display the result matrix in the GUI."""
    for widget in result_frame.winfo_children():
        widget.destroy()

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            tk.Label(result_frame, text=f"{value}", relief="solid", width=10).grid(row=i, column=j) #:2f is the number of decimal places

# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Matrix Calculator")

    size_label = tk.Label(root, text="Matrix Size (e.g., 3 for 3x3):")
    size_label.grid(row=0, column=0)

    size_entry = tk.Entry(root, width=5)
    size_entry.grid(row=0, column=1)

    input_frame = tk.Frame(root)
    input_frame.grid(row=1, column=0, columnspan=2)

    result_frame = tk.Frame(root)
    result_frame.grid(row=3, column=0, columnspan=2, pady=10)

    entries = []

    def create_matrix_grid():
        """Dynamically create entry grid for the matrix."""
        nonlocal entries
        entries = []
        for widget in input_frame.winfo_children():
            widget.destroy()

        try:
            size = int(size_entry.get())
            if size <= 0:
                raise ValueError("Size must be a positive integer.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for size.")
            return

        for i in range(size):
            row = []
            for j in range(size):
                entry = tk.Entry(input_frame, width=5, justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                row.append(entry)
            entries.append(row)

    def compute_inverse():
        """Compute and display the inverse matrix."""
        try:
            size = int(size_entry.get())
            matrix = get_matrix(entries, size)
            result = rref(matrix)
            display_result(result, result_frame)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    create_button = tk.Button(root, text="Create Matrix", command=create_matrix_grid)
    create_button.grid(row=0, column=2, padx=5)

    compute_button = tk.Button(root, text="Compute Inverse", command=compute_inverse)
    compute_button.grid(row=2, column=0, columnspan=2, pady=10)

    clear_button = tk.Button(root, text="Clear", command=lambda: [widget.destroy() for widget in input_frame.winfo_children()])
    clear_button.grid(row=2, column=2, pady=10)

    root.mainloop()

# Run the GUI
create_gui()