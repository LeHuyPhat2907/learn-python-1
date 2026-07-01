n = int(input("Nhập một số nguyên dương n: "))

total = 0
i = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print(f"Tổng các số chẵn từ 0 đến {n} là: {total}")