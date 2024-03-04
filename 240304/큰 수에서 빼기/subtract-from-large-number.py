arr = list(map(int, input().split()));

diff = arr[0] - arr[1];

if diff < 0:
    diff *= -1;

print(diff);