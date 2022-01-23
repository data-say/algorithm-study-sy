## 미로탈출
"""
동빈이는 N × M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다
동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다
"""

# 아이디어
# BFS : 간선의 비용이 모두 같을 때 최단 거리를 구하는 문제에서 사용하는 알고리즘
# 시작지점의 가까운 노드부터 차례대로 모든 노드를 탐색하여 최단 거리 탐색
# (1, 1)부터 BFS 탐색 진행

from collections import deque
def solution(n, m, s):
    graph = []
    for i in range(n):
        graph.append(list(map(int, s[i])))

    # 상하좌우 방향 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        # 큐가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            # 상하좌우 4가지 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 공간 벗어난 경우, 괴물이 있는 경우 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                    continue
                # 미방문노드의 경우 최단 거리 기록 (현재 최단 거리 + 1)
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

        # 도착지 최단 거리 반환
        return graph[n - 1][m - 1]

    return bfs(0, 0)


if __name__ == '__main__':
    print(solution(5, 6,
                   ["101010",
                    "111111",
                    "000001",
                    "111111",
                    "111111"]))
