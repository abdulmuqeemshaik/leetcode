class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            Sum=0
            while(num>0):
                temp=num%10
                Sum+=temp
                num//=10
            num=Sum
        return num
