"""
Problem:    217. Contains Duplicate
Link:       https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Date:       2026-11-02

Idea:  Keep a set of numbers already seen; if the current number is already in it, there is a duplicate.
Time:  O(n) - one pass, set lookup and insert are O(1) on average
Space: O(n) - the set can hold every number
Solved without hints: yes
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
