class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count1=0
        count2=0
        for val in nums:
            if(val<10):
                count1+=val
            else:
                count2+=val
        return count1!=count2