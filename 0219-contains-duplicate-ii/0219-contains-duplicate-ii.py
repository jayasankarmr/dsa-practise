class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i,num in enumerate(nums):
            if num in seen:
                prev = seen[num]
                if i-prev <= k:
                    return True
            seen[num] = i
        return False
        