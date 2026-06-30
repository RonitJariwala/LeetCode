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
            st.append(i)
        return ans

    def findNGE(self,arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n-1,-1,-1):
            curEl=arr[i]
            while st and arr[st[-1]]<=curEl:
                st.pop()
            ans[i]=st[-1] if st else n
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
    
    def findPGE(self,arr):
        n=len(arr)
        ans=[0]*n
        st=[]
        for i in range(n):
            curEl=arr[i]
            while st and arr[st[-1]]<curEl:
                st.pop()
            ans[i]=st[-1] if st else -1
            st.append(i)
        return ans
    
    def subarrayMins(self,arr): #use nse and pse in this
        nse=self.findNSE(arr)
        pse=self.findPSE(arr)
        n=len(arr)
        total_sum=0
        for i in range(n):
            left=i-pse[i]
            right=nse[i]-i
            freq=left*right*1
            val=(freq*arr[i]*1)
            total_sum+=val
        return total_sum
    
    def subarrayMaxs(self,arr):  #use nge and pge in this
        nge=self.findNGE(arr)
        pge=self.findPGE(arr)
        n=len(arr)
        total_sum=0
        for i in range(n):
            left=i-pge[i]
            right=nge[i]-i
            freq=left*right*1
            val=(freq*arr[i]*1)
            total_sum+=val
        return total_sum

    def subArrayRanges(self,nums):
        return (self.subarrayMaxs(nums)-self.subarrayMins(nums))
