## 떡볶이 떡 만들기
"""
오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다.
동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다.
대신에 한봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다
절단기에 높이(H) 를 지정하면 줄지어진 떡을 한 번에 절단한다.
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다
예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤
떡의 높이는 15, 14, 10, 15cm가 될 것이다.
잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다.
손님은 6cm만큼의 길이를 가져간다

손님이 왔을 때 요청한 총 길이가 M일 때
적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요
"""

# 아이디어
# 절단기 높이의 가능 범위: 0 ~ 떡의 최대길이
# 떡의 최대길이부터 시작해서 얻은 떡의 길이가 주어진 길이 이상인지 확인하기
# >> 시간 초과 예상

# def solution(n, m, array):
#     heights = list(range(max(array), 0, -1))
#
#     for height in heights:
#         result = 0
#         for i in array:
#             result += max(0, i - height)
#         if result >= m:
#             break
#
#     return height

# 아이디어2
# 절단기 높이의 가능 범위: 0 ~ 10억
# 범위가 넓을 때에는 이진 탐색을 통해 범위를 줄여나가야 함
# 적절한 높이를 찾을 때까지 이진 탐색을 진행해 범위를 줄여나가면서 조정
# 탐색 범위를 줄여나가며 얻은 떡이 길이 값이 주어진 조건에 만족할 때마다 저장

def solution(n, m, array):
    start = 0
    end = max(array)

    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        # 남은 떡 길이 계산
        for i in array:
            total += max(0, i - mid)

        # 떡 길이 부족한 경우 (왼쪽 탐색)
        if total < m:
            end = mid - 1
        # 떡 길이 충분한 경우 (오른쪽 탐색)
        else:
            result = mid # 결과 저장
            start = mid + 1

    return result

if __name__ == '__main__':
    print(solution(4, 6, [19, 15, 10, 17]))