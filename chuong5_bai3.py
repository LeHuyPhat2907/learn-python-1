n = int(input("Nhập một số nguyên dương n: "))

total = 1
for i in range(1, n+1):
    total *= i

print(f"{n}! = {total}")