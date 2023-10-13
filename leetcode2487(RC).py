# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 링크드리스트 나보다 큰 수가 뒤에 있으면 삭제
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val: # head와 head.next가 존재하고 값을 비교해서 더 작으면 head노드는 제거해야 하기 때문에 head.next를 새로운 head로 설정
            return head.next
        return head
        