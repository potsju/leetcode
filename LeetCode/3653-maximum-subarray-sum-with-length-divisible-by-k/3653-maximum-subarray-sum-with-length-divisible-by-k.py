class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        best = float('-inf')

        # Stores the smallest prefix sum for each index % k
        best_prefix = {0: 0}  # prefix before starting at index -1

        for i, num in enumerate(nums):
            prefix += num
            r = (i + 1) % k  # length (i - j + 1) divisible by k → compare by index mod k

            if r in best_prefix:
                best = max(best, prefix - best_prefix[r])

            # store the minimum prefix sum for this remainder
            if r not in best_prefix:
                best_prefix[r] = prefix
            else:
                best_prefix[r] = min(best_prefix[r], prefix)

        return best
