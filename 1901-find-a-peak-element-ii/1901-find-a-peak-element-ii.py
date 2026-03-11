class Solution:
    def maxElement(self,mat,col):
        max_value=float('-inf')
        index=-1
        n=len(mat)
        for i in range(n):
            if mat[i][col]>max_value:
                max_value=mat[i][col]
                index=i
        return index

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            row=self.maxElement(mat,mid)
            left=mat[row][mid-1] if mid-1>=0 else float('-inf')
            right=mat[row][mid+1] if mid+1<m else float('-inf')
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif left>mat[row][mid]:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]