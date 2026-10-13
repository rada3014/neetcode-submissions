class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        st =1
        end =1
        size = len(nums)-1
        pre_list = []
        post_list = []
        final_result = []

        for i in range(len(nums)):
            pre_list.append(st)
            st=st*nums[i]
            post_list.append(end)
            end = end * nums[size]
            size = size-1

        size = len(pre_list)
        #print(size)
        for i in range(size):
            final_result.append(pre_list[i]*post_list[size-1])
            size = size-1

        return final_result


