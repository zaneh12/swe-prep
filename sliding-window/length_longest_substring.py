class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring
        without repeating characters.

        Uses a sliding window approach with a set to track unique characters.

        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is the size of the character set
        """
        curstr = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in curstr:
                curstr.remove(s[l])
                l += 1

            curstr.add(s[r])
            res = max(res, len(curstr))
            r += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))     # Output: 3
