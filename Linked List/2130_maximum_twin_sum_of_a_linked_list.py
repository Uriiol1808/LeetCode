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
        
        twin_dict = {}
        max_twin_sum = float()
        current = head
        n = 0+1

        while current:
            twin_index = n - (n // 2) - 1
            twin_val = twin_dict.get(twin_index, 0)

            twin_sum = current.val + twin_val
            max_twin_sum = max(max_twin_sum, twin_sum)

            twin_dict[n] = current.val + twin_val
            current = current.next
            n += 1

        return max_twin_sum
                
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

        