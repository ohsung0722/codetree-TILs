arr = list(map(int, input().split()));

total = sum(arr);
avg = int(total / len(arr));

diff = total - avg;

print(total);
print(avg);
print(diff);