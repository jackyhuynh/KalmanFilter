import math
from math import sqrt
import numbers


def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

#
# class matrix 
#############################
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        self_deter = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                # if the value is smaller than 0, get the absolute value of i
                new_row.append(abs(self[i][j]))
                print(abs(self[i][j]))
            self_deter.append(new_row)
 
        return Matrix(self_deter)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        sum = 0
        # Get the sum of all the diagnol value
        for i in range(self.h):
            sum += self[i][i]
            
        return sum
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        # define blank inverse matrix
        inverse = []
        
        if self.h == 1:
            inverse.append([1./self[0][0]])
        elif self.h == 2:
            # If the matrix is 2x2 check if it is inversable
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the 2x2 matrix
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]
                
                # get the factor value
                factor = 1/ (a*d - b*c)
                
                # assign the value to the inverse matrix
                inverse= [[d, -b],[-c, a]]
                
                # Tracel through the vector and return the inverse vector
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
                        
        # return the inverse vector              
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        # get the new length of the array
        new_row = self.w 
        
        # for loop that iterate through the loop
        for i in range(new_row):
            column = []
            for r in range(self.h):
                column.append(self[r][i])    
            matrix_transpose.append(column)
        
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        sum_matrix = []
        for i in range(self.h):
            new_row = []
            
            for j in range(self.w):
                new_row.append(self[i][j] + other[i][j])
            
            # append the new line to the summ matrix
            sum_matrix.append(new_row)
            
        return Matrix(sum_matrix)
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        """
        
        neg_self = []
        for i in range(self.h):
            new_row = []
            
            for j in range(self.w):
                new_row.append(self[i][j] * -1)
                
            # append the new row to the negative matrix
            neg_self.append(new_row)
        
        # return negative matrix
        return Matrix(neg_self)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtract if the dimensions are the same") 
        
        sub_matrix = []
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self[i][j] - other[i][j])
            
            # append the new line to the subtract matrix
            sub_matrix.append(new_row)
        
        # return subtract matrix
        return Matrix(sub_matrix)
    
    def get_column(matrix, column_number):
        column = []
        for r in range(matrix.h):
            column.append(matrix[r][column_number])

        return column
    
    def dot_product(vector_one, vector_two):
        """
        dot_product() that has two vectors as inputs and outputs the 
        dot product of the two vectors.
        """
        
        if (len(vector_one) != len(vector_two)):
            return "vector size is not equal"
        sum = 0
        for i in range(len(vector_one)):
            sum += vector_one[i]*vector_two[i]
        return sum    

            
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        m_rows = self.h
        p_columns = other.w
         # empty list that will hold the product of AxB
        result = []

        for i in range(m_rows):
            row_result = []

            # Get the row of first matrices
            vector_one = self[i]
            for j in range(p_columns):

                # Get each column of the second matrices by j index
                vector_two = Matrix.get_column(other,j)
                row_result.append(Matrix.dot_product(vector_one,vector_two))

            result.append(row_result)
        
        return Matrix(result)


    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            rmul_matrix = []
            for i in range(self.h):
                new_row=[]
                for j in range(self.w):
                    new_row.append(other*self[i][j])
                    
                rmul_matrix.append(new_row)
            return Matrix(rmul_matrix)
        else:
            return self
                    
            
            
            
            