class Solution:
    def frequencySort(self, s: str) -> str:
        freq=[(0,chr(i)) for i in range(128)]
        for ch in s:
            index=ord(ch)
            freq[index]=(freq[index][0]+1,ch)
        freq.sort(key=lambda x: (-x[0],x[1]))
        res=[ch*f for f,ch in freq if f>0]
        return "".join(res)