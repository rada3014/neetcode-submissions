class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #nums = [-1,0,1,2,-1,-4]
        nums.sort()
        #print(nums)

        result_hash = dict()
        results = []
        for i in range(len(nums)):
            if nums[i] not in result_hash:
                result_hash[nums[i]]=i

        #print(result_hash)
        for a,b in result_hash.items():
            target = 0-a 
            #print('target:',target)
            s=b+1
            e= len(nums)-1
            while s<e:
                if nums[s]+nums[e]<target:
                    s=s+1
                elif nums[s]+nums[e]>target:
                    e=e-1
                else:
                    results.append([a,nums[s],nums[e]])
                    s += 1
                    e -= 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1

        return results
            
            
            