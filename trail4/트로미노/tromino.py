n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

blocks = [
    [(0,0), (0, 1), (0, 2)],
    [(0,0), (1,0), (2,0)],

    [(0,0), (1,0), (1,1)],
    [(0,0),(0,1),(1,0)],
    [(0,0), (0,1), (1,1)],
    [(1,0), (1,1), (0,1)]
]

answer = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            total = 0
            possible = True
            for dx, dy in block:
                nx = i + dx
                ny = j + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    possible = False
                    break
            
                total += grid[nx][ny]
            
            if possible:
                answer = max(answer, total)

print(answer)

