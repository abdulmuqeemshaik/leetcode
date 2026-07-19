class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        rev=str(x)
        return rev==rev[::-1]
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

        