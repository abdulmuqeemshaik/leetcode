class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            temp=i
            sum=0
            while temp>0:
                sum+=temp%10
                temp//=10
            if sum%2==0:
                count+=1
        return count