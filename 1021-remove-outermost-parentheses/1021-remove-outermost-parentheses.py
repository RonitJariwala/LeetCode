class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        level=0
        for char in s:
            if char=='(':
                if level>0:
                    res+=char
                level+=1
            elif char==')':
                level-=1
                if level>0:
                    res+=char
        return res        