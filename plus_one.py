class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        r = 1
        size = len(digits)
        i = size - 1
        while i >= 0 or r:
            sum = digits[i] + r
            if i >= 0:
                digits[i] = sum % 10
            else:
                digits.insert(0, sum % 10)
            r = sum / 10
            i -= 1
        return digits


if __name__ == '__main__':
    x = [9, 9, 9]
    # x = [1, 0, 0]
    solution = Solution()
    print solution.plusOne(x)
