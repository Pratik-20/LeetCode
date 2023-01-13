"""
19. Remove Nth Node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:

1->2->3->4->5
1->2->3->->5

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 """


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        if (head == None or head.next == None and n == 1):
            return None

        temp = head
        while (temp != None and temp.next != None):
            temp = temp.next
            count += 1
        k = count - n

        if k < 0:
            head = head.next
            return head
        slow = head
        for i in range(0, k):
            slow = slow.next
        slow.next = slow.next.next
        return head
