## Largest Number
"""
link: https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
"""

# 아이디어
# 문자열로 변경하여 정렬
# 정렬 기준: 두 숫자를 앞뒤로 붙인 것 중에 더 큰것 기준

# functools의 cmp_to_key: key 매개변수에 함수(func)를 전달할 때 사용하는 함수
# 크다 (양수 리턴)
# 작다 (음수 리턴)
# 같다 (0 리턴)

# 주의할 점
# 0으로 시작할 경우 0 제거해줌

from typing import *
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key = cmp_to_key(lambda x,y: ((x+y)>(y+x)) - ((x+y)<(y+x)) ), reverse=True)
        result = ''.join(nums)

        return '0' if result[0] == '0' else result

if __name__ == '__main__':
    sol = Solution()

    print(sol.largestNumber([3, 30, 34, 5, 9]))
    print(sol.largestNumber([0, 0]))
