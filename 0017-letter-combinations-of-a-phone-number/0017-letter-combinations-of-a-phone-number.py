class Solution:
    def letterCombinations(self, digits: str):

        # If input is empty, return empty list
        if not digits:
            return []

        # Phone keypad mapping
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        # Backtracking function
        def backtrack(index, path):

            # Base case:
            # If we've used all digits, store the current combination
            if index == len(digits):
                ans.append(path)
                return

            # Get letters for the current digit
            letters = phone[digits[index]]

            # Try every possible letter
            for ch in letters:
                # Move to the next digit
                backtrack(index + 1, path + ch)

        # Start from index 0 with an empty string
        backtrack(0, "")

        return ans