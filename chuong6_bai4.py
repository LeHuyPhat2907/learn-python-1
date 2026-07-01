# kiểm tra số nguyên tố

def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
    
def dem_so_nguyen_to(n):
    dem = 0
    for i in range(0,n+1):
        if kiem_tra_so_nguyen_to(i):
            dem += 1
    return dem

def tong_so_nguyen_to(n):
    tong = 0
    for i in range(0, n+1):
        if kiem_tra_so_nguyen_to(i):
            tong += i
    return tong

try:
    n = int(input("Nhập số nguyên dương n: "))
    dem = dem_so_nguyen_to(n)
    tong = tong_so_nguyen_to(n)
    print(f"Từ 1 đến {n} có {dem} số nguyên tố!")
    print(f"Tổng các số nguyên tố: {tong}")
except ValueError:
    print("Vui lòng nhập số nguyên dương hợp lệ!")