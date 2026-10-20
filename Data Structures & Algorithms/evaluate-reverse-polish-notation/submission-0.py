class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        operands = set(['+', '-', '*', '/'])

        result = []

        for i in tokens:
            if i not in operands:
                result.append(int(i))
            else:
                if i=='+':
                    temp_result = result[-2]+result[-1]
                elif i=='-':
                    temp_result = result[-2]-result[-1]
                elif i=='*':
                    temp_result = result[-2]*result[-1]
                else:
                    temp_result = result[-2]/result[-1]
                result.pop()
                result.pop()
                result.append(int(temp_result))
        return result[-1]