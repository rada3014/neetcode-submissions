class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        highest = 1
        nums_set = set(nums)

        if len(nums_set)>=1:
            
            hash_map = dict() 

            for i in nums: 
                if i-1 not in nums_set:
                    hash_map[i]=1

            for k in hash_map.keys():
                key_temp = k+1
                while key_temp in nums_set:
                    hash_map[k]=hash_map[k]+1
                    if hash_map[k]>highest:
                        highest=hash_map[k]
                    key_temp=key_temp+1
        else:
            highest=0
        
        return highest

        
       