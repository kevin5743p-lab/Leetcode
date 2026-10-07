class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        return None

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna