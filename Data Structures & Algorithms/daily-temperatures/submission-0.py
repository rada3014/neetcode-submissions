class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
    
        waiting_stack_index = []

        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):

        
            while waiting_stack_index and temperatures[waiting_stack_index[-1]]<temperatures[i]:
                    j = waiting_stack_index.pop()
                    answer[j] = i - j   
                        
            waiting_stack_index.append(i)

        
                    
        return answer


        
        