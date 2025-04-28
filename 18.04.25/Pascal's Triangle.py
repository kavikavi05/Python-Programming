class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l = [[1]]
        for _ in range(1,numRows):
            ll = l[-1]
            newl = [1]
            for i in range(len(ll)-1):
                newl.append(ll[i]+ll[i+1])
            newl.append(1)
            l.append(newl)
        return l
