class Solution:
    def findNSE(self,arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            curEl=arr[i]
            while st and arr[st[-1]]>=curEl:
                st.pop()
            ans[i]=st[-1] if st else n
            # push the index of current el in stack
            st.append(i)
        return ans
    
    def findPSE(self,arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n):
            curEl=arr[i]
            while st and arr[st[-1]]>curEl:
                st.pop()
            ans[i]=st[-1] if st else -1
            st.append(i)
        return ans

    def sumSubarrayMins(self,nums):
        nse=self.findNSE(nums)
        pse=self.findPSE(nums)
        n=len(nums)
        mod=int(1e9+7)
        total_sum=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            freq=left*right*1
            val=(freq*nums[i])%mod
            total_sum=(total_sum+val)%mod
        return total_sum
