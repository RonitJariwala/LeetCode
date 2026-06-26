class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left,right=0,n-1
        maxLeft,maxRight=0,0
        totalWater=0
        while left<=right:
            if height[left]<height[right]:
                if height[left]>=maxLeft:
                    maxLeft=height[left]
                else:
                    totalWater+=maxLeft-height[left]
                left+=1
            else:
                if height[right]>=maxRight:
                    maxRight=height[right]
                else:
                    totalWater+=maxRight-height[right]
                right-=1
        return totalWater
            