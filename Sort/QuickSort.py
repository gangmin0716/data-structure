# 퀵 정렬(Quick Sort) left ~ right 범위를 오름차순으로 정렬하는 재귀 함수
def quick_sort(A, left, right):
    if left < right:  # 정렬할 구간의 데이터가 2개 이상일 때만 수행
        q = partition(A, left, right)  # pivot을 기준으로 분할 수행
        quick_sort(A, left, q - 1)  # pivot 왼쪽 구간 정렬
        quick_sort(A, q + 1, right)  # pivot 오른쪽 구간 정렬


# pivot을 기준으로 왼쪽에는 작은 값, 오른쪽에는 큰 값을 두도록 재배치
# pivot의 최종 위치(high)를 반환
def partition(A, left, right):
    low = left + 1  # pivot 오른쪽에서 시작하는 포인터
    high = right  # 오른쪽 끝에서 시작하는 포인터
    pivot = A[left]  # pivot을 현재 구간의 맨 왼쪽 값으로 설정

    print(f"\n▶ partition({left}, {right})  pivot={pivot}")
    print("  시작:", A)

    # low와 high가 서로 교차하기 전까지 반복
    while low <= high:
        # low를 오른쪽으로 이동, pivot보다 크거나 같은 값에서 멈춤
        while low <= right and A[low] < pivot:
            low += 1
        # high를 왼쪽으로 이동, pivot보다 작거나 같은 값에서 멈춤
        while high >= left and A[high] > pivot:
            high -= 1

        # low <= high이면 둘 다 잘못된 구역에 있으므로 swap
        if low <= high:
            print(f"  swap: A[{low}]={A[low]} ↔ A[{high}]={A[high]}  (low={low}, high={high})")
            A[low], A[high] = A[high], A[low]  # swap
            print(f"    → swap 후: {A}")
            low += 1
            high -= 1

    # 반복문이 끝나면 high는 pivot이 들어가야 할 정확한 위치
    # pivot(A[left])과 A[high]를 교환하여 pivot을 제자리로 이동
    print(f"  pivot swap: A[{left}]={A[left]} ↔ A[{high}]={A[high]}  (pivot→{high})")
    A[left], A[high] = A[high], A[left]
    print(f"    → pivot 후: {A}")

    return high  # pivot의 최종 위치 반환


# 실행 부분
if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Original:", data)
    quick_sort(data, 0, len(data) - 1)
    print("\nFinal   :", data)