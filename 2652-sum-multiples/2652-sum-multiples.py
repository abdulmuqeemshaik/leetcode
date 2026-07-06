class Solution:
    def sumOfMultiples(self, n: int) -> int:
        Sum=0
        for val in range(1,n+1):
            if(val%3==0 or val%5==0 or val%7==0):
                Sum+=val
        return Sum
                
        