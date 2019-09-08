from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        inputs = []
        rt_string = ""
        for i in range(n):
            inputs.append(str(i+1))
        a = permutations(inputs, n)
        for i in list(a)[k-1]:
            rt_string += i
        return rt_string


sol = Solution()
rt_string = sol.getPermutation(4,9)
print(rt_string)