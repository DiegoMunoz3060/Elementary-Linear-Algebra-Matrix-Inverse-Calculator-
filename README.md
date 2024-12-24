# Matrix Inverse Calculator

This project is a stand-alone program designed to calculate the inverse of matrices of various sizes. Developed as part of an honors project for Linear Algebra, the program includes algorithms for determinant calculation utilizing the cofactor expansion algorithm, and Reduced Row Echelon Form (RREF) conversion, along with a GUI implementation using Tkinter.

[Project Documentation](https://docs.google.com/document/d/e/2PACX-1vTPo5_JCOv6qMG_FXFnsRALtCrRJA8xmDIOdy1mKP2JJCXpMfFtCdSwEsw0SwBmOazu9Bg865nRTSLm/pub)


## Files
- **Main**:
  - This file includes comments made throught the process of each phase
  - Running this program will output a determinant, an inverse matrix and launch the GUI
  - For a smooth compilation follow "Installation"
- **CofactorExpansion**:
  - This file is not part of the Inverse Calculator program.
  - Cofactor expansion is an algorithm used to find the determinant of any size matrix
  - You do not need to install any libraries for this file
- **InverseCalculator**:
  - This is the backend of the GUI program
  - TKinter is required to run tbis program
    
## Features

- **Recursive Cofactor Expansion**:
  - Computes determinants for 2x2 and 3x3 matrices.
  - Implements the cofactor expansion algorithm recursively.
  - Handles minors calculation using Python's modulus operator.

- **Matrix Inversion Using Adjoining and RREF**:
  - Augments input matrices with identity matrices.
  - Applies elementary row operations (swapping, scaling, and adding rows).
  - Outputs the inverse matrix after transforming the augmented matrix to RREF.

- **Graphical User Interface (GUI)**:
  - Developed using the Tkinter library.
  - Accepts user input for matrix size and elements.
  - Displays the computed inverse or error messages for singular matrices.
  - Dynamic memory allocation for creating the matrix grid.

## Limitations

- Only supports integer inputs (future updates will add support for special constants and fractions).
- Outputs are limited to 8 significant figures, with values beyond displayed in scientific notation.
- GUI has minor clearing issues when resetting the inverse output.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Matrix-Inverse-Calculator.git
   cd InverseCalculator
