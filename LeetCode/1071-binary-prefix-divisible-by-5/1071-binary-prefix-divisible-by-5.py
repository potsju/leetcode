class Solution(object):
    def prefixesDivBy5(self, nums):
        result = []
        current = 0

        for digit in nums:
            # Update current prefix value mod 5
            current = (current * 2 + digit) % 5

            # Append whether divisible by 5
            result.append(current == 0)

        return result
