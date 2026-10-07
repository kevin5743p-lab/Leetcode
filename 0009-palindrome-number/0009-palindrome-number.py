class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''num = int()
        while x != 0:
            dig = x % 10
            x = x // 10'''
        num = str(x)
        num = list(num)
        b = num.copy()
        b.reverse()
        if num == b:
            return True
        return False



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna