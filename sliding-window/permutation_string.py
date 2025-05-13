from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer, no permutation is possible
        if len(s1) > len(s2):
            return False

        # Initialize frequency counters for s1 and the sliding window in s2
        check = [0] * 26  # frequency of characters in s1
        window = [0] * 26 # frequency of current window in s2

        for c in s1:
            check[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            window[ord(c) - ord('a')] += 1

        # Initial comparison
        if check == window:
            return True

        # Slide the window through s2
        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord('a')] += 1                          # add new char
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1                # remove old char
            if check == window:
                return True

        return False

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))  # True: "ba" is in s2
    print(sol.checkInclusion("ab", "eidboaoo"))  # False: no permutation of "ab"
    print(sol.checkInclusion("adc", "dcda"))     # True: "dca"
    print(sol.checkInclusion("hello", "ooolleoooleh"))  # False
    print(sol.checkInclusion("a", "a"))          # True
    print(sol.checkInclusion("a", "b"))          # False
