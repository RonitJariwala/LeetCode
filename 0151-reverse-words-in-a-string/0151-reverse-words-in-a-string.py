class Solution:
    def reverseWords(self, s: str) -> str:
        word=""
        words=[]
        for char in s:
            if char!=" ":
                word+=char
            elif word:
                words.append(word)
                word=''
        if word:
            words.append(word)
        words.reverse()
        return " ".join(words)
