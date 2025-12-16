class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s = set(jewels)
        for i in stones:
            if i in s:
                count += 1
        return count
        