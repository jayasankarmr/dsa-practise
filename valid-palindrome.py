class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_s=""
        for i in s:
            if i.isalnum():
                clean_s+=i.lower()
            else:
                continue
        print(clean_s)
        if clean_s[::-1] == clean_s:
            return True
        else:
            return False
        