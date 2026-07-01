def xu_ly_uoc_chung(a, b):
    """
    Hàm tìm UCLN và đếm số lượng ước chung của 2 số nguyên a và b.
    """
    # Bước 1: Lấy giá trị tuyệt đối để xử lý trường hợp người dùng nhập số âm
    a = abs(a)
    b = abs(b)
    
    # Xử lý trường hợp đặc biệt khi cả 2 số đều bằng 0
    if a == 0 and b == 0:
        print("Cả hai số đều là 0, chúng có vô số ước chung và không có UCLN.")
        return

    # Bước 2: Tìm UCLN bằng Thuật toán Euclid
    # Sử dụng 2 biến tạm để không làm thay đổi giá trị a, b ban đầu lúc in ra
    x, y = a, b
    while y != 0:
        # Lặp liên tục việc chia lấy dư cho đến khi phần dư bằng 0
        x, y = y, x % y
    
    ucln = x # Khi y = 0, x chính là Ước chung lớn nhất
    
    # Bước 3: Đếm số lượng ước chung (chính là số lượng ước của UCLN)
    dem_uoc_chung = 0
    
    # (Tùy chọn) In ra danh sách các ước chung cho rõ ràng
    # print("Các ước chung là:", end=" ")
    
    for i in range(1, ucln + 1):
        if ucln % i == 0:
            dem_uoc_chung += 1
            # print(i, end=" ")
            
    # Bước 4: In kết quả ra màn hình
    print(f"Ước chung lớn nhất (UCLN) của {a} và {b} là: {ucln}")
    print(f"Số {a} và {b} có tất cả {dem_uoc_chung} ước chung.")

# --- Chương trình chính (Nhập/Xuất) ---
try:
    so_a = int(input("Nhập vào số nguyên a: "))
    so_b = int(input("Nhập vào số nguyên b: "))
    
    print("-" * 30)
    xu_ly_uoc_chung(so_a, so_b)
    print("-" * 30)
        
except ValueError:
    print("Lỗi: Vui lòng nhập vào số nguyên hợp lệ!")