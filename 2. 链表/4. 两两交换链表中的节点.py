# leetcode 24  https://leetcode.cn/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归法
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # 待翻转的两个node分别是pre和cur
        pre = head
        cur = head.next
        next = head.next.next

        cur.next = pre # 交换
        pre.next = self.swapPairs(next) # 将以next为head的后续链表两两交换

        return cur
