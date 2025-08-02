class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ssort=sorted(s)
        tsort=sorted(t)
        if ssort==tsort:
            return True
        else:
            return False
        