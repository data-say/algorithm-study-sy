## 효율적인 화폐구성
"""
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 각 종류의 화폐는 몇 개라도 사용할 수 있다
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다
M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하라

조건
1 <= n <= 100, 1 <= m <= 10,000

출력
최소 화폐 개수 출력
불가능할 때는 -1 출력
"""

# 아이디어
# 먼저 해당 문제가 다이나믹 프로그래밍을 이용하는 문제인 이유
# 1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다
#   - 각 i의 최적의 해 a_i를 구하는 문제로 풀 수 있다
# 2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결한다
#   - a_i 최적의 해를 m까지 계속해서 구해가는 방식으로 반복해서 풀 수 있다

# a_i: 금액 i를 만들기 위한 최소 화폐 개수
# k: 화폐의 단위
# 점화식
# - a_(i-k)를 만들 수 있는 경우 a_i = min(a_i, a_(i-k) + 1)
# - a_(i-k)를 만들 수 없는 경우 a_i = INF

# 주의할 점
# dp 테이블을 화폐 단위 종류수 만큼 반복해서 갱신해나가기
# 이때 화폐 단위 종류 ~ m 까지 반복

def solution(n, m, k):
    # DP 테이블 초기화
    INF = 10001 # 특정 금액을 만들기 위한 화폐 구성 불가능 의미
    dp = [INF] * (m + 1)

    # Bottom-up DP
    dp[0] = 0
    for i in range(n):
        for j in range(k[i], m + 1):
            # a_(i-k)를 만들 수 있는 경우
            if dp[j - k[i]] != INF:
                dp[j] = min(dp[j], dp[j - k[i]] + 1)

    return -1 if dp[m] == INF else dp[m]


if __name__ == '__main__':
    print(solution(2, 15, [2, 3])) # 5
    print(solution(3, 4, [3, 5, 7])) # -1