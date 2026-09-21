class Solution:
    def resultArray(self, nums, k):
        # dp[r] = number of subarrays ending at previous index
        # whose product % k == r
        dp = [0] * k

        # answer[r] = total number of subarrays
        # whose product % k == r
        answer = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray with only num
            remainder = num % k
            new_dp[remainder] += 1

            # Extend all previous subarrays
            for r in range(k):
                new_remainder = (r * remainder) % k
                new_dp[new_remainder] += dp[r]

            # Add current subarrays to the final answer
            for r in range(k):
                answer[r] += new_dp[r]

            dp = new_dp

        return answer