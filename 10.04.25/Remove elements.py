class Solution:
    def removeElement(self, nums, val):
        k = 0  # Pointer to track position of elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:  # If nums[i] is not val, keep it
                nums[k] = nums[i]
                k += 1  # Move pointer forward
        return k  # k is the number of valid elements
