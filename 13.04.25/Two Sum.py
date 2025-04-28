class Solution(object):
    def swapPairs(self,head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:return head  
        next_node=head.next
        head.next=self.swapPairs(next_node.next)
        next_node.next=head
        return next_node
