class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num=[]
        while n>0:
            num.append(n%10)
            n//=10
        num.reverse()
        ans=0
        for i in range(len(num)):
            if(i%2==0):
                ans+=num[i]
            else:
                ans-=num[i]
        return ans