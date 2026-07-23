class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        hash_len=[-1]*256
        l,r,maxLen=0,0,0
        while r<n:
            if hash_len[ord(s[r])]!=-1:
                l=max(hash_len[ord(s[r])]+1,l)
            maxLen=max(maxLen,r-l+1)
            hash_len[ord(s[r])]=r
            r+=1
        return maxLen