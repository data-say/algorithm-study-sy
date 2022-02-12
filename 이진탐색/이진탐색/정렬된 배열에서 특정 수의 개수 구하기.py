## 정렬된 배열에서 특정 수의 개수 구하기
"""
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
이때 이 수열에서 x가 등장하는 횟수를 계산하라.
예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면,
현재 수열에서 값이 2인 원소가 4개이므로 4를 출력한다
단, 이 문제는 시간 복잡도 O(logN) 으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다
"""

# 아이디어
# 이진탐색 bisect 라이브러리 사용

# 주의할 점
# x 값이 없으면 -1 출력

import bisect

def solution(n, x, array):
    left_idx = bisect.bisect_left(array, x)
    right_idx = bisect.bisect_right(array, x)
    return right_idx - left_idx if right_idx - left_idx != 0 else -1


if __name__ == '__main__':
    print(solution(7, 2, [1, 1, 2, 2, 2, 2, 3]))
    print(solution(7, 4, [1, 1, 2, 2, 2, 2, 3]))