class Solution:
    def isPalindrome(self, x: int) -> bool:
        # temp=x
        # rev=0
        # while(x>0):
        #     last=x%10
        #     rev=(rev)*10+last
        #     x//=10
        # if(temp==rev):
        #     return True
        # else:
        #     return False
        if(x<0):
            return False


        s=str(x)
        return s==s[::-1]

        