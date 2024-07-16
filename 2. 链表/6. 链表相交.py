# leetcode 160   https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dis = self.getLength(headA) - self.getLength(headB)

        # 通过移动较长的链表， 使两链表长度相等
        if dis >0:
            headA = self.moveForward(headA, dis)
        else:
            headB = self.moveForward(headB, abs(dis))
        
        # 将两个头向前移动， 直到它们相交
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLength(self, head:ListNode):
        length = 0
        while head:
            length +=1
            head = head.next
        return length

    def moveForward(self, head:ListNode, steps:int):
        while steps > 0:
            head = head.next
            steps -= 1
        return head

        
