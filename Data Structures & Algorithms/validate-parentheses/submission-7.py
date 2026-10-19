class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_pair = {'[':']','{':'}','(':')'}

        for i in range(len(s)):
            if s[i] in ['[','{','(']:
                stack.append(s[i])
            else:
                if len(stack):
                    if s[i] == bracket_pair[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack):
            return False
        else:
            return True
            
        