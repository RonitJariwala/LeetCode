class Solution:
    def largestOddNumber(self, s: str) -> str:
        ind=-1
        i=0
        #find end index and then traverse from start to end eliminating zeroes
        for i in range(len(s)-1,-1,-1):
            if (int(s[i])%2)==1:
                ind=i
                break
            # skip leading zeroes 
        i=0
        while i<=ind and s[i]=='0':
                i+=1
        return s[i:ind+1]

