class Solution:


    def checkValidString(self, s: str) -> bool:
        min_open,max_open=0,0
        for char in s:
            if char=="(":
                min_open+=1
                max_open+=1
            elif char==")":
                min_open-=1
                max_open-=1
            else: #char=="*"
                min_open-=1  #assume "*" is ")"
                max_open+=1  #assume "*" is "("

            # If max_open drops below 0, ')' permanently outnumbers '('
            if max_open<0:
                return False

            # min_open cannot be negative (we can't have negative unmatched '(')
            if min_open<0:
                min_open=0

        return min_open==0