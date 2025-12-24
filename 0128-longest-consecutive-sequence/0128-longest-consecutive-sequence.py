class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0  # Fixes the empty list case
        
        nums.sort()
        
        longest_streak = 1
        current_streak = 1
        
        for i in range(len(nums) - 1):
            if nums[i+1] != nums[i]: # Skip duplicates
                if nums[i+1] == nums[i] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1
        
        return max(longest_streak, current_streak)
        