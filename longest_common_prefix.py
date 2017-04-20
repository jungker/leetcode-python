class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        minSize = min(len(i) for i in strs)
        while i < minSize:
            t = strs[0][i]
            for s in strs:
                if t != s[i]:
                    break
            else:
                i += 1
                continue
            break
        return strs[0][:i]

if __name__ == '__main__':
    strs = ['ddas', 'ddae', 'ddaevcxv', 'ddaenekww']
    solution = Solution()
    print solution.longestCommonPrefix(strs)
