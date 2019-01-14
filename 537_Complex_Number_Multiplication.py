class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        real_a, img_a = a.split('+')
        real_a = int(real_a)
        img_a = int(img_a.rstrip('i'))
        real_b, img_b = b.split('+')
        real_b = int(real_b)
        img_b = int(img_b.rstrip('i'))
        return str(real_a*real_b - img_a*img_b)+'+'+str(real_a*img_b + real_b*img_a)+'i'


a = '1+1i'
b = '1+1i'
a = '1+-1i'
b = '1+-1i'
res = Solution().complexNumberMultiply(a,b)
print(res)
