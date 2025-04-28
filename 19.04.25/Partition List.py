class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        less_head=ListNode(0)
        great_head=ListNode(0)

        less=less_head
        great=great_head

        current=head
        while current:
            if current.val < x:
                less.next=current
                less=less.next

            else:
                great.next=current
                great=great.next
            current=current.next

        great.next=None
        less.next=great_head.next
        return less_head.next
