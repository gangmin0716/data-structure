# 딕셔너리(인접 리스트) 기반 너비 우선 탐색(BFS)
from queue import Queue     # queue 모듈에서 Queue 사용

def BFS_dict(graph, start):
    visited = set()         # 방문한 정점을 저장하는 집합
    Q = Queue()             # 공백 큐 생성
    Q.put(start)            # 시작 정점을 큐에 삽입
    visited.add(start)      # 시작 정점 방문 표시

    while not Q.empty():
        u = Q.get()         # 큐에서 정점을 꺼냄
        print(u, end=' ')   # 정점을 출력(또는 처리)
        for v in graph[u]:  # u의 모든 인접 정점 v에 대해
            if v not in visited:     # 아직 방문하지 않았다면
                Q.put(v)             # 큐에 넣고
                visited.add(v)       # 방문 표시

# 그래프를 딕셔너리(인접 리스트)로 표현
graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'D', 'E'],
         'D': ['B', 'C', 'F'],
         'E': ['C', 'G', 'H'],
         'F': ['D'],
         'G': ['E', 'H'],
         'H': ['E', 'G']}

print('BFS_dict(출발:A): ', end='')
BFS_dict(graph, 'A')
print()