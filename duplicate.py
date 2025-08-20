class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup = set()
        for num in nums:
            if num in dup:
                return num
            dup.add(num)