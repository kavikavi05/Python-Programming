class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def nCr(n, r):
            return (fact(n) / (fact(r) * fact(n - r)))

        def fact(n):
            if n == 0 or n==1:
                return 1
            res = 1
            for i in range(2, n+1):
                res = res * i 
            return res

        lis = []
        for i in range(0, rowIndex + 1):
            lis.append(nCr(rowIndex, i))

        return lis
