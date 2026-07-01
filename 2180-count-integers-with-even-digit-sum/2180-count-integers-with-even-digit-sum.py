class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(1,num+1):
            temp=i
            Sum=0
            while(temp>0):
                digit=temp%10
                Sum+=digit
                temp=temp//10
            if(Sum%2==0):
                count+=1
        return count