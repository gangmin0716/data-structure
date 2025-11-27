# BFS.py 파일에서 BFS_dict 함수를 import
from BFS import BFS_dict

# FastBus.py 파일에서 city_transport_network 그래프를 import
from FastBus import city_transport_network

# 1. 탐색을 시작할 출발 정류장 정의
start_station = '우리집'

print("--- BFS (너비 우선 탐색)을 이용한 대중교통 네트워크 탐색 ---")

# 2. BFS_dict 함수를 사용하여 그래프 탐색 실행
# BFS는 '우리집'에서 가까운 정류장(최소 환승/경유) 순서로 탐색합니다.
print(f'BFS 탐색 순서 (출발: {start_station}): ', end='')
BFS_dict(city_transport_network, start_station)
print()
