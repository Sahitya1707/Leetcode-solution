class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: one at the start, one at the end
        p1, p2 = 0, len(numbers) - 1  

        # Loop until the two pointers meet
        while p1 < p2:
            # Calculate the sum of the current pair
            total = numbers[p1] + numbers[p2]

            if total > target:
                # If sum is too large, move the right pointer left
                p2 -= 1
            elif total < target:
                # If sum is too small, move the left pointer right
                p1 += 1
            else:
                # If sum matches target, return 1-based indices
                return [p1 + 1, p2 + 1]

        # Problem guarantees one solution, so we don't need to handle "no solution"
