class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

        def insert(S, index):
            return S[:index] + '-'+ S[index:]

        S_without_dash = S.replace('-', '').upper()
        N = len(S_without_dash)
        if N <= K:
            return S_without_dash
        else:
            for i in range(N // K):
                index = N - K * (i + 1)
                S_without_dash = insert(S_without_dash, index)
            if N%K==0:
                S_without_dash = S_without_dash.lstrip('-')
            return S_without_dash


S = "----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo"
K = 99
S ="2-5g-3-J"
K=2
print(Solution().licenseKeyFormatting(S, K))
