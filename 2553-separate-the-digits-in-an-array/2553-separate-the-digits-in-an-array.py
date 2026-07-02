class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for val in nums:
            temp=[]
            while val>0:
                temp.append(val% 10)
                val//=10
            temp.reverse()
            for val in temp:
                ans.append(val)
        return ans