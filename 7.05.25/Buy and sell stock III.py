class Solution(object):
    def maxProfit(self, prices):
        memo = [[[-1 for k in range(2)] for j in range(2)] for i in range(len(prices))]
        def cal(i, holding, tokens):
            if i>len(prices)-1 or (tokens<0 and not holding):
                return 0
            elif memo[i][holding][tokens]!=-1:
                return memo[i][holding][tokens]
            elif holding:
                memo[i][holding][tokens]= max(prices[i]+ cal(i+1, not holding, tokens), cal(i+1, holding, tokens))
            else:
                memo[i][holding][tokens]= max(-prices[i]+ cal(i+1, not holding, tokens-1), cal(i+1, holding, tokens))
            return memo[i][holding][tokens]
        return cal(0, 0, 1)
