arr = list(map(int, input().split()));

a = arr[0];
b = arr[1];

max = arr[0] if arr[0] > arr[1] else arr[1];

print(max);