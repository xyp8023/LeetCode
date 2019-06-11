class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)
        r_deck = [deck[-1]]
        for i in range(len(deck)-2,-1,-1):
            r_deck.insert(0, r_deck.pop())
            r_deck.insert(0, deck[i])
            # r_deck = [deck[i]] + r_deck

        return r_deck


deck = [17, 13, 11, 2, 3, 5, 7]
sol = Solution()
res = sol.deckRevealedIncreasing(deck)
print(res)