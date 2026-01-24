''' Shortcut for rotations
90 = transpose + reverse row
180 = reverse row + reverse column
270 = transpose + reverse col
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #Transpose matrix
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #Reverse the rows of matrix
        for i in range(n):
            matrix[i].reverse()

        