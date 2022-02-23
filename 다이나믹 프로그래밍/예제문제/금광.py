## 금광
"""
n × m크기의 금광이 있다.
금광은 1 × 1크기의 칸으로 나누어져 있으며,각 칸은 특정한 크기의 금이 들어 있다
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다.
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
이후에 m - 1번에 걸쳐서 매번 오른쪽 위,오른쪽,오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라

1   3   3   2
2*  1   4   1
0   6*  4*  7*
=> 2 + 6 + 4 + 7 = 19
"""

# 아이디어
# 금광에서 고려해야할 위치
# 1) 왼쪽 위에서 오는 경우
# 2) 왼쪽에서 오는 경우
# 3) 왼쪽 아래에서 오는 경우
# 위 3가지 경우에 대해 가장 많은 금을 가지고 있는 경우를 업데이트

# dp[i][j] : i행 j열에서 얻을 수 있는 금의 최대 크기
# array[i][j]: i행 j열에 있는 금의 크기
# 점화식: dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

# 주의할 점

import numpy as np

def solution(n, m, array):
    array = np.array(array)
    array = array.reshape(n, m)
    dp = array

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽
            left = dp[i][j - 1]
            # 왼쪽 아래
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            dp[i][j] = array[i][j] + max(left_up, left, left_down)

    # 금 크기 최대 합 구하기
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    return result


if __name__ == '__main__':
    print(solution(3, 4, [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7])) # 19
    print(solution(4, 4, [1, 3, 1, 5, 2, 2, 4, 1, 5, 0, 2, 3, 0, 6, 1, 2])) # 16