class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or not s:
            return s

        test = True
        s_array = list(s)

        while test:
            if s_array[::-1] == s_array:
                test = False
                return "".join(s_array)
            else:
                s_array.pop()
                s_array.pop(0)



sol = Solution()
print(sol.longestPalindrome('Enter String to be checked here'))

# Time complextitiy if 0(n) due to conecatation of string (Using methods .join and list())