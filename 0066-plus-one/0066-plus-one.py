class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        list1=[]
        for i in digits:
            string += str(i)
        string = str(int(string) + 1)
        for i in string:
            list1.append(int(i))
        return list1
        
        
        