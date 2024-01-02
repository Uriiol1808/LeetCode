"""
2096. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, 
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from 
the start using 0-based indexing, where ⌊x⌋ denotes the largest integer 
less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, 
respectively.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        
        slow_ptr = head
        fast_ptr = head
        prev_str = None

        while fast_ptr and fast_ptr.next:
            prev_str = slow_ptr
            # One step at a time
            slow_ptr = slow_ptr.next
            # Two steps at a time
            fast_ptr = fast_ptr.next.next

        # Delete the middle one
        if prev_str:
            prev_str.next = slow_ptr.next
        else:
            head = head.next

        return head

    def listNodeToList(self, head):
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        return output

s = Solution()

# Case 1
head =  ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
reverse_head1 = s.deleteMiddle(head)
reversed_list1 = s.listNodeToList(reverse_head1)
expected1 = [1,3,4,1,2,6]
print(f"Result: {reversed_list1}, Expected: {expected1}")
assert reversed_list1 == expected1

# Case 2
head2 =  ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reverse_head2 = s.deleteMiddle(head2)
reversed_list2 = s.listNodeToList(reverse_head2)
expected2 = [1,2,4]
print(f"Result: {reversed_list2}, Expected: {expected2}")
assert reversed_list2 == expected2

# Case 3
head3 =  ListNode(2, ListNode(1))
reverse_head3 = s.deleteMiddle(head3)
reversed_list3 = s.listNodeToList(reverse_head3)
expected3 = [2]
print(f"Result: {reversed_list3}, Expected: {expected3}")
assert reversed_list3 == expected3