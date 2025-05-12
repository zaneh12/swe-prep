class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k, return the length of the longest substring 
        containing the same letter you can get after performing at most k character replacements.
        """
        count = {}  # Dictionary to store frequency of characters in the current window
        res = 0
        l = 0  # Left pointer of the window

        for r in range(len(s)):  # Right pointer of the window
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if we need to shrink the window
            # (r - l + 1) is the window size
            # max(count.values()) is the count of the most frequent character in the window
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # Update result with the current valid window size
            res = max(res, r - l + 1)

        return res
