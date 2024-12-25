class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        parans_pair = {
            ')': '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in parans_pair:
                if not stack or stack[-1] != parans_pair[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        if len(stack) > 0:
            return False
        
        return True
