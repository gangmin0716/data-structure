from ArrayStack import ArrayStack

def main():
    # 입력: 테스트 케이스 개수 N을 입력받음
    N = int(input().strip())  # 예) 3

    # N개의 문장을 순서대로 처리
    for i in range(1, N + 1):
        words = input().split()  # 문장을 공백 기준으로 단어 리스트로 분리
        # 예) "this is a test" → ["this", "is", "a", "test"]

        # ArrayStack 생성 (스택의 최대 용량은 단어 개수만큼)
        stack = ArrayStack(len(words))

        # 스택에 단어들을 차례로 push (스택의 특성: 나중에 들어온 게 먼저 나감)
        for w in words:
            stack.push(w)
            # push 순서: this → is → a → test
            # 스택 상태(top이 오른쪽이라면): [this, is, a, test]

        # 스택에서 pop을 이용해 단어를 꺼내면, 입력의 역순으로 나옴
        reversed_words = []
        while not stack.isEmpty():
            reversed_words.append(stack.pop())
            # pop 순서: test → a → is → this
            # reversed_words = ["test", "a", "is", "this"]

        # 결과 출력: 각 케이스 앞에 "Case #i:"를 붙이고 뒤집은 문장을 출력
        print(f"Case #{i}:", " ".join(reversed_words))
        # 출력 예: Case #1: test a is this

if __name__ == "__main__":
    main()
