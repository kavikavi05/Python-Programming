class Solution(object):
    def preorder(self, root):
        output=[]
        if not root:
            return 

        stack=[root]

        while stack:
            node=stack.pop()

            output.append(node.val)

            for i in reversed(node.children):
                stack.append(i)
        
        return output



        
