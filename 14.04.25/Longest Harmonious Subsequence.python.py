from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        numberCountsMap = Counter(nums)
        answer = 0
        for key in numberCountsMap:
            if key + 1 in numberCountsMap:
                answer = max(answer , numberCountsMap[key] + numberCountsMap[key + 1])
        return answer
