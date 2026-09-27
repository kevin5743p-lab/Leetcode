class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_diff = 0
        low = prices[0]
        for i in prices:
            diff = i - low
            if i < low:
                low = i 
            if diff > max_diff:
                max_diff = diff

        return max_diff


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna