"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, 
and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
    def listNodeToList(self, head):
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        return output
        
s = Solution()

# Case 1
head =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reverse_head1 = s.reverseList(head)
reversed_list1 = s.listNodeToList(reverse_head1)
expected1 = [5,4,3,2,1]
print(f"Result: {reversed_list1}, Expected: {expected1}")
assert reversed_list1 == expected1

# Case 2
head2 = ListNode(1, ListNode(2))
reverse_head2 = s.reverseList(head2)
reversed_list2 = s.listNodeToList(reverse_head2)
expected2 = [2,1]
print(f"Result: {reversed_list2}, Expected: {expected2}")
assert reversed_list2 == expected2

# Case 3
head3 = None
reverse_head3 = s.reverseList(head3)
reversed_list3 = s.listNodeToList(reverse_head3)
expected3 = []
print(f"Result: {reversed_list3}, Expected: {expected3}")
assert reversed_list3 == expected3