class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = dict()
    
        result = []
        for i in nums:
            if i not in freq_dict:
                freq_dict[i]=1
            else:
                freq_dict[i]=freq_dict[i]+1

        list_val = [[] for i in range(max(freq_dict.values()))]

        
        for x,y in freq_dict.items():
            list_val[y-1].append(x)

        

        for p in list_val[::-1]:
            result.extend(p)
            if len(result)<k:
                continue 
            else:
                break

        return result[:k]


        


        