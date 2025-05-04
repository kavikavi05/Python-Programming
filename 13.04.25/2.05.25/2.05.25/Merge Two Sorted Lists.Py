class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        final_result=ListNode()
        current_node=final_result
        
        while list1 and list2:
            if list1.val<list2.val:
                current_node.next=list1
                list1=list1.next
            else:
                current_node.next=list2
                list2=list2.next
            current_node=current_node.next
            
        
        if list1:
            current_node.next=list1
        if list2:
            current_node.next=list2

        return final_result.next
