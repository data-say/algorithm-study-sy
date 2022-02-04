## Sort Colors
"""
link: https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
"""

# 아이디어
# 문자열로 변경하여 정렬
# 정렬 기준: 두 숫자를 앞뒤로 붙인 것 중에 더 큰것 기준

# 주의할 점
# 기본 라이브러리 사용 금지

from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 계수 정렬
        i = j = k = 0
        for num in nums:
            if num == 0:
                i += 1
            elif num == 1:
                j += 1
            else:
                k += 1

        nums[:i] = [0] * i
        nums[i:i+j] = [1] * j
        nums[i+j:] = [2] * k


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)
