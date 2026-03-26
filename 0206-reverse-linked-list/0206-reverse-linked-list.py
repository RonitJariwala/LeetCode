# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        temp=head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    ''' Recursive based O(N) with O(N) stack space
    def reverseListR(self,head):
        if head is None or head.next is None:
            return head
        newHead=self.reverseListR(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead
    '''

        