class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = set()
        for i in nums:
            if i in a:
                return True
            a.add(i)
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna