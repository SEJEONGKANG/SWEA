# 이분탐색

# import sys
# sys.stdin = open(r"C:\Users\sjkan\Desktop\swea\sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))

    start = 1
    end = max(arr) * M

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for i in range(N):
            count += mid // arr[i]
            if count >= M:
                result = mid
                end = mid-1
                break
        if count < M:
            start = mid+1

    print('#{} {}'.format(test_case, result))
