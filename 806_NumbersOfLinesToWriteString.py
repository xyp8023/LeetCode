class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        ord_a = ord('a')
        units_left = 100
        lines_number=1
        for string in S:
            i = ord(string)-ord_a
            if units_left-widths[i]<0:
                lines_number+=1
                units_left=100
            units_left -= widths[i]
        return [lines_number, 100-units_left]


widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# S = "bbbcccdddaaa"
sol = Solution()
res = sol.numberOfLines(widths,S)
print(res)