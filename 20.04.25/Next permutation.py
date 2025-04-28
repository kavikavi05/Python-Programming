class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(-2,-n-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[i],nums[j] = nums[j], nums[i]
                        nums[i+1:] = reversed(nums[i+1:])
                        return       
        nums.reverse()
