from circular_queue import *

def main():
    # 카드의 개수 N을 입력받음
    N = int(input())

    # circular_queue.py에 정의된 큐 생성
    q = CircularQueue()

    # 1번부터 N번까지의 카드를 순서대로 큐에 삽입
    for i in range(1, N + 1):
        q.enqueue(i)

    # 버려진 카드들을 저장할 리스트
    discarded = []

    # 카드가 한 장 남을 때까지 반복
    while q.size() > 1:
        # 제일 위의 카드를 버림 (큐의 front 원소 제거)
        discarded.append(q.dequeue())

        # 다음 제일 위의 카드를 맨 아래로 이동
        # 즉, front에서 꺼내서 rear에 다시 삽입
        q.enqueue(q.dequeue())

    # 남은 한 장의 카드를 출력해야 하므로 마지막 dequeue 실행
    last_card = q.dequeue()

    # 버린 카드들과 마지막 남은 카드를 순서대로 출력
    # 예: 1 3 2 4
    print(*discarded, last_card)

# 프로그램 실행 시작점
if __name__ == "__main__":
    main()
