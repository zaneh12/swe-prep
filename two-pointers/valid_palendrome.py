class Solution:
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    """
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            
            right -=1
            left +=1
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(s = "Was it a car or a cat I saw?"))
    print(sol.isPalindrome(s = "tab a cat"))
    