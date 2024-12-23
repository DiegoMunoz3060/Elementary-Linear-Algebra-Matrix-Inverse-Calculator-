import tkinter as tk
from tkinter import messagebox

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
            if row != col:  # The normalized pivot, should not be 0 out
                factor = -(augmented_matrix[row][col])  #Factor needs to be negative in order to 0 out the current column
                add_row(augmented_matrix, col, row, factor)

    # Extract the right part of the augmented matrix, which is the inverse and round to 1 decimal place
    inverse_matrix = []
    for row in augmented_matrix:
        inverse_row = []
        for element in row[N:]:
            inverse_row.append(round(element, 4))
        inverse_matrix.append(inverse_row)
    
    return inverse_matrix
#example
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

    clear_button = tk.Button(root, text="Clear", command=lambda: [widget.destroy() for widget in input_frame.winfo_children()]) #for widget in result_frame.winfo_children() clearing the result matrix
    clear_button.grid(row=2, column=2, pady=10)

    root.mainloop()

# Run the GUI
create_gui()