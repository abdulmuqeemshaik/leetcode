class Solution:
    def countDigits(self, num: int) -> int:
        strn=str(num)
        count=0
        for i in strn:
            if(num%int(i)==0):
                count+=1
        return count    