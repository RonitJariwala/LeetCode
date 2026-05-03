class Solution:

    def isSafe(self,row,col,board,n):
        #check left
        for j in range(col):
            if board[row][j]=='Q':
                return False
        #check upper left
        i,j=row,col
        while i>=0 and j>=0:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        #check lower left diagonal
        i,j=row,col
        while i<n and j>=0:
            if board[i][j]=='Q':
                return False
            i+=1
            j-=1
        #safe
        return True
        
    def solve(self,col,board,ans,n):
        if col==n:
            temp=[''.join(row) for row in board]
            ans.append(temp)
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]='Q'
                self.solve(col+1,board,ans,n)
                board[row][col]='.'  #backtrack

    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.' for _ in range(n)] for _ in range(n)]
        ans=[]
        self.solve(0,board,ans,n)
        return ans