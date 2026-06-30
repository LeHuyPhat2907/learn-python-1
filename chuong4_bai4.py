# Máy ATM
total = 0

while True:
    print("==== MAY ATM ===")
    print("0. Thoát chương trình")
    print("1. Xem số tiền hiện tại")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("================")
    choice = input("Nhập lựa chọn: ")
    match choice:
        case "0":
            print("Đã thoát chương trình")
            break
        case "1":
            print(f"Số tiền hiện tại: {total}")
        case "2":
            money = int(input("Nhập số tiền bạn muốn nạp: "))
            total += money
            print(f"Nạp tiền thành công. Số dư mới: {total}")
        case "3":
            money = int(input("Nhập số tiền muốn rút: "))
            total -= money
            print(f"Đã rút thành công {money} VND. Số dư hiện tại {total}")
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại")
            