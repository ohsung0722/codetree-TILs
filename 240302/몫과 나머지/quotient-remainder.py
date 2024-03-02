a,b = input().split();

a = int(a);
b = int(b);

div = a // b;
last = a % b;

print(f"{div}...{last}")