class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        r = 0
        res = []
        while i >= 0 or j >= 0 or r:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            sum = x + y + r
            res.append(sum % 2)
            r = sum / 2
            i -= 1
            j -= 1
        res.reverse()
        return ''.join([str(i) for i in res])


if __name__ == '__main__':
    solution = Solution()
    a = '11'
    b = '11'
    print solution.addBinary(a, b)
