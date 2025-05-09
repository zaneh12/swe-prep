class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an of s, and false otherwise.
        """
        # Simple Solution using Counter but this is space of O(n) (length of the string)
        # return Counter(s) == Counter(t)

        # the O(1) space solution

        arr = [0]*26

        for i in s:
            arr[ord(i) - ord('a')] +=1        
        for j in t:
            arr[ord(j) - ord('a')] -=1
        
        return all(c == 0 for c in arr)
            

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))     # expected: True
print(sol.isAnagram("rat", "car"))             # expected: False
print(sol.isAnagram("a", "a"))                 # expected: True
print(sol.isAnagram("abc", "abcc"))            # expected: False
print(sol.isAnagram("aacc", "ccac"))           # expected: False


        