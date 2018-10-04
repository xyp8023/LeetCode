class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ''
        # s_list = map(str,s.strip().split(' '))
        # for word in s_list:
        for word in s.split():
            res+=word[::-1]+' '
        res = res.strip()
        return res

        # another solution, one line python
        # return " ".join([word[::-1] for word in s.split()])


s = "Let's take LeetCode contest"
sol = Solution()
res = sol.reverseWords(s)
print(res)

