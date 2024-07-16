# leetcode 19  https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)

        # 创建两个指针， 慢指针和快指针，并将它们初始化为虚拟节点
        slow = fast = dummy_head

        # 快指针比慢指针快n+1步
        for i in range(n+1):
            fast = fast.next
        
        # 移动两个指针，直到快指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 通过更新第（n-1)个节点的next指针删除第n个节点
        slow.next = slow.next.next

        return dummy_head.next
