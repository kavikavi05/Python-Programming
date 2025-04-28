class Solution(object):


    # this is the memomization sol
    def find(self, n, dp):
        if n == 0 or n== 1:
            return 1
        if n in dp:
            return dp[n]
        ways = self.find(n-1, dp) + self.find(n-2, dp)
        dp[n] = ways
        return ways

    # tabulation sol
    def tabulation(self, n):
        dp = [-1] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # space optimised tabulation
    def space_opt_tabulation(self, n):
        prev, prev2 = 1, 1
        for i in range(2, n+1):
            prev, prev2 = prev + prev2, prev
        return prev
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.space_opt_tabulation(n)
        
