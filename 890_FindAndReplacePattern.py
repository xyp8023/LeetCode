class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def unique(it):
            s = set()
            for x in it:
                if x not in s:
                    s.add(x)
                    yield x

        def wordToPattern(word):
            rWord = ''
            pattern_dict = dict()
            pattern_set = ''.join(unique(word))
            for letter in pattern_set:
                if letter not in pattern_dict:
                    pattern_dict[letter] = pattern_set.index(letter)
            for letter in word:
                rWord += str(pattern_dict[letter])
            return rWord

        rWordMatchPattern = list()
        rPattern = wordToPattern(pattern)
        for word in words:
            rWord = wordToPattern(word)
            if rWord == rPattern:
                rWordMatchPattern.append(word)
        return rWordMatchPattern


#
# class Solution(object):
#     def findAndReplacePattern(self, words, pattern):
#         """
#         :type words: List[str]
#         :type pattern: str
#         :rtype: List[str]
#         """
#         perm = self.create_pattern(pattern)
#         res = []
#         for each in words:
#             if self.create_pattern(each) == perm:
#                 res.append(each)
#         return res
#
#     def create_pattern(self, pattern):
#         ctr = 0
#         pat_dict = dict()
#         pat_list = list()
#         for i in pattern:
#             if i not in pat_dict:
#                 pat_dict[i] = ctr
#                 pat_list.append(pat_dict[i])
#             else:
#                 pat_list.append(pat_dict[i])
#             ctr += 1
#         return pat_list


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
sol = Solution()
res = sol.findAndReplacePattern(words, pattern)
print(res)
