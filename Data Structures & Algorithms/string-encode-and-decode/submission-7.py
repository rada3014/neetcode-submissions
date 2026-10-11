class Solution:

    def encode(self, strs: List[str]) -> str:

        if strs==[]:
            return ''
            
        else:
            return ('').join(strs)+'_' + str(('#').join([str(len(i)) for i in strs]))

    
    def decode(self, s: str) -> List[str]:

        if s=='':
            return []
        else:
            x= s.rsplit('_', 1)
            a,b = x[0],x[1]
            result = []
            curr =0 
            b=b.split('#')
        
            for i in range(len(b)):
            
                next = curr+int(b[i])
                result.append(a[curr:next])
                curr = next
                

            return result
