# 중간 과정 출력용 함수
def printStep(arr, val):
    print(" Step %2d = " % val, end='')
    print(arr)


# 삽입 정렬 알고리즘
def insertion_sort(A):
    n = len(A)  # 배열의 길이 저장
    for i in range(1, n):  # 두 번째 원소 부터 끝가지 반복
        key = A[i]  # 현재 삽입할 값을 key에 저장
        j = i - 1  # 비교하게 될 값의 인덱스
        # key 보다 큰 원소들은 한 칸씩 오른쪽으로 이동
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]  # 오른쪽으로 이동
            j -= 1  # 비교하는 위치 인덱스 이동
        A[j + 1] = key  # key가 들어갈 위치에 삽입
        printStep(A, i)


if __name__ == "__main__":
    org = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    data = list(org)
    print("Original  :", org)
    insertion_sort(data)
    print("Insertion :", data)