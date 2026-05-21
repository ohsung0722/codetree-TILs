n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
answer = 0

def get_count(x, y, k):
    count = 0

    for i in range(n):
        for j in range(n):
            if abs(i - x) + abs(j - y) <= k:
                count += grid[i][j]

    return count

for i in range(n):
    for j in range(n):
        for k in range(2 * n): #중심 기준으로 마름모가 격자를 덮는 최대값
            gold_count = get_count(i, j, k)
            cost = k * k + (k + 1) * (k + 1)

            if gold_count * m >= cost:
                answer = max(answer, gold_count)

print(answer)
