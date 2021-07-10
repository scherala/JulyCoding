# Link to question: https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Variable to store result and initialize it to zero
        result = 0
        current_length = 0
        for num in nums:
            if(num == 1):
                current_length += 1
            else:
                result = max(current_length, result)
                current_length = 0
        return max(current_length, result)
