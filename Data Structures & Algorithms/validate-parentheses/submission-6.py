class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_pair = {'[':']','{':'}','(':')'}

        for c in s:
            if c in ['[','{','(']:
                stack.append(c)
            else:
                if len(stack):
                    if c == bracket_pair[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack):
            return False
        else:
            return True
            
        