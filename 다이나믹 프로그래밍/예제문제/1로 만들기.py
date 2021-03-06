## 1로 만들기
"""
정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다
1) X가 5로 나누어 떨어지면, 5로 나눈다
2) X가 3으로 나누어 떨어지면, 3으로 나눈다
3) X가 2로 나누어 떨어지면, 2로 나눈다
4) X에서 1을 뺀다

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 한다.
연산을 사용하는 횟수의 최솟값을 출력하라.

예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다
26 → 25 → 5 → 1

조건
1 <= x <= 30,000
"""

# 아이디어
# 먼저 해당 문제가 다이나믹 프로그래밍을 이용하는 문제인 이유
# 1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다
#   - 각 i의 최적의 해 a_i를 구하는 문제로 풀 수 있다
# 2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결한다
#   - a_i 최적의 해를 1부터 x까지 계속해서 구해가는 방식으로 반복해서 풀 수 있다

# a_i: i를 1로 만들기 위한 최소 연산 수
# 점화식: a_i = min(a_(i/5), a_(i/3), a_(i/2), a_(i-1))

# 주의할 점
# x의 조건이 1부터 30000까지이므로 0번째 인덱스를 비워둠
# 각 4가지 경우의 수의 최솟값을 구할 때 나누기의 경우 조건을 확인해야 함
# 1을 빼는 것은 조건을 확인하지 않아도 되므로 해당 계산을 먼저 진행하고, 그 값과 조건에 만족했을 때 나눈 값을 비교함

def solution(x):
    # DP 테이블 초기화
    dp = [0] * (x + 1)

    # Bottom-up DP
    for i in range(2, x + 1):
        # 4번 경우의 수 (x - 1)
        dp[i] = dp[i-1] + 1
        # 1번 조건 (x가 5로 나누어 떨어지면)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
        # 2번 조건 (x가 3으로 나누어 떨어지면)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        # 3번 조건 (x가 2로 나누어 떨어지면)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    return dp[x]


if __name__ == '__main__':
    print(solution(26)) # 3