#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        max_candies = max(candies)
        return [i + extra_candies >= max_candies for i in candies]
# @lc code=end
