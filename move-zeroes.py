class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        w=0
        for r in range(len(nums)):
            if nums[r] != 0 :
                nums[r],nums[w] = nums[w],nums[r]
                w+=1