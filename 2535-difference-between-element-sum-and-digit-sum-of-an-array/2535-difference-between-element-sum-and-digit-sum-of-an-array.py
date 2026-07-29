class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # element_sum=sum(nums)
        # digit_sum=0
        # for num in nums:
        #     for digit_char in str(num):
        #         digit_sum+=int(digit_char)
                
        # return abs(element_sum-digit_sum)

        
        element_sum=0
        digit_sum=0
        for num in nums:
            element_sum+=num
            while num>0:
                digit_sum+=num % 10
                num//=10
        return abs(element_sum-digit_sum)
        