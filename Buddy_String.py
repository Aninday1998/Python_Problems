


class Solution:
    def buddyStrings(self, s: str, goal: str):

        if s[::-1] in goal[::]:
            return "true"
        else:
            return "false"

s = Solution()
x = s.buddyStrings("ab", "ab")
print(x)