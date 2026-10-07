class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        base = range(len(nums) + 1)
        for i in base:
            if i not in nums:
                return i
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna