class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' O(NlogN) better OPtimal uses SET O(N)
        n=len(nums)
        if n==0: return 0
        nums.sort()
        longest=1;cnt=0
        lastSmaller=float('-inf')
        for i in range(n):
            if nums[i]-1==lastSmaller:
                cnt+=1
                lastSmaller=nums[i]
            elif nums[i]!=lastSmaller:
                cnt=1
                lastSmaller=nums[i]
            longest=max(longest,cnt)
        return longest 
        '''
        n=len(nums)
        if n==0: return 0
        longest=0
        st=set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                cnt=1
                x=it
                while x+1 in st:
                    x+=1
                    cnt+=1
                longest=max(longest,cnt)
        return longest