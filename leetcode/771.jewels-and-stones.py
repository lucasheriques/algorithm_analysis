#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        number_jewels = 0

        for char in S:
            if char in jewels:
                number_jewels += 1

        return number_jewels

        # return (1 if char in jewels else 0 for char in jewels) # oneline solution

# @lc code=end
