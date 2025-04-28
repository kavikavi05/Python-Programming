class Solution(object):
    def inorderTraversal(self,root):
        self.l=[]
        self.helper(root)
        return self.l
    def helper(self,node):
        if node is None:
            return
        self.helper(node.left)
        self.l.append(node.val)
        self.helper(node.right)
