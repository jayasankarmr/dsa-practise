class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[w] = nums[i]
                w+=1
        return w
