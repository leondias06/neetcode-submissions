class Solution:
    def isPalindrome(self, s: str) -> bool:

        normalS = ""

        for char in s:
            if char.isalnum():
                normalS += char.lower()

        reversedS = normalS[::-1]

        return reversedS == normalS