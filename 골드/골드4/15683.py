import sys
import copy
input = sys.stdin.readline

# 문제 이해를 잘 이해하지 못했다
# CCTV별 이동 가능한 방향을 재귀적으로 표현할 방법을 찾지 못했다.

# CCTV 종류별, 바라보는 방향별 감시영역 재귀적 탐색
def dfs(graph, depth):
    global answer
    # 종료 조건: 모든 CCTV 탐색
    if depth == len(cctv_list):
        # 사각지대 최솟값
        answer = min(answer, count_zero(graph))
        return
    else:
        # 사무실 정보 깊은 복사
        graph_copy = copy.deepcopy(graph)
        x, y, cctv_type = cctv_list[depth]
        for cctv_dir in cctv_direction[cctv_type]:
            # CCTV 감시영역 구하는 함수 호출
            watch(x, y, cctv_dir, graph_copy)
            # 현재 Case에서 타 모든 CCTV 재귀적 탐색
            dfs(graph_copy, depth + 1)
            # CCTV를 다른 방향으로 회전시킨 후 재탐색하기 위함
            graph_copy = copy.deepcopy(graph)

# CCTV 감시영역 구하는 함수
def watch(a, b, direction, graph):
    for d in direction:
        x = a
        y = b
        # 특정 방향으로 벽을 만나거나 사무실을 벗어나기 전까지 탐색
        while True:
            x += dx[d]
            y += dy[d]
            # 맵 내 위치
            if 0 <= x < n and 0 <= y < m:
                # 벽을 만난 경우
                if graph[x][y] == 6:
                    break
                # 새로운 감시가능 영역일 경우
                elif graph[x][y] == 0:
                    graph[x][y] = '#'
            # 맵 외 위치
            else:
                break

# 사각지대 개수 구하는 함수
def count_zero(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
# 최솟값을 구하기 위해 초기값 10억 세팅
answer = int(1e9)
cctv_list = []
for i in range(n):
    for j in range(m):
        if 1 <= arr[i][j] <= 5:
            # CCTV 좌표 및 종류 저장
            cctv_list.append((i, j, arr[i][j]))
            
# 탐색 방향: 상, 하, 좌, 우
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# CCTV별 이동 가능한 방향
cctv_direction = [
    [],
    [[0], [1], [2], [3]], # 1번 CCTV
    [[0, 2], [1, 3]], # 2번 CCTV
    [[0, 1], [1, 2], [2, 3], [0, 3]], # 3번 CCTV
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번 CCTV
    [[0, 1, 2, 3]] # 5번 CCTV
    ]
dfs(arr, 0)
print(answer)