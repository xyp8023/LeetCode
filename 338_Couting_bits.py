class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        rlist = []
        for i in range(num+1):
            rlist.append(bin(i).count('1'))
        return rlist


num = 2
num = 5
res = Solution().countBits(num)
print(res)
