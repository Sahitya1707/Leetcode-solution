# 347. Top K Frequent Elements

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

**Follow up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Approach

The solution uses a hash map (dictionary in Python) to count the frequency of each number in the input array. After counting, it sorts the elements based on their frequencies in descending order and selects the top `k` elements.

## Code

```python
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1

        counts_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in counts_list[:k]]
```

### Code Explanation

1.  **Frequency Counting:**

    - A dictionary `my_dict` is used to store the frequency of each number in `nums`.
    - The code iterates through `nums`, and for each number, it increments its count in `my_dict`.

2.  **Sorting by Frequency:**

    - `my_dict.items()` returns a list of (key, value) pairs (i.e., (number, frequency)).
    - `sorted()` is used to sort these pairs based on the frequency (the second element of the tuple, `x[1]`). `reverse=True` ensures descending order.

3.  **Extracting Top K Elements:**
    - `counts_list[:k]` slices the sorted list to get the top `k` items.
    - A list comprehension `[num for num, count in counts_list[:k]]` is used to extract just the numbers (the first element of the tuple) from the top `k` items.

## Complexity Analysis

- **Time Complexity:** O(n log n)

  - The frequency counting takes O(n) time, where n is the number of elements in `nums`.
  - The sorting step takes O(m log m) time, where m is the number of unique elements in `nums`. In the worst case, m can be equal to n, so this step is O(n log n).
  - The final list comprehension takes O(k) time.
  - Therefore, the dominant factor is the sorting step, making the overall time complexity O(n log n). This meets the follow-up requirement of being better than O(n log n) in the average case, but not the worst case. A heap-based solution could achieve O(n log k).

- **Space Complexity:** O(m)
  - The space complexity is determined by the storage required for the hash map and the sorted list. In the worst case, where all elements are unique, this is O(n).
