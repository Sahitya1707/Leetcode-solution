class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute-force solution (commented out) is O(n^2), slow for large arrays
        # n = len(nums)
        # output = []
        # result = 1
        # for i, num in enumerate(nums):
        #     j = 0
        #     while j < len(nums):
        #         if i == j:
        #             j += 1
        #         else:
        #             result *= nums[j]
        #             j += 1
        #     output.append(result)
        #     result = 1
        # return output

        n = len(nums)
        output = [1] * n  # Initialize output array with 1s

        # -------------------------
        # Step 1: Prefix pass
        # Compute product of all numbers BEFORE index i
        # output[i] will temporarily store this prefix product
        # -------------------------
        prefix = 1
        for i in range(n):
            output[i] = prefix      # store product of elements before i
            prefix *= nums[i]       # update prefix for next iteration

        # -------------------------
        # Step 2: Suffix pass
        # Compute product of all numbers AFTER index i
        # Multiply it with the prefix stored in output[i]
        # -------------------------
        suffix = 1
        for i in range(n-1, -1, -1):  # iterate from right to left
            output[i] *= suffix       # multiply by product of elements after i
            suffix *= nums[i]         # update suffix for next iteration

        # -------------------------
        # output[i] now contains product of all elements except nums[i]
        # -------------------------
        return output
