class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs):
            #print(len(strs))
            
            if strs!=[""]:
                return ('_+-').join(strs)
            else:
                return ""
        else:
            return 'None'

    def decode(self, s: str) -> List[str]:

        if s=='None':
            return []
        else:
            if len(s):
                return s.split('_+-')
            else:
                return [""]
