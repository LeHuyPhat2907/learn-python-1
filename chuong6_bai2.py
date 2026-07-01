# Kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(so_n):
    if n <= 0:
        return False
    
    tong_uoc = 0
    for i in range(1, so_n // 2 + 1):
        if so_n % i == 0:
            tong_uoc += i
        
    return tong_uoc == so_n


try:
    n = int(input("Nhập số nguyên dương lớn hơn 0: "))
    if kiem_tra_so_hoan_hao(n):
        print(f"Số {n} là số hoàn hảo.")
    else:
        print(f"Số {n} không phải số hoàn hảo.")
except ValueError:
    print("Vui lòng nhập vào số nguyên dương hợp lệ!")