arr = list(map(int, input().split()));

height = arr[0] / 100;
weight = arr[1];
bmi = int(weight / (height*height));

print(bmi);

if bmi >= 25:
    print("Obesity");