class Solution:

    def largestRectangle(self,heights):
        heights.append(0)
        stack=[]
        maxArea=0
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                maxArea=max(maxArea,height*width)
            stack.append(i)
        return maxArea


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m=len(matrix[0])
        height=[0]*m
        maxArea=0
        for row in matrix:
            for i in range(m):
                if row[i]=='1':
                    height[i]+=1
                else:
                    height[i]=0
            maxArea=max(maxArea,self.largestRectangle(height))
        return maxArea