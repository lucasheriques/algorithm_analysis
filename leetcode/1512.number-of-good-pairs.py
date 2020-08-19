#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_table = {}
        pairs = 0

        for n in nums:
            pairs += hash_table.get(n, 0)
            hash_table[n] = hash_table.get(n, 0) + 1

        return pairs

# @lc code=end
