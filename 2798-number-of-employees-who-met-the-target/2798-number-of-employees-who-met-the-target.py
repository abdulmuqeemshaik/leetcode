class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for val in range(len(hours)):
            if(target<=hours[val]):
                count+=1
        return count