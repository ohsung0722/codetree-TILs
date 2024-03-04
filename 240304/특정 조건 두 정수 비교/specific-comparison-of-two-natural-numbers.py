a,b = list(map(int, input().split()));

if a > b:
    print(0, end=" ");
else:
    print(1, end=" ");

if a == b:
    print(1);
else:
    print(0);