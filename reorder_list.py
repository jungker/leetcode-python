# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printListNode(p):
    while p:
        print p.val,
        p = p.next
    print


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        res = ListNode(0)
        res.next = head

        cnt = 0
        p = head
        while p:
            p = p.next
            cnt += 1
        cnt /= 2
        p = head
        for i in range(cnt):
            p = p.next

        t = ListNode(0)
        t.next, q = p, p.next
        while q:
            tt = q
            q = q.next
            tt.next = t.next
            t.next = tt
        p.next = None

        p, q = head, t.next
        t = res
        for i in range(cnt):
            t.next = p
            t = t.next
            p = p.next
            t.next = q
            t = t.next
            q = q.next
        if q:
            t.next = q


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    printListNode(head)
    solution.reorderList(head)
    printListNode(head)
