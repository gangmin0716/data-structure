import heapq

def find_fastest_route(subway_map, departure_station, destination_station):
    shortest_times = {station: float('inf') for station in subway_map}
    shortest_times[departure_station] = 0
    
    stations_to_visit = []
    heapq.heappush(stations_to_visit, (0, departure_station)) # (시간, 정류장)
    
    route_history = {station: None for station in subway_map}

    while stations_to_visit:
        current_time, current_station = heapq.heappop(stations_to_visit) # 큐에서 누적시간이 가장 짧은 정류장 꺼내기

        if current_time > shortest_times[current_station]:
            continue

        if current_station == destination_station: # 목적지 도착 시 반복 멈춤
            break

        for next_station, travel_time in subway_map[current_station].items(): # 꺼낸 정류장과 연결된 다른 정류장 탐색
            new_route_time = current_time + travel_time # 다른 정류장까지 가는 시간 ( 현재 누적시간 + 이동시간 ) 계산

            if new_route_time < shortest_times[next_station]:
                shortest_times[next_station] = new_route_time
                route_history[next_station] = current_station
                heapq.heappush(stations_to_visit, (new_route_time, next_station))

    path = []
    current_stop = destination_station
    
    if shortest_times[destination_station] == float('inf'):
        return None, float('inf')

    while current_stop is not None:
        path.append(current_stop)
        current_stop = route_history[current_stop]
    
    path.reverse()
    
    return path, shortest_times[destination_station]

city_transport_network = {
    '우리집': {'A정류장': 20, 'B정류장': 50, 'C정류장': 5},
    'A정류장': {'학교': 10},
    'B정류장': {'학교': 10},
    'C정류장': {'학교': 10},
    '학교': {}
}
# 대중교통 정보를 담은 그래프 생성

route, total_minutes = find_fastest_route(city_transport_network, '우리집', '학교')

print(f"최적 경로: {' -> '.join(route)}")
print(f"총 소요 시간: {total_minutes}분")