class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Step 1: Place each number in its right index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        # Step 2: Find the first place where index doesn't match value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
