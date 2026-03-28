# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDifference(self,head1,head2):
        len1,len2=0,0
        while head1 or head2:
            if head1:
                len1+=1
                head1=head1.next
            if head2:
                len2+=1
                head2=head2.next
        return len1-len2

    def getIntersectionNode(self, head1: ListNode, head2: ListNode) -> Optional[ListNode]:
        diff=self.getDifference(head1,head2)
        if diff<0:
            for _ in range(abs(diff)):
                head2=head2.next
        else:
            for _ in range(diff):
                head1=head1.next
        while head1:
            if head1==head2:
                return head1
            head1=head1.next
            head2=head2.next
        return None