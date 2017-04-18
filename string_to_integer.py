class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        size = len(str)
        if not size:
            return 0

        i = 0

        while str[i].isspace():
            i += 1

        sign = 1
        if str[i] in {'+', '-'}:
            sign = 1 if str[i] == '+' else 0
            i += 1

        if i == size:
            return 0

        res = 0
        while i < size and str[i].isdigit():
            res = res * 10 + (ord(str[i]) - ord('0'))
            i += 1
        if sign and res > 2147483647:
            return 2147483647
        elif not sign and res > 2147483648:
            return -2147483648
        return res if sign else -res


if __name__ == '__main__':
    solution = Solution()
    s = '-3924xekr324'
    s = '2147483648'
    print solution.myAtoi(s)
