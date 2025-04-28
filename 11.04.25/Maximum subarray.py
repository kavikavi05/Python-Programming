class Solution(object):
    #Kadane's Algorithm
    def maxSubArray(self, nums):
        sum = 0
        largest = float('-inf')
        for i in range(len(nums)):
            sum += nums[i]

            if sum > largest:
                largest = sum
            
            if sum < 0:
                sum = 0
        return large
