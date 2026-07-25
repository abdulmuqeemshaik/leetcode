class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return []  # No solution found
        
        # optimal  
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in  d:
                return (d[diff],i)
                break
            d[nums[i]]=i
        
        # num_to_index={} 
        # for i,num in enumerate(nums):
        #     complement=target-num
        #     # If complement exists, we found our pair
        #     if complement in num_to_index:
        #         return [num_to_index[complement],i]
        #     # Store current number and its index in the hash map
        #     num_to_index[num]=i