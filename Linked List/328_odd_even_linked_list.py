"""
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with 
odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, 
and so on.

Note that the relative order inside both the even and odd groups
 should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and 
O(n) time complexity.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        odd_head = ListNode()
        even_head = ListNode()

        odd_ptr = odd_head
        even_ptr = even_head

        is_odd = True
        while head:
            if is_odd:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = head
                even_ptr = even_ptr.next

            # Each iteration changes to odd/even
            is_odd = not is_odd
            head = head.next
        
        even_ptr.next = None
        # Append even indices next to odd indices 
        odd_ptr.next = even_head.next

        return odd_head.next

    def listNodeToList(self, head):
        output = []
        while head is not None:
            output.append(head.val)
            head = head.next
        return output

s = Solution()

# Case 1
head =  ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reverse_head1 = s.oddEvenList(head)
reversed_list1 = s.listNodeToList(reverse_head1)
expected1 = [1,3,5,2,4]
print(f"Result: {reversed_list1}, Expected: {expected1}")
assert reversed_list1 == expected1

# Case 2
head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, 
        ListNode(4, ListNode(7)))))))
reverse_head2 = s.oddEvenList(head2)
reversed_list2 = s.listNodeToList(reverse_head2)
expected2 = [2,3,6,7,1,5,4]
print(f"Result: {reversed_list2}, Expected: {expected2}")
assert reversed_list2 == expected2


        