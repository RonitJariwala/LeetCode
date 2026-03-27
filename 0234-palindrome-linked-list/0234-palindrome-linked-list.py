# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return True
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        newHead=self.reverseLL(slow.next)
        first=head
        second=newHead
        while second is not None:
            if first.val!=second.val:
                newHead=self.reverseLL(newHead)
                return False
            first=first.next
            second=second.next
        newHead=self.reverseLL(newHead)
        return True