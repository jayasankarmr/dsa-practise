from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counter = Counter(magazine)
        for i in ransomNote:
            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else :
                counter[i] -= 1
        return True