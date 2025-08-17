class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if k == 0:
            return

        nums.reverse()
        self.reverse_partial(nums, 0, k - 1)
        self.reverse_partial(nums, k, n - 1)

    def reverse_partial(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1