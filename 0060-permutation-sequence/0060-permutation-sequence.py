class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [str(i) for i in range(1, n + 1)]

        # factorials
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # k is 1-indexed, convert to 0-indexed
        k -= 1

        ans = ""

        for i in range(n, 0, -1):

            # Number of permutations for each choice
            block = fact[i - 1]

            # Find which number should be selected
            index = k // block

            ans += nums[index]

            # Remove selected number
            nums.pop(index)

            # Remaining position inside the block
            k %= block

        return ans