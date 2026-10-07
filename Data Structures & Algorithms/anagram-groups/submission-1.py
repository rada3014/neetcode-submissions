class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_freq_dict(s):
            out = dict()
            for i in s:
                if i not in out:
                    out[i]=1
                else:
                    out[i]=out[i]+1
            return dict(sorted(out.items(), key=lambda item: item[0])) 

        word_dict= dict()
        
        for s in strs:
            out = str(get_freq_dict(s))
            if out not in word_dict:
                word_dict[out] = [s]
            else:
                word_dict[out].append(s)

        return list(word_dict.values())
