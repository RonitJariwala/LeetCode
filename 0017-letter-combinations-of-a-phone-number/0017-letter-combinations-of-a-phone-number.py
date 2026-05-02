class Solution:

    def findComb(self,ind,digits,ds,ans,phone_map):
        if ind==len(digits):
            ans.append("".join(ds))
            return
        current_digits=digits[ind]
        possible_letter=phone_map[current_digits]
        for letter in possible_letter:
            ds.append(letter)
            self.findComb(ind+1,digits,ds,ans,phone_map)
            ds.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map={
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        ans=[]
        self.findComb(0,digits,[],ans,phone_map)
        return ans