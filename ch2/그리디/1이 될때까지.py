## 1이 될때까지
"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
1. N에서 1을 뺀다
2. N을 K로 나눈다
예를 들어 N이 17, K가 4라고 가정하면. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다.
이 후에 2번의 과정을 두 번 수행하면 N은 1이 된다.
결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다
이는 N을 1로 만드는 최소 횟수이다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하라
"""

# 아이디어: 2 이상의 수로 나누기를 많이 수행할수록 수행 횟수가 적음

# O(N)
def solution(n, k):
    count = 0

    while True:
        if n == 1:
            break

        if n % k == 0:
            n /= k
        else:
            n -= 1

        count += 1

    return count

# O(logN)
def solution2(n, k):
    count = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
        target = (n // k) * k
        count += (n - target)
        n = target

        # n이 k보다 작을 때 반복문 탈출
        if n < k:
            break

        # k로 나누기
        count += 1
        n /= k

    count += (n - 1)
    return int(count)

if __name__ == '__main__':
    print(solution(17, 4))
    print(solution(25, 3))
    print(solution(25, 5))

    print(solution2(17, 4))
    print(solution2(25, 3))
    print(solution2(25, 5))