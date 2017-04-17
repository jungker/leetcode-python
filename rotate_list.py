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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        cnt = 0
        while p:
            p = p.next
            cnt += 1
        k %= cnt
        if not k:
            return head
        p = head
        for i in range(cnt - k - 1):
            p = p.next
        q0 = q = p.next
        p.next = None
        while q.next:
            q = q.next
        q.next = head
        return q0


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    res = solution.rotateRight(head, 5)
    printListNode(res)
