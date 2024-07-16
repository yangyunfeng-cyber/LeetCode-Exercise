# leetcode 142 https://leetcode.cn/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 快慢指针法
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head # 定义slow指针为头结点指针
        fast = head # 定义fast指针为头结点指针

        while fast and fast.next:
            slow = slow.next  # slow指针每步走一个结点
            fast = fast.next.next  # fast指针每步走两个结点   

            # 如果存在环，则fast指针和slow指针最终会相遇
            if slow == fast:
                # 将slow指针返回到链表的开始位置
                slow = head
                # 通过下面的代码找到环的入口
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        # 如果没环，返回None
        return None 
        
