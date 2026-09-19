class Solution:
    def countPrimeSetBits(self, left, right):
        count = 0

        for num in range(left, right + 1):

            # Count number of 1s in binary
            ones = bin(num).count('1')

            # Check if number of 1s is prime
            if ones > 1:
                is_prime = True

                for i in range(2, int(ones ** 0.5) + 1):
                    if ones % i == 0:
                        is_prime = False
                        break

                if is_prime:
                    count += 1

        return count