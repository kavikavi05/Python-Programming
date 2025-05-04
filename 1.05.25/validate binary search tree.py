class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isValid(root, max, min):
            if root is None:
                return True

            if min < root.val < max:
                return isValid(root.left, root.val, min) and isValid(root.right, max, root.val)

            return False

        return isValid(root, float("inf"), float("-inf"))
