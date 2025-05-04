class Solution(object):
    def findDuplicate(self, nums):
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
