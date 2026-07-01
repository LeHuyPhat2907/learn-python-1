def in_bang_cuu_chuong(n):
    """
    Hàm in bảng cửu chương của một số nguyên n.
    """
    print(f"--- BẢNG CỬU CHƯƠNG {n} ---")
    
    # Sử dụng vòng lặp từ 1 đến 10
    # Lưu ý: range(1, 11) sẽ tạo ra các số từ 1 đến 10 (không bao gồm 11)
    for i in range(1, 11):
        # Tính kết quả
        ket_qua = n * i
        
        # In ra màn hình theo đúng định dạng yêu cầu
        print(f"{n} x {i} = {ket_qua}")

# --- Chương trình chính (Nhập/Xuất) ---
try:
    so_n = int(input("Nhập vào số nguyên n: "))
    in_bang_cuu_chuong(so_n)
    
except ValueError:
    print("⚠️ Lỗi: Vui lòng nhập vào một số nguyên hợp lệ!")