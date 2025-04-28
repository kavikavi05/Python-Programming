class Solution(object):
    def convertToTitle(self, columnNumber):
        v = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = 26
        title = ''
        
        while columnNumber > 0:
            columnNumber -= 1  
            index = columnNumber % n
            title = v[index] + title
            columnNumber //= n

        return title
        """
        :type columnNumber: int
        :rtype: str
        """
        
