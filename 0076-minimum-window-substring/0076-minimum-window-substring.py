from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""
            
        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        res = [-1, -1]
        res_len = float('inf')
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in count_t and window[char] == count_t[char]:
                have += 1
                
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                    
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                    
                left += 1
                
        left_bound, right_bound = res
        return s[left_bound:right_bound+1] if res_len != float('inf') else ""