## 네트워크
"""
* 문제
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때
컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

* 제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.
"""

# 아이디어: BFS / DFS
# 방문하지 않았으면 방문처리
# 방문처리 안한 컴퓨터를 찾으면 새로운 네트워크로 개수 구함
# 사실 연결만 되어 있으면 네트워크를 구성할 수 있기 때문에 깊이를 구할 필요는 없음

# 1. 탐색을 위한 큐, 방문한 노드를 체크해 둘 리스트 생성
# 2. 탐색을 시작할 노드를 큐에 넣기 (탐색 시작 노드의 방문 표시 해두기)
# 3. 큐가 빌 때까지 반복문 수행
# 3-1. 큐의 앞에서부터 노드를 하나씩 꺼내기
# 3-2. 꺼낸 노드에 인접한 노드들을 방문하는 반복문 수행
# 3-2-1. 방문한 노드가 이전에 방문한 적이 없다면 큐에 넣기
# 3-2-2. 방문한 노드는 체크해두기

# BFS 풀이
from collections import deque

def solution(n, computers):

    def bfs(x):
        queue = deque()
        queue.append(x)
        while queue:
            q = queue.popleft()
            visited[q] = True
            # 인접노드 탐색
            for adj in range(n):
                if adj != q and computers[q][adj] == 1 and not visited[adj]:
                    queue.append(adj)

    result = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i)
            result += 1

    return result

# DFS 풀이
def solution2(n, computers):

    def dfs(x):
        visited[x] = True
        for adj in range(n):
            if adj != x and computers[x][adj] and not visited[adj]:
                dfs(adj)

    result = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            result += 1

    return result


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0],
                       [1, 1, 0],
                       [0, 0, 1]]))
    print(solution(3, [[1, 1, 0],
                       [1, 1, 1],
                       [0, 1, 1]]))
    print(solution2(3, [[1, 1, 0],
                        [1, 1, 0],
                        [0, 0, 1]]))
    print(solution2(3, [[1, 1, 0],
                        [1, 1, 1],
                        [0, 1, 1]]))
