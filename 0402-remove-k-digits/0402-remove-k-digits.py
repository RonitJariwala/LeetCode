class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for digit in num:
            while st and k>0 and st[-1]>digit:
                st.pop()
                k-=1
            st.append(digit)
        # edge cases if more digits can be removed  
        while st and k>0:
            st.pop()
            k-=1
        # not stack k==input string    
        if not st:
            return "0"
        # to store the res
        res=""
        while st:
            res+=st.pop()
        res=res.rstrip('0') #remove trailing zeroes from right
        res=res[::-1] #reverse number
        if not res:
            return "0"
        return res
