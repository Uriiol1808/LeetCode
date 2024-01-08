"""
2310. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed)
of the linked list is known as the twin of the (n-1-i)th node,
if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 
1 is the twin of node 2. These are the only nodes with twins 
for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum 
twin sum of the linked list.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if not head or not head.next:
            return 0
        
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return res
                
s = Solution()

# Case 1
head =  ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
output = s.pairSum(head)
expected = 6
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 2
head =  ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
output = s.pairSum(head)
expected = 7
print(f"Result: {output}, Expected: {expected}")
assert output == expected

# Case 3
head =  ListNode(1, ListNode(100000))
output = s.pairSum(head)
expected = 100001
print(f"Result: {output}, Expected: {expected}")
assert output == expected

        