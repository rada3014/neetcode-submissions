class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table=dict()

        for j in range(len(nums)):
            hash_table[nums[j]]=j


        for i in range(len(nums)):
            balance = target - nums[i]

            if balance in hash_table:
                if hash_table[balance]!=i:
                    return [i,hash_table[balance]]



        