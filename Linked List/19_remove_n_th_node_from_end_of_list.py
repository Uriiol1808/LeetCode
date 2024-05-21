"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the
end of the list and return its head.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Init fast and slow pointers
        fast = slow = head

        # Put the second pointer just before the one we want to remove
        for _ in range(n):
            fast = fast.next

        # If there is only 1 node left then delete
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next

        return head
    
    def listNodeToList(self, head):
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        return output
        
s = Solution()

# Case 1
head =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linked_list_output = s.removeNthFromEnd(head, 2)
output = s.listNodeToList(linked_list_output)
expected = [1,2,3,5]
print(f"Result: {output}, Expected: {expected}")
# assert output == expected

# Case 2
head =  ListNode(1)
linked_list_output = s.removeNthFromEnd(head, 1)
output = s.listNodeToList(linked_list_output)
expected = []
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 3
head =  ListNode(1, ListNode(2))
linked_list_output = s.removeNthFromEnd(head, 1)
output = s.listNodeToList(linked_list_output)
expected = [1]
print(f"Result: {output}, Expected: {expected}")
assert output == expected