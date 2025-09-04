class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            count = 0
            for j in nums:
                if j == i:
                    count+=1
            if count == 1:
                return i

        