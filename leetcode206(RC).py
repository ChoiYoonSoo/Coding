# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 링크드리스트 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        def recur(curr,prev):
            if curr != None:
                next,curr.next = curr.next,prev
                return recur(next,curr)
            else:
                return prev

        return recur(head,prev)