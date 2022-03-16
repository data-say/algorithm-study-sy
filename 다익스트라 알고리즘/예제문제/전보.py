## 전보
"""
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를
보내서 다른 도시로 해당 메시지를 전송할 수 있다
하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다
또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다
어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는
총 몇 개이며 도시들이 모두 메시지를 받는 데 까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하라

조건
1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= n
1 <= X, Y <= N, 1 <= Z <= 1,000

출력
도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 결리는 시간
"""

# 아이디어
# 최단 거리 문제
# n, m이 크므로 우선순위 큐를 사용한 다익스트라 방법 사용

# 주의할 점
# 총 걸리는 시간은 가장 오래 걸리는 시간

import heapq

def solution(n, m, c, lst):
    # 무한대
    INF = int(1e9) # 10억

    # 노드 정보 담는 리스트 생성
    graph = [[] for _ in range(n + 1)]

    # 최단 거리 테이블을 모두 무한대로 초기화
    distance = [INF] * (n + 1)

    # 간선 정보
    for i in range(m):
        x, y, z = lst[i][0], lst[i][1], lst[i][2]
        graph[x].append((y, z))

    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q: # 큐가 비어있지 않다면
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드 확인
            for adj in graph[now]:
                cost = dist + adj[1]
                if cost < distance[adj[0]]:
                    distance[adj[0]] = cost
                    heapq.heappush(q, (cost, adj[0]))

    dijkstra(c)

    # 도달할 수 있는 노드의 개수
    final_cnt = 0
    # 도달할 수 있는 노드 중, 가장 멀리 있는 노드와의 최단 거리
    max_distance = 0
    for d in distance:
        # 도달할 수 있는 노드인 경우우
       if d != INF:
            final_cnt += 1
            max_distance = max(max_distance, d)

    # 시작 노드 제외해야 하므로 final_cnt - 1 반환
    return final_cnt - 1, max_distance


if __name__ == '__main__':
    print(solution(3, 2, 1, [[1, 2, 4], [1, 3, 2]])) # 2 4