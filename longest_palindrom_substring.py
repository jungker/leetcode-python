class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1:
            return s
        maxLen = 1
        res = s[0]
        i = j = k = 0
        while i < size:
            if i > 0 and s[i] == s[i - 1]:
                j = i - 1
                k = i
            while j >= 0 and k < size and s[j] == s[k]:
                j -= 1
                k += 1
            t = k - j - 1
            if t > maxLen:
                maxLen = t
                res = s[j + 1:k]

            j = i - 1
            k = i + 1
            while j >= 0 and k < size and s[j] == s[k]:
                j -= 1
                k += 1
            t = k - j - 1
            if t > maxLen:
                maxLen = t
                res = s[j + 1:k]
            i += 1
        return res


if __name__ == '__main__':
    s = 'babcad'
    # s = 'bb'
    # s = 'ccc'
    # s = 'abcda'
    solution = Solution()
    print solution.longestPalindrome(s)
