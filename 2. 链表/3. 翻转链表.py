# leetcode 206  https://leetcode.cn/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
考点：递归，链表
递归终止条件：当前节点为空
递归函数内：判断递归是否应该终止，保存当前节点的下一个节点，将当前节点的下一个指针指向前一个节点
            使用self.reverse(temp, cur)调用递归函数，反转当前节点与下一个节点
递归函数外：使用self.reverse(head,None)开始调用递归函数
"""


# 递归法, 更加节省运行时间
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 调用递归函数 reverse 开始反转链表
        return self.reverse(head, None)
    
    def reverse(self, cur: ListNode, pre: ListNode) -> ListNode:
        # 递归终止条件：当前节点为空，说明链表已经反转完毕
        if cur is None:
            return pre
        
        # 保存当前节点的下一个节点
        temp = cur.next
        
        # 将当前节点的下一个指针指向前一个节点
        cur.next = pre
        
        # 递归反转剩下的链表，并将当前节点作为前一个节点传入
        return self.reverse(temp, cur)
