class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxLenght=0
        for i in range(n):
            hash_set=[0]*256 #for asci characters
            for j in range(i,n):
                if hash_set[ord(s[j])]==1:
                    break       
                hash_set[ord(s[j])]=1
                leng=j-i+1
                maxLenght=max(maxLenght,leng)
        return maxLenght