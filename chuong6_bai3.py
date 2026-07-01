# Kiểm tra số chính phương
import math

def kiem_tra_so_chinh_phuong(n):
    temp = math.sqrt(n)
    so_chinh_phuong = temp * temp
    return so_chinh_phuong == n

try:
    n = int(input("Nhập số nguyên dương n: "))
    if kiem_tra_so_chinh_phuong(n):
        print(f"Số {n} là số chính phương.")
    else:
        print(f"Số {n} không phải số chính phương.")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")