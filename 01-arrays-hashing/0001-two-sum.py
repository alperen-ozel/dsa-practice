"""
Problem:    1. Two Sum
Link:       https://leetcode.com/problems/two-sum/
Difficulty: Easy
Date:       2026-11-02

Idea:  Brute force: try every pair (i, j) with j > i and return the first pair that adds up to target.
Time:  O(n^2) - two nested loops over the list
Space: O(1)
Solved without hints: mostly - needed a hint for setting up the nested loops
Next:  solve it again in O(n) with a hash map
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
