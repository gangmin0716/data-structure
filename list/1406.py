from linkedList import LinkedList  # 업로드하신 파일 이름에 맞게 수정


def main():
    import sys
    input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

    # 초기 문자열 입력
    s = input().strip()  # 문자열을 입력받고 양쪽 공백 제거

    # 연결 리스트로 초기화
    # LinkedList를 사용하여 문자열의 각 문자를 노드로 저장
    # 이유: 삽입/삭제가 많은 편집기의 커서 이동 시 배열보다 효율적
    ll = LinkedList()
    for i, c in enumerate(s):
        ll.insert(i, c)  # i 위치에 문자 c 삽입

    # 커서 위치 초기화 (문자열 끝)
    cursor = len(s)  # 커서는 현재 문자열의 끝에 위치

    # 명령 처리
    M = int(input())  # 명령 개수 입력
    for _ in range(M):
        cmd = input().split()  # 명령과 인자를 분리
        if cmd[0] == 'L':
            # 커서를 왼쪽으로 한 칸 이동
            if cursor > 0:
                cursor -= 1
        elif cmd[0] == 'D':
            # 커서를 오른쪽으로 한 칸 이동
            # 연결 리스트 길이를 초과하지 않도록 확인
            if cursor < ll.get_length():
                cursor += 1
        elif cmd[0] == 'B':
            # 커서 왼쪽 문자를 삭제
            if cursor > 0:
                ll.delete(cursor - 1)  # 연결 리스트에서 노드 삭제
                cursor -= 1
        elif cmd[0] == 'P':
            # 커서 위치에 문자 삽입
            ll.insert(cursor, cmd[1])
            cursor += 1

    # 결과 출력
    # 연결 리스트를 순회하면서 각 노드 데이터를 결과 리스트에 저장
    result = []
    node = ll.head
    while node:
        result.append(node.data)
        node = node.link  # 다음 노드로 이동
    print(''.join(result))  # 모든 문자를 합쳐 최종 문자열 출력


if __name__ == "__main__":
    main()
