class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        for i in nums:
            if abs(i) < abs(cand):
                cand = i
        if cand<0 and abs(cand) in nums:
            return abs(cand)
        else:
            return cand        