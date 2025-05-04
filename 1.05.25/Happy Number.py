'''
Approach 1: Check for divergence if n == 2^31 - 1 then not happy 

'''

class Solution(object):
    def split(self, n): 
        nums = [0] 
        while n > 0: 
            q = n // 10
            r = (n % 10) ** 2 
            nums.append(nums[-1] + r) 
            n = q 
        return nums[-1]

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = set()
        while n < 2e31 - 1: 
            if n == 1: 
                return True 
            if n in memo: 
                return False 

            memo.add(n) 
            n = self.split(n)

        return False  
