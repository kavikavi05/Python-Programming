class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Checks for first 3 nodes in tree(used to check whether the tree consists of only one node, or 2 node or 3 node but the values of 2nd and 3rd nodes are different)
        if root.left==None and root.right==None:
            return True
        if (root.left!=None and root.right==None) or (root.left==None and root.right!=None):
            return False
        
        if root.left.val!=root.right.val:
            return False


        # Queue for left tree 
        left1=[root.left]
        # Queue for right tree
        right1=[root.right]


        while len(left1)>0 and len(right1)>0:
            # Check for values in queue(left1 and right1)
            if left1[0].val!=right1[0].val:
                return False

            # Travel in opposite direction and check whether the mirror element exists or not. Checks left node of left tree and right node of right tree.
            if left1[0].left!=None and right1[0].right!=None:
                left1.append(left1[0].left)
                right1.append(right1[0].right)
            elif left1[0].left==None and right1[0].right!=None:
                return False
            elif left1[0].left!=None and right1[0].right==None:
                return False

            # Same as above but checks for right tree node for left tree and left tree node for right tree
            if left1[0].right!=None and right1[0].left!=None:
                left1.append(left1[0].right)
                right1.append(right1[0].left)
            elif left1[0].right==None and right1[0].left!=None:
                return False
            elif left1[0].right!=None and right1[0].left==None:
                return False
            left1.pop(0)
            right1.pop(0)
        
        if len(left1)!=0 or len(right1)!=0:
            return False
        return True
            
