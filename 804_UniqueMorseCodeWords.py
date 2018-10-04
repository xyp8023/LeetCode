# class Solution:
    # def uniqueMorseRepresentations(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: int
    #     """
    #     MorseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
    #                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    #     res = []
    #     ascii_a = ord('a') # 97
    #     for i in words:
    #         Str = ''
    #         for j in i:
    #             Str += MorseCode[ord(j) - ascii_a]
    #         res.append(Str)
    #     return len(set(res))

# another solution
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MorseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                     "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        ascii_a = ord('a')  # 97
        seen = {''.join(MorseCode[ord(c)-ascii_a] for c in word) for word in words}
        return len(seen)


words = ["gin", "zen", "gig", "msg"]
sol = Solution()
res = sol.uniqueMorseRepresentations(words)
print(res)